"""
VerseBot for reddit
By Matthieu Grieger
translation.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

class Translation:
    """ A Translation class that holds various properties regarding a specific translation. """

    def __init__(self, name, abbreviation, language, has_ot=True, has_nt=True, has_deut=False):
        """ Initializes a Translation object. """
        self.name = name
        self.abbreviation = abbreviation
        self.language = language
        self.has_ot = has_ot
        self.has_nt = has_nt
        self.has_deut = has_deut
