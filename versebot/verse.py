"""
VerseBot for reddit
By Matthieu Grieger
verse.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

class Verse:
    """ Class that holds the properties and methods of a Verse object. """
    
    def __init__(self, book, chapter, verse, translation):
        """ Initializes a Verse object with book, chapter, verse (if
        exists), and translation (if exists). """
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.translation = translation
