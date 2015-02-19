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
import regex
import webparser
import localbible

class TestBookRetrieval(unittest.TestCase):
    """ Tests book retrieval and parsing functions. """
    
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
        
    def test_tanakh_name_retrieval(self):
        """ Tests TaggedTanakh URL book name retrieval. """
        self.assertTrue(books.get_tanakh_name("Genesis") == "Gen")
        self.assertTrue(books.get_tanakh_name("2 Chronicles") == "2%20Chron")
        
        
class TestBibleGatewayParsing(unittest.TestCase):
    """ Tests parsing of BibleGateway webpages. """
    
    def test_supported_translation_retrieval(self):
        """ Tests retrieval of supported translations. """
        parser = webparser.Parser()
        self.assertTrue(len(parser.translations) != 0)
        
    def test_bible_gateway_text_retrieval(self):
        """ Tests the retrieval of BibleGateway verse contents. """
        parser = webparser.Parser()
        self.assertTrue("In the beginning, God created the heavens and the earth." in 
            parser.get_bible_gateway_verse("Genesis", "1", "1", "esv"))
            
class TestLocalBibleRetrieval(unittest.TestCase):
    """ Tests verse text retrieval from local pickle files. """
    
    def test_local_text_retrieval(self):
        """ Tests retrieval of Genesis 1:1 from NJPS pickle file. """
        bible = localbible.LocalBible("NJPS", "JPS Tanakh (NJPS)", "Copyright", "../bibles/NJPS.pickle")
        self.assertTrue("When God began to create heaven and earth—" in
            bible.get_contents(1, 1, "1"))
        

class TestRegex(unittest.TestCase):
    """ Tests regular expressions. """
    
    def test_verse_regex(self):
        self.assertTrue(regex.find_verses("Testing testing! [genesis 5:3-5 (nrsv)]") != None)
        self.assertTrue(regex.find_verses("[genesis (nrsv)") == None)


if __name__ == "__main__":
    unittest.main()
