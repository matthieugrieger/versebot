#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import re
import regex
import database
import data
from threading import Timer
from verse import Verse
from config import get_bot_username

# Begins to scan unread inbox messages to check for various triggers that
# allow VerseBot users to interact with the bot.
def check_messages(r):
	Timer(60, check_messages, [r]).start()
	print('Checking messages....')
	messages = r.get_unread()
	for message in messages:
		if 'edit' in message.subject:
			process_edit_request(r, message)
		elif 'delete' in message.subject:
			process_delete_request(r, message)

# Processes an edit request if found in check_messages(). Simply reconstructs
# an updated VerseBot comments based on the user's revised verse quotations,
# and replaces the outdated comment with the updated one. Additionally, the bot
# sends the user a message letting them know that the edit has been completed
# successfully.
# NOTE: Users can only edit a VerseBot comment if they authored the parent
# comment of VerseBot's reply.
def process_edit_request(r, message):
	try:
		comment_url = message.subject[5:]
		comment = r.get_submission(comment_url)
	except:
		message.reply('An error occurred while processing your request. Please make sure that you do not modify the subject line of your message to VerseBot.')
		comment = False
	if message.author == comment.author and comment:
		verses_to_find = regex.find_bracketed_text(message.body)
		lookup_list = list()
		if len(verses_to_find) != 0:
			for ver in verses_to_find:
				next_ver = regex.find_verses(ver)
				lookup_list.append(str(next_ver))
			if len(lookup_list) != 0:
				for reply in comment.comments[0].replies:
					if str(reply.author) == get_bot_username():
						try:
							print(str(comment.author) + ' has requested a comment edit...')
							link = reply.permalink[24:comment.permalink.find('/', 24)]
							verse_object = Verse(lookup_list, message, comment_url, link)
							edited_comment = '*^This ^comment ^has ^been ^edited ^by ^' + str(comment.author) + '.* \n\n' + verse_object.get_comment()
							remove_invalid_statistics(reply.body, link)
							reply.edit(edited_comment)
							database.update_db_stats(verse_object)
							verse_object.clear_verses()
							message.mark_as_read()
							message.reply('[Your triggered VerseBot response](' + comment_url + ') has been successfully edited to reflect your updated quotations.')
							break
						except:
							print('Comment edit failed. Will try again later...')
							verse_object.clear_verses()
					else:
						message.mark_as_read()
				lookup_list[:] = []
			else:
				message.mark_as_read()
	else:
		message.mark_as_read()

# Processes a delete request if found in check_messages(). Simply deletes
# the requested comment. Additionally, the bot sends the user a message
# letting them know that the deletion has been completed successfully.
# NOTE: Users can only delete a VerseBot comment if they authored the parent
# comment of VerseBot's reply.
def process_delete_request(r, message):
	try:
		comment_url = message.subject[7:]
		comment = r.get_submission(comment_url)
	except:
		message.reply('An error occurred while processing your request. Please make sure that you do not modify the subject line of your message to VerseBot.')
		comment = False
	if message.author == comment.author and comment:
		for reply in comment.comments[0].replies:
			if str(reply.author) == get_bot_username():
				try:
					print(str(comment.author) + ' has requested a comment deletion...')
					remove_invalid_statistics(reply.body, reply.permalink[24:comment.permalink.find('/', 24)])
					reply.delete()
					message.mark_as_read()
					message.reply('VerseBot\'s response to [your comment](' + comment_url + ') has been deleted. Sorry for any inconvenience!')
					break
				except:
					print('Comment deletion failed. Will try again later...')
			else:
				message.mark_as_read()
	else:
		message.mark_as_read()
		
# Corrects database statistics entries before a comment is edited or deleted.
def remove_invalid_statistics(comment_body, subreddit):
	print('Removing invalid statistics...')
	invalid_verses = regex.find_already_quoted_verses(comment_body)
	invalid_books = dict()
	invalid_trans = dict()
	invalid_sub = dict()
	
	for verse in invalid_verses:
		book_num = data.get_book_number(verse.lower())
		if book_num:
			invalid_book = data.get_book_title(book_num)
			translation = regex.find_translation_in_title(verse)
			if invalid_book in invalid_books:
				invalid_books[invalid_book] += 1
			else:
				invalid_books[invalid_book] = 1
			if translation in invalid_trans:
				invalid_trans[translation] += 1
			else:
				invalid_trans[translation] = 1
			if subreddit in invalid_sub:
				invalid_sub[subreddit] += 1
			else:
				invalid_sub[subreddit] = 1
			
	database.fix_db_stats(invalid_books, invalid_trans, invalid_sub)	
		
