"""
VerseBot for reddit
By Matthieu Grieger
database.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from config import *
import psycopg2
import urlparse

_conn = None

def connect():
    """ Connect to PostgreSQL database. The connection information for the
    database is retrieved via Heroku environment variable."""

    global _conn
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(HEROKU_DB)
    try:
        _conn = psycopg2.connect(
            database = url.path[1:],
            user = url.username,
            password = url.password,
            host = url.hostname,
            port = url.port)
        return True
    except:
        exit()

def update_book_stats(new_books, is_edit_or_delete=False):
    """ Updates book_stats table with recently quoted books.
    Alternatively, this function is also used to remove book counts
    that were added by a comment that has been edited/deleted. """

    for book in new_books.items():
        with _conn.cursor() as cur:
            if is_edit_or_delete:
                cur.execute("UPDATE book_stats SET count = count - %s WHERE book = %s", [book[1], book[0]])
            else:
                cur.execute("UPDATE book_stats SET count = count + %s WHERE book = %s", [book[1], book[0]])
    _conn.commit()

def update_translation_stats(new_subreddits, is_edit_or_delete=False):
	""" Updates subreddit_stats table with subreddits that have recently used VerseBot.
	Alternatively, this function is also used to remove subreddit counts that were
	added by a comment that has been edited/deleted. """
	
	for subreddit in new_subreddits.items():
		with _conn.cursor() as cur:
			if is_edit_or_delete:
				cur.execute("UPDATE subreddit_stats SET count = count - %(num)s WHERE sub = %(subreddit)s;" +
					"DELETE FROM subreddit_stats WHERE count = 0;", {"subreddit":subreddit[0], "num":subreddit[1]})
			else:
				# I opted for this instead of upsert because it seemed simpler.
				cur.execute("UPDATE subreddit_stats SET count = count + %(num)s WHERE sub = %(subreddit)s;" +
					"INSERT INTO subreddit_stats (sub, count) SELECT %(subreddit)s, %(num)s WHERE NOT EXISTS" +
					"(SELECT 1 FROM subreddit_stats WHERE sub = %(subreddit)s);",
					{"subreddit":subreddit[0], "num":subreddit[1]})
	_conn.commit()
	
