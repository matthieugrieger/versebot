"""
VerseBot for reddit
By Matthieu Grieger
localbible.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from os.path import isfile
from pickle import load
from collections import OrderedDict
from versebot import bot

class LocalBible:
    """ Definition of a local (pickled) Bible class. """
    
    def __init__(self, translation, translation_title, translation_copyright, filepath):
        if isfile(filepath):
            self.filepath = filepath
        else:
            raise Exception("Invalid filepath for %s translation." % translation)
        self.translation = translation
        self.translation_title = translation_title
        self.translation_copyright = translation_copyright
        
    def get_contents(self, book_num, chapter, verse):
        """ Retrieve the contents of the Bible passage the user requested.
        Obtains text from local pickle file. Used for translations that
        BibleGateway does not support. """
        
        f = open(self.filepath, "rb")
        bible = load(f)
        f.close()
        
        contents = ""
        if book_num and chapter:
            try:
                if verse != "0":
                    if "-" in verse:
                        starting_verse, _, ending_verse = verse.partition("-")
                        if int(starting_verse) < int(ending_verse) + 1:
                            for v in range(int(starting_verse), int(ending_verse) + 1):
                                contents += "[**%d**] %s " % (v, bible[str(book_num)][chapter][v])
                        else:
                            raise Exception("Ending verse is less than starting verse.")
                    else:
                        contents = "[**%s**] %s " % (verse, bible[book_num][chapter][int(verse)])
                else:
                    for v in bible[book_num][chapter]:
                        contents += "[**%d**] %s " % (v, bible[str(book_num)][chapter][v])
                            
                return contents
            except KeyError:
                raise Exception("An error occurred while reading verse data from pickle file.")
                            
                        
