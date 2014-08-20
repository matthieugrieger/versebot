#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import praw
import config
import database
import requests
import regex
import datetime
from helpers import find_supported_translations
from verse import Verse
from messages import check_messages

from sys import exit
from re import findall
from time import sleep
from os import environ

def main():
	print('Starting up VerseBot...')

	# Connects to reddit via PRAW.
	try:
		r = praw.Reddit(user_agent = ('VerseBot by /u/mgrieger. Github: https://github.com/matthieugrieger/versebot'))
		r.login(config.get_bot_username(), config.get_bot_password())
		print('Connected to reddit!')
	except:
		print('Connection to reddit failed. Either reddit is down at the moment or something in the config is incorrect.')
		exit()

	print('Connecting to database...')
	database.connect()
	print('Cleaning database...')
	database.clean_comment_id_database()

	print('Retrieving supported translations...')
	find_supported_translations()

	lookup_list = list()
	comment_ids_this_session = set()
	
	check_message_timer = datetime.datetime.utcnow()
	
	print('Beginning to scan comments...')
	while True:
		comments = praw.helpers.comment_stream(r, 'all', limit=None)
		for comment in comments:
			# This if statement allows for messages to be checked every 2 minutes (or so). Ideally this would be
			# done with another timed thread, but Reddit objects in PRAW (which check_messages() takes as
			# an argument) are not thread-safe.
			if (datetime.datetime.utcnow() - check_message_timer).seconds >= 120:
				print('Checking messages...')
				check_messages(r)
				check_message_timer = datetime.datetime.utcnow()
			if comment.author != config.get_bot_username() and not database.check_comment_id(comment.id) and comment.id not in comment_ids_this_session:
				comment_ids_this_session.add(comment.id)
				verses_to_find = regex.find_bracketed_text(comment.body)
				if len(verses_to_find) != 0:
					for ver in verses_to_find:
						next_ver = regex.find_verses(ver)
						lookup_list.append(str(next_ver))

					if len(lookup_list) != 0:
						verse_object = Verse(lookup_list, comment)
						next_comment = verse_object.get_comment()
						if next_comment != False:
							try:
								comment.reply(next_comment)
							except requests.exceptions.HTTPError, err:
								# If true, this means the bot is banned.
								if str(err) == '403 Client Error: Forbidden':
									print('Banned from subreddit. Cannot reply.')
									next_comment = False
							except praw.errors.APIException, err:
								if err.error_type in ('TOO_OLD','DELETED_LINK', 'DELETED_COMMENT'):
									next_comment = False
								else:
									raise
					else:
						next_comment = False

					if next_comment != False:
						print('Inserting new comment id to database...')
						database.add_comment_id(comment.id)
						print('Updating statistics...')
						database.update_db_stats(verse_object)

						lookup_list[:] = []
					else:
						try:
							comment_ids_this_session.remove(comment.id)
						except KeyError:
							pass
						lookup_list[:] = []
					verse_object.clear_verses()

if __name__ == '__main__':
	main()
