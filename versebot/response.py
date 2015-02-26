"""
VerseBot for reddit
By Matthieu Grieger
response.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

class Response:
    """ Class that holds the properties and methods of a comment 
    response. """
    
    def __init__(self, message, parser):
        """ Initializes a Response object. """
        self._verse_list = list()
        self.message = message
        self.parser = parser
        self.response = ""
        
    def add_verse(verse):
        """ Adds a verse to the verse list. """
        self._verse_list.append(verse)
        
    def construct_message(self):
        """ Constructs a message response. """
        for verse in self._verse_list:
            verse.get_contents(self.parser)
            if verse.verse != "0":
                self.response += ("[**%s %d %s | %s**](%s)\n"
                    % (verse.book, verse.chapter, verse.verse, verse.translation_title, 
                        verse.permalink))
            else:
                self.response += ("[**%s %d | %s**](%s)\n"
                    % (verse.book, verse.chapter, verse.translation_title, verse.permalink))
            self.response += verse.contents
        self.response += "\n\n***"
        
    def get_comment_footer(self):
        return "The comment footer will go here."
