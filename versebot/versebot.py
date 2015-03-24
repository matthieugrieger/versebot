"""
VerseBot for reddit
By Matthieu Grieger
versebot.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

import praw
import database
import logging
import books
from config import *
from time import sleep
from webparser import WebParser
from verse import Verse
from regex import find_verses
from response import Response

class VerseBot:
    """ Main VerseBot class. """

    def __init__(self, username, password):
        """ Initializes a VerseBot object with supplied username and password. It is recommended that
        the username and password are stored in something like an environment variable for security
        reasons. """
        logging.basicConfig(level=LOG_LEVEL)
        self.log = logging.getLogger("versebot")
        try:
            self.log.info("Connecting to reddit...")
            self.r = praw.Reddit(user_agent = ("VerseBot by /u/mgrieger. GitHub: https://github.com/matthieugrieger/versebot"))
            self.r.login(username, password)
        except:
            self.log.critical("Connection to reddit failed. Exiting...")
            exit(1)
        self.log.info("Successfully connected to reddit!")
        self.log.info("Connecting to database...")
        database.connect(self.log)  # Initialize connection to database.
        self.log.info("Successfully connected to database!")
        self.parser = WebParser()  # Initialize web parser with updated translation list.
        self.log.info("Updating translation list table...")
        database.update_translation_list(self.parser.translations)
        self.log.info("Translation list update successful!")

    def main_loop(self):
        """ Main inbox searching loop for finding verse quotation requests. """
        self.log.info("Beginning to scan for new inbox messages...")
        while True:
            messages = self.r.get_unread()
            for message in messages:
                if message.subject == "username mention":
                    messages.respond_to_username_mention(message)
                elif message.subject == "Edit Request":
                    messages.respond_to_edit_request(message)
                elif message.subject == "Delete Request":
                    messages.respond_to_delete_request(message)
                message.mark_as_read()
            sleep(30)

    def respond_to_username_mention(self, message):
        """ Responds to a username mention. This could either contain one or more valid
        Bible verse quotation requests, or it could simply be a username mention without
        any valid Bible verses. If there are valid Bible verses, VerseBot generates a
        response that contains the text from these quotations. Otherwise, the message is
        forwarded to the VerseBot admin for review. """

        verses = find_verses(message.body)
        if verses != None:
            response = Response(message, self.parser)
            for verse in verses:
                book_name = books.get_book(verse[0].lower().replace(" ", ""))
                if book_name:
                    response.add_verse(Verse(book_name,  # Book
                        verse[1],  # Chapter
                        verse[3],  # Translation
                        message.author,  # User
                        message.permalink[24:message.permalink.find("/", 24)],  # Subreddit
                        verse[2]))  # Verse
                    self.log.info("Replying to %s with verse quotations..." % message.author)
                    message.reply(response.construct_message(self.parser))
        else:
            self.log.info("No verses found in this message. Forwarding to /u/%s..." % VERSEBOT_ADMIN)
            self.r.send_message(VERSEBOT_ADMIN, "Forwarded VerseBot Message",
                "%s\n\n[[Link to Original Message](%s)]" % (message.body, message.permalink))

    def respond_to_edit_request(self, message):
        """ Responds to an edit request. The bot will parse the body of the message, looking for verse
        quotations. These will replace the quotations that were placed in the original response to the
        user. Once the comment has been successfully edited, the bot then sends a message to the user
        letting them know that their verse quotations have been updated. """

    def respond_to_delete_request(self, message):
        """ Responds to a delete request. The bot will attempt to open the comment which has been requested
        to be deleted. If the submitter of the delete request matches the author of the comment that triggered
        the VerseBot response, the comment will be deleted. The bot will then send a message to the user letting
        them know that their verse quotation comment has been removed. """


bot = VerseBot(REDDIT_USERNAME, REDDIT_PASSWORD)
if __name__ == "__main__":
    bot.main_loop()
