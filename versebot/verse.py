"""
VerseBot for reddit
By Matthieu Grieger
verse.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

import database
import books

class Verse:
    """ Class that holds the properties and methods of a Verse object. """

    def __init__(self, book, chapter, translation, user, subreddit, verse="0"):
        """ Initializes a Verse object with book, chapter, verse (if
        exists), and translation (if exists). """
        self.book = book
        book_num = books.get_book_number(self.book)
        if book_num <= 39:
            self.bible_section = "Old Testament"
        else if book_num <= 66:
            self.bible_section = "New Testament"
        else:
            self.bible_section = "Deuterocanon"

        self.chapter = int(chapter.replace(" ", ""))
        self.verse = verse.replace(" ", "")
        if translation:
            self.translation = translation.upper().replace(" ", "")
        else:
            user_default = database.get_user_default_translation(user, self.bible_section)
            if user_default:
                self.translation = user_default
            else:
                subreddit_default = database.get_subreddit_default_translation(subreddit, self.bible_section)
                if subreddit_default:
                    self.translation = subreddit_default
                else:
                    if self.bible_section == "Old Testament":
                        self.translation = "ESV"
                    else if self.bible_section == "New Testament":
                        self.translation = "ESV"
                    else:
                        self.translation = "NRSV"

        self.verse_title = ""
        self.translation_title = ""
        self.contents = ""

    def get_contents(self, parser):
        """ Retrieves the contents of a Verse object if it exists in
        the supported translation list. """
        if self.translation in parser.translations:
            self.contents = self.parser.get_bible_gateway_verse(self)
