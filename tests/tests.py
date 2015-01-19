"""
VerseBot for reddit
By Matthieu Grieger
tests.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

import unittest
import sys
import os

sys.path.append(os.path.join('..', 'versebot'))
import database
import books

class TestBookRetrieval(unittest.TestCase):
    """ Test book retrieval and parsing functions. """
    
    def test_book_standardization(self):
        """ Tests book conversion to standardized book names. """
        self.assertTrue(books.get_book("1 Jn") == "1 John")
        self.assertTrue(books.get_book("ti") == "Titus")
        self.assertTrue(books.get_book("thisisntabook") == False)
    
    def test_book_number_retrieval(self):
        """ Tests book number retrieval. """
        self.assertTrue(books.get_book_number("Genesis") == 1)
        self.assertTrue(books.get_book_number("Bel and the Dragon") == 82)
        self.assertTrue(books.get_book_number("thisisntabook") == False)


if __name__ == "__main__":
    unittest.main()
