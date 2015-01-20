"""
VerseBot for reddit
By Matthieu Grieger
response.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

class Response:
    """ Class that holds the properties and methods of a comment 
    response. """
    
    def __init__(self, message):
        """ Initializes a Response object. """
        self._verse_list = list()
        
    def add_verse(verse):
        """ Adds a verse to the verse list. """
        self._verse_list.append(verse)
        
    def construct_message(self):
        """ Constructs a message response. """
