"""
VerseBot for reddit
By Matthieu Grieger
versebot.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

import praw
import database
import regex
from config import *
from strings import *
from time import sleep
from response import Response
from verse import Verse
from webparser import WebParser

class VerseBot:
    """ Main VerseBot class. """
    
    def __init__(self, username, password):
        """ Initializes a VerseBot object with supplied username and password. It is recommended that
        the username and password are stored in something like an environment variable for security
        reasons. """
        try:
            self.r = praw.Reddit(user_agent = ("VerseBot by /u/mgrieger. GitHub: https://github.com/matthieugrieger/versebot"))
            self.r.login(username, password)
        except:
            exit(1)
        database.connect()  # Initialize connection to database.
        self.parser = WebParser()  # Initialize web parser with updated translation list.
    
    def main_loop(self):
        """ Main inbox searching loop for finding verse quotation requests. """
        while True:
            messages = self.r.get_unread()
            for message in messages:
                if message.subject == "username mention":
                    verses = regex.find_verses(message.body)
                    if verses != None:
                        response = Response(message)
                        for verse in verses:
                            response.add_verse(Verse(verse[0], verse[1], verse[2], verse[3]))
                        message.reply(response.construct_message())
                    else:
                        self.r.send_message(VERSEBOT_ADMIN, "Forwarded VerseBot Message", 
							"%s\n\n[[Link to Original Message](%s)]" % (message.body, message.permalink))
                elif message.subject == "Edit Request":
                    pass
                elif message.subject == "Delete Request":
                    pass
                message.mark_as_read()
            sleep(30)
            

bot = VerseBot(REDDIT_USERNAME, REDDIT_PASSWORD)
if __name__ == "__main__":
    bot.main_loop()
