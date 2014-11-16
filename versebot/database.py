"""
#---------------------#
| VerseBot for reddit |
| By Matthieu Grieger |
#---------------------#
"""

import config
import psycopg2
import urlparse
from os import environ

_conn = None


def connect():
	""" Connect to PostgreSQL database. The connection information for the
	database is retrieved via Heroku environment variable. """
	
	global _conn
	urlparse.uses_netloc.append('postgres')
	url = urlparse.urlparse(config.get_database())
	try:
		_conn = psycopg2.connect(
		database = url.path[1:],
		user = url.username,
		password = url.password,
		host = url.hostname,
		port = url.port)

		print('Connected to database!')
		return True
	except:
		print('Connection to database failed.')
		exit()


def add_comment_id(comment_id):
	""" Add new comment ID to the comment_ids database. Used to prevent the
	bot from spamming on posts it already replied to. """
	
	with _conn.cursor() as cur:
		cur.execute('INSERT INTO comment_ids (comment_id, timestamp) VALUES (%s, NOW())', [comment_id])
	_conn.commit()


def check_comment_id(comment_id):
	""" Checks database for the specified comment id. Used to check for comments
	that have already been replied to. """
	
	with _conn.cursor() as cur:
		cur.execute('SELECT count(*) FROM comment_ids WHERE comment_id = %s', [comment_id])
		return cur.fetchone()[0] > 0


def clean_comment_id_database():
	""" Deletes all entries in comment_ids that are 2 days old or older. This function
	is called approximately every 24 hours due to Heroku automatically restarting
	apps every 24 hours. """
	
	with _conn.cursor() as cur:
		cur.execute('DELETE FROM comment_ids WHERE timestamp < (NOW() - INTERVAL \'2 DAYS\')')
	_conn.commit()


def update_book_stats(new_books, is_edit_or_delete = False):
	""" Updates book_stats table with recently quoted books.
	Alternatively, this function is also used to remove book counts
	that were added by a comment that has been edited/deleted. """
	
	for book in new_books.items():
		with _conn.cursor() as cur:
			if is_edit_or_delete:
				cur.execute('UPDATE book_stats SET count = count - %s WHERE book = %s', [book[1], book[0]])
			else:
				cur.execute('UPDATE book_stats SET count = count + %s WHERE book = %s', [book[1], book[0]])
	_conn.commit()

	
def update_translation_stats(new_translations, is_edit_or_delete = False):
	""" Updates translation_stats table with recently used translations.
	Alternatively, this function is also used to remove translation counts
	that were added by a comment that has been edited/deleted. """
	
	for translation in new_translations.items():
		if translation[0] == 'NET':
			trans = 'NET Bible'
		else:
			trans = translation[0]
		count = translation[1]
		with _conn.cursor() as cur:
			if is_edit_or_delete:
				cur.execute('UPDATE translation_stats SET count = count - %s WHERE trans = %s', [count, trans])
			else:
				cur.execute('UPDATE translation_stats SET count = count + %s WHERE trans = %s', [count, trans])
	_conn.commit()


def update_subreddit_stats(new_subreddits, is_edit_or_delete = False):
	""" Updates subreddit_stats table with subreddits that have recently used VerseBot.
	Alternatively, this function is also used to remove subreddit counts
	that were added by a comment that has been edited/deleted. """
	
	for subreddit in new_subreddits.items():	
		with _conn.cursor() as cur:
			if is_edit_or_delete:
				cur.execute('UPDATE subreddit_stats SET count = count - %(num)s WHERE sub = %(subreddit)s;' +
						'DELETE FROM subreddit_stats WHERE count = 0;', {'subreddit':subreddit[0], 'num':subreddit[1]})
			else:
				# I opted for this instead of upsert because it seemed simpler.
				cur.execute('UPDATE subreddit_stats SET count = count + %(num)s WHERE sub = %(subreddit)s;' +
							'INSERT INTO subreddit_stats (sub, count) SELECT %(subreddit)s, %(num)s WHERE NOT EXISTS (SELECT 1 FROM subreddit_stats WHERE sub = %(subreddit)s);',
							{'subreddit':subreddit[0], 'num':subreddit[1]})
	_conn.commit()


def update_db_stats(verse_ob):
	""" Iterates through all verses in Verse object and adds them to dicts to
	pass to the database update functions.
	NOTE: verse[0] = book name
		verse[3] = translation name
		verse[5] = subreddit name """
		
	book_stats = dict()
	translation_stats = dict()
	subreddit_stats = dict()
	
	for verse in verse_ob.get_verse_data():
		if verse[0] in book_stats:
			book_stats[verse[0]] += 1
		else:
			book_stats[verse[0]] = 1
		
		if verse[3] in translation_stats:
			translation_stats[verse[3]] += 1
		else:
			translation_stats[verse[3]] = 1
			
		if verse[5] in subreddit_stats:
			subreddit_stats[verse[5]] += 1
		else:
			subreddit_stats[verse[5]] = 1
			
	update_book_stats(book_stats)
	update_translation_stats(translation_stats)
	update_subreddit_stats(subreddit_stats)
	
	return
	
	
def fix_db_stats(invalid_books, invalid_translations, invalid_subreddit):
	""" Calls other functions to clean up invalid statistics after a user
	has requested a comment edit or deletion. """
	
	update_book_stats(invalid_books, is_edit_or_delete = True)
	update_translation_stats(invalid_translations, is_edit_or_delete = True)
	update_subreddit_stats(invalid_subreddit, is_edit_or_delete = True)
	



	
