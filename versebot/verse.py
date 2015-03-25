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

    def __init__(self, book, chapter, translation, user, subreddit, verse):
        """ Initializes a Verse object with book, chapter, verse (if
        exists), and translation (if exists). """
        self.book = book
        book_num = books.get_book_number(self.book)
        if book_num <= 39:
            self.bible_section = "Old Testament"
        elif book_num <= 66:
            self.bible_section = "New Testament"
        else:
            self.bible_section = "Deuterocanon"

        self.chapter = int(chapter.replace(" ", ""))
        if verse != "":
            self.verse = verse.replace(" ", "")
        else:
            self.verse = None
        if translation != "":
            trans = translation.upper().replace(" ", "")
            if database.is_valid_translation(trans, self.bible_section):
                self.translation = trans
            else:
                self.determine_translation(user, subreddit)
        else:
            self.determine_translation(user, subreddit)

        self.verse_title = ""
        self.translation_title = ""
        self.contents = ""
        self.permalink = ""
        
    def determine_translation(self, user, subreddit):
        """ Determines which translation should be used when either the user does not provide
        a translation, or when the user provides an invalid translation. """
        user_default = database.get_user_translation(user.name, self.bible_section)
        if user_default:
            self.translation = user_default
        else:
            subreddit_default = database.get_subreddit_translation(subreddit, self.bible_section)
            if subreddit_default:
                self.translation = subreddit_default
            else:
                if self.bible_section == "Old Testament":
                    self.translation = "ESV"
                elif self.bible_section == "New Testament":
                    self.translation = "ESV"
                else:
                    self.translation = "NRSV"

    def get_contents(self, parser):
        """ Retrieves the contents of a Verse object. """
        self.contents, self.verse_title, self.translation_title, self.permalink = parser.get_bible_gateway_verse(self)
