"""
VerseBot for reddit
By Matthieu Grieger
response.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from config import REDDIT_USERNAME

class Response:
    """ Class that holds the properties and methods of a comment 
    response. """
    
    def __init__(self, message, parser):
        """ Initializes a Response object. """
        self.verse_list = list()
        self.message = message
        self.parser = parser
        self.response = ""
        
    def add_verse(self, verse):
        """ Adds a verse to the verse list. """
        self.verse_list.append(verse)
        
    def construct_message(self):
        """ Constructs a message response. """
        for verse in self.verse_list:
            verse.get_contents(self.parser)
            if verse.verse != "0":
                self.response += ("[**%s %d:%s | %s**](%s)\n\n>"
                    % (verse.book, verse.chapter, verse.verse, verse.translation_title, 
                        verse.permalink))
            else:
                self.response += ("[**%s %d | %s**](%s)\n\n>"
                    % (verse.book, verse.chapter, verse.translation_title, verse.permalink))
            self.response += verse.contents
            self.response += "\n\n"
        self.response += self.get_comment_footer()
        return self.response
        
    def get_comment_footer(self):
        """ Returns the footer for the comment. """
        return ("\n***\n[^Code](https://github.com/matthieugrieger/versebot) ^|"
            " ^/r/VerseBot ^| [^Contact ^Dev](http://www.reddit.com/message/compose/?to=mgrieger) ^|"
            " [^Usage](https://github.com/matthieugrieger/versebot/blob/master/README.md) ^|"
            " [^Changelog](https://github.com/matthieugrieger/versebot/blob/master/CHANGELOG.md) ^|"
            " [^Stats](http://matthieugrieger.com/versebot) \n\n"
            "^All ^texts ^provided ^by [^BibleGateway](http://biblegateway.com) ^and [^Mechon ^Mamre](http://mechon-mamre.org)^. \n\n"
            " ^**Mistake?** ^%(user)s ^can [^edit](http://www.reddit.com/message/compose/?to=%(bot)s&subject=edit&message={%(link)s} "
            "Please+enter+your+revised+verse+quotations+below+in+the+usual+bracketed+syntax.)" 
            " ^or [^delete](http://www.reddit.com/message/compose/?to=%(bot)s&subject=delete&message={%(link)s} "
            "This+action+cannot+be+reversed!) ^this ^comment." 
            % {"user":self.message.author, "bot":REDDIT_USERNAME, "link":self.message.permalink})
