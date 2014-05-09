#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import unittest
import sys
import os

sys.path.append(os.path.join('..', 'versebot'))
import helpers
import database
import data

class TestBibleGateway(unittest.TestCase):
	def test_supported_translations_retrieval(self):
		helpers.find_supported_translations()
		self.assertTrue(helpers.get_supported_translations() != 0)
	
	def test_passage_retrieval(self):
		self.assertTrue(helpers.get_verse_contents('Genesis', '1', '1', 'ESV') != False)
		
class TestDatabase(unittest.TestCase):
	def test_database_connection(self):
		self.assertTrue(database.connect())
		
#class TestRegex(unittest.TestCase):
#	def test_verse_regex(self):

class TestDataFunctions(unittest.TestCase):
	def test_get_book_number(self):
		self.assertTrue(data.get_book_number('[1 corinthians 1:1]') == 46)
	
	def test_get_book_title(self):
		self.assertTrue(data.get_book_title(46) == '1 Corinthians')
		
	def test_default_translations(self):
		self.assertTrue(data.get_default_translation('Catholicism', 3) == 'DRA')
		self.assertTrue(data.get_default_translation('Christianity', 3) == 'ESV')		
		
		
if __name__ == '__main__':
	unittest.main()
