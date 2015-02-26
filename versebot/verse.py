"""
VerseBot for reddit
By Matthieu Grieger
verse.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

class Verse:
    """ Class that holds the properties and methods of a Verse object. """
    
    def __init__(self, book, chapter, translation, verse="0"):
        """ Initializes a Verse object with book, chapter, verse (if
        exists), and translation (if exists). """
        self.book = book.lower().replace(" ", "")
        self.chapter = int(chapter.replace(" ", ""))
        self.verse = verse.replace(" ", "")
        self.translation = translation.replace(" ", "")
        self.verse_title = ""
        self.translation_title = ""
        self.contents = ""
        
    def get_contents(self, parser):
        """ Retrieves the contents of a Verse object if it exists in
        the supported translation list. """
        if self.translation in parser.translations:
            self.contents = self.parser.get_bible_gateway_verse(self)
