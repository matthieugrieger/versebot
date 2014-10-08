"""
#---------------------#
| VerseBot for reddit |
| By Matthieu Grieger |
#---------------------#
"""

import unittest
import sys
import os

sys.path.append(os.path.join('..', 'versebot'))
import helpers
import database
import data


class TestBibleGateway(unittest.TestCase):
	""" Tests BibleGateway related functions. """
	
	def test_supported_translations_retrieval(self):
		""" Tests the retrieval of supported translations from BibleGateway. """
		
		helpers.find_supported_translations()
		self.assertTrue(helpers.get_supported_translations() != 0)


	def test_passage_retrieval(self):
		""" Tests the retrieval of verse texts from BibleGateway. """
		
		self.assertTrue(helpers.get_verse_contents('Genesis', '1', '1', 'ESV') != False)


class TestDatabase(unittest.TestCase):
	""" Tests database related functions. """
	
	def test_database_connection(self):
		""" Tests the ability for the bot to establish a database connection. """
		
		self.assertTrue(database.connect())


class TestDataFunctions(unittest.TestCase):
	""" Tests data related functions. """
	
	def test_get_book_number(self):
		""" Tests retrieval of book number from a verse quotation string. """
		
		self.assertTrue(data.get_book_number('[1 corinthians 1:1]') == 46)


	def test_get_book_title(self):
		""" Tests book title retrieval from a book number. """
		
		self.assertTrue(data.get_book_title(46) == '1 Corinthians')


	def test_default_translations(self):
		""" Tests subreddit-specific default translations. """
		
		self.assertTrue(data.get_default_translation('Catholicism', 3) == 'DRA')
		self.assertTrue(data.get_default_translation('Christianity', 3) == 'ESV')


if __name__ == '__main__':
	unittest.main()
