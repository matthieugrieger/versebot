"""
VerseBot for reddit
By Matthieu Grieger
response.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from config import REDDIT_USERNAME, MAXIMUM_MESSAGE_LENGTH

class Response:
    """ Class that holds the properties and methods of a comment
    response. """

    def __init__(self, message, parser, link=None):
        """ Initializes a Response object. """
        self.verse_list = list()
        self.message = message
        self.parser = parser
        self.response = ""
        if link is not None:
            self.link = link
        else:
            self.link = self.message.permalink

    def add_verse(self, verse):
        """ Adds a verse to the verse list. """
        self.verse_list.append(verse)

    def is_duplicate_verse(self, verse):
        """ Checks the incoming verse against the verse list to make sure
        it is not a duplicate. """
        for v in self.verse_list:
            if (v.book == verse.book and v.chapter == verse.chapter and
                v.verse == verse.verse and v.translation == verse.translation):
                return True
        return False

    def construct_message(self):
        """ Constructs a message response. """
        for verse in self.verse_list:
            verse.get_contents(self.parser)
            if verse.contents is not None:
                if verse.verse is not None:
                    self.response += ("[**%s %d:%s | %s**](%s)\n\n>"
                        % (verse.book, verse.chapter, verse.verse, verse.translation_title,
                            verse.permalink))
                else:
                    self.response += ("[**%s %d | %s**](%s)\n\n>"
                        % (verse.book, verse.chapter, verse.translation_title, verse.permalink))
                self.response += verse.contents
                self.response += "\n\n"
        if self.response == "":
            return None
        else:
            if self.exceeds_max_length():
                self.response = self.generate_overflow_response()
            self.response += self.get_comment_footer()
            return self.response

    def exceeds_max_length(self):
        """ Returns true if the current response exceeds the maximum comment
        length, returns false otherwise. """

        return len(self.response) > MAXIMUM_MESSAGE_LENGTH

    def generate_overflow_response(self):
        """ Constructs and generates an overflow comment whenever the comment
        exceeds the character limit set by MAXIMUM_MESSAGE_LENGTH. Instead of posting
        the contents of the verse(s) in the comment, it links to webpages that contain
        the contents of the verse(s). """

        comment = ("The contents of the verse(s) you quoted exceed the %d character limit."
        " Instead, here are links to the verse(s)!\n\n" % MAXIMUM_MESSAGE_LENGTH)

        for verse in self.verse_list:
            if verse.translation == "JPS":
                overflow_link = verse.permalink
            else:
                if verse.verse is not None:
                    overflow_link = ("https://www.biblegateway.com/passage/?search=%s+%s:%s&version=%s"
                        % (verse.book, verse.chapter, verse.verse, verse.translation))
                else:
                    overflow_link = verse.permalink

            if verse.verse is not None:
                comment += ("- [%s %d:%s (%s)](%s)\n\n" % (verse.book, verse.chapter,
                    verse.verse, verse.translation, overflow_link))
            else:
                comment += ("- [%s %d (%s)](%s)\n\n" % (verse.book, verse.chapter,
                    verse.translation, overflow_link))

        return comment

    def get_comment_footer(self):
        """ Returns the footer for the comment. """
        return ("\n***\n[^Code](https://github.com/matthieugrieger/versebot) ^|"
            " ^/r/VerseBot ^| [^Contact ^Dev](/message/compose/?to=mgrieger) ^|"
            " [^Usage](https://github.com/matthieugrieger/versebot/blob/master/README.md) ^|"
            " [^Changelog](https://github.com/matthieugrieger/versebot/blob/master/CHANGELOG.md) ^|"
            " [^Stats](http://matthieugrieger.com/versebot) ^|"
            " [^Set ^a ^Default ^Translation](http://matthieugrieger.com/versebot#defaults) \n\n"
            "^All ^texts ^provided ^by [^BibleGateway](http://biblegateway.com) ^and [^Bible ^Hub](http://biblehub.com)^. \n\n"
            " ^Mistake? ^%(user)s ^can [^edit](/message/compose/?to=%(bot)s&subject=edit+request&message={%(link)s} "
            "Please+enter+your+revised+verse+quotations+below+in+the+usual+bracketed+syntax.)"
            " ^or [^delete](/message/compose/?to=%(bot)s&subject=delete+request&message={%(link)s} "
            "This+action+cannot+be+reversed!) ^this ^comment."
            % {"user":self.message.author, "bot":REDDIT_USERNAME, "link":self.link})
