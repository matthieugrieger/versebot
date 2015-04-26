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
import requests
from config import *
from time import sleep
from webparser import WebParser
from verse import Verse
from regex import find_verses, find_default_translations, find_subreddit_in_request
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
        self.log.info("Cleaning old user translation entries...")
        database.clean_user_translations()
        self.log.info("User translation cleaning successful!")

    def main_loop(self):
        """ Main inbox searching loop for finding verse quotation requests. """
        self.log.info("Beginning to scan for new inbox messages...")
        while True:
            messages = self.r.get_unread()
            for message in messages:
                if message.subject == "username mention":
                    self.respond_to_username_mention(message)
                elif message.subject == "edit request":
                    self.respond_to_edit_request(message)
                elif message.subject == "delete request":
                    self.respond_to_delete_request(message)
                elif message.subject == "user translation default request":
                    self.respond_to_user_translation_request(message)
                elif message.subject == "subreddit translation default request":
                    self.respond_to_subreddit_translation_request(message)
                message.mark_as_read()
            sleep(30)

    def respond_to_username_mention(self, message):
        """ Responds to a username mention. This could either contain one or more valid
        Bible verse quotation requests, or it could simply be a username mention without
        any valid Bible verses. If there are valid Bible verses, VerseBot generates a
        response that contains the text from these quotations. Otherwise, the message is
        forwarded to the VerseBot admin for review. """

        verses = find_verses(message.body)
        if verses is not None:
            response = Response(message, self.parser)
            for verse in verses:
                book_name = books.get_book(verse[0])
                if book_name is not None:
                    v = Verse(book_name,  # Book
                        verse[1],  # Chapter
                        verse[3],  # Translation
                        message.author,  # User
                        message.permalink[24:message.permalink.find("/", 24)],  # Subreddit
                        verse[2])  # Verse
                    if not response.is_duplicate_verse(v):
                        response.add_verse(v)
            if len(response.verse_list) != 0:
                message_response = response.construct_message()
                if message_response is not None:
                    self.log.info("Replying to %s with verse quotations..." % message.author)
                    try:
                        message.reply(message_response)
                        database.update_db_stats(response.verse_list)
                    except requests.exceptions.HTTPError as err:
                        # The bot is banned. :(
                        if str(err) == "403 Client Error: Forbidden":
                            self.log.warning("Banned from subreddit. Skipping message.")
                    except praw.errors.APIException as err:
                        if err.error_type in ("TOO_OLD", "DELETED_LINK", "DELETED_COMMENT"):
                            self.log.warning("An error occurred while replying with error_type %s." % err.error_type)
        else:
            self.log.info("No verses found in this message. Forwarding to /u/%s..." % VERSEBOT_ADMIN)
            self.r.send_message(VERSEBOT_ADMIN, "Forwarded VerseBot Message",
                "%s\n\n[[Link to Original Message](%s)]" % (message.body, message.permalink))

    def respond_to_edit_request(self, message):
        """ Responds to an edit request. The bot will parse the body of the message, looking for verse
        quotations. These will replace the quotations that were placed in the original response to the
        user. Once the comment has been successfully edited, the bot then sends a message to the user
        letting them know that their verse quotations have been updated. """

        try:
            comment_url = message.body[1:message.body.find("}")]
            comment = self.r.get_submission(comment_url)
        except:
            message.reply("An error occurred while processing your edit request. "
                "Please make sure that you do not modify the subject line of your message to %s."
                % REDDIT_USERNAME)
            return

        if message.author == comment.author and comment:
            verses = find_verses(message.body)
            if verses is not None:
                for reply in comment.comments[0].replies:
                    if str(reply.author) == REDDIT_USERNAME:
                        try:
                            self.log.info("%s has requested a comment edit..." % comment.author)
                            link = reply.permalink[24:comment.permalink.find("/", 24)]
                            response = Response(message, self.parser, comment_url)
                            for verse in verses:
                                book_name = books.get_book(verse[0])
                                if book_name is not None:
                                    v = Verse(book_name,  # Book
                                        verse[1],  # Chapter
                                        verse[3],  # Translation
                                        message.author,  # User
                                        link,  # Subreddit
                                        verse[2])  # Verse
                                    if not response.is_duplicate_verse(v):
                                        response.add_verse(v)
                            if len(response.verse_list) != 0:
                                message_response = ("*^This ^comment ^has ^been ^edited ^by ^%s.*\n\n" % message.author)
                                message_response += response.construct_message()
                                if message_response is not None:
                                    self.log.info("Editing %s's comment with updated verse quotations..." % message.author)
                                    database.remove_invalid_statistics(reply.body, link)
                                    reply.edit(message_response)
                                    database.update_db_stats(response.verse_list)
                                    message.mark_as_read()
                                    message.reply("[Your triggered %s response](%s) has been successfully edited to reflect"
                                        " your updated quotations." % (REDDIT_USERNAME, comment_url))
                                    break
                        except:
                            raise
                            self.log.warning("Comment edit failed. Will try again later...")
                            break
            else:
                message.mark_as_read()
        else:
            message.mark_as_read()

    def respond_to_delete_request(self, message):
        """ Responds to a delete request. The bot will attempt to open the comment which has been requested
        to be deleted. If the submitter of the delete request matches the author of the comment that triggered
        the VerseBot response, the comment will be deleted. The bot will then send a message to the user letting
        them know that their verse quotation comment has been removed. """

        try:
            comment_url = message.body[1:message.body.find("}")]
            comment = self.r.get_submission(comment_url)
        except:
            message.reply("An error occurred while processing your deletion request. "
                "Please make sure that you do not modify the subject line of your message to %s."
                % REDDIT_USERNAME)
            return

        if message.author == comment.author and comment:
            for reply in comment.comments[0].replies:
                if str(reply.author) == REDDIT_USERNAME:
                    try:
                        self.log.info("%s has requested a comment deletion..." % comment.author)
                        link = reply.permalink[24:comment.permalink.find("/", 24)]
                        database.remove_invalid_statistics(reply.body, link)
                        reply.delete()
                        message.mark_as_read()
                        message.reply("%s's response to [your comment](%s) has been deleted. "
                            "Sorry for any inconvenience!" % (REDDIT_USERNAME, comment_url))
                        break
                    except:
                        self.log.warning("Comment deletion failed. Will try again later...")
        else:
            message.mark_as_read()

    def respond_to_user_translation_request(self, message):
        """ Responds to a user's default translation request. The bot will parse the message which contains the
        desired translations, and will check them against the database to make sure they are valid. If they are
        valid, the bot will respond with a confirmation message and add the defaults to the user_translations table.
        If not valid, the bot will respond with an error message. """

        ot_trans, nt_trans, deut_trans = find_default_translations(message.body)
        if ot_trans is not None:
            if (database.is_valid_translation(ot_trans, "Old Testament")
                and database.is_valid_translation(nt_trans, "New Testament")
                and database.is_valid_translation(deut_trans, "Deuterocanon")):
                database.update_user_translation(str(message.author), ot_trans, nt_trans, deut_trans)
                message.reply("Your default translations have been updated successfully!")
            else:
                message.reply("One or more of your translation choices is invalid. Please review your choices"
                    " and try again.")
        else:
            message.reply("Your default translation request does not match the required format. Please do not edit"
                " the message after generating it from the website.")
        message.mark_as_read()


    def respond_to_subreddit_translation_request(self, message):
        """ Responds to a subreddit's default translation request. The bot will parse the message which contains the
        desired translations, and will check them against the database to make sure they are valid. If they are
        valid, the bot will respond with a confirmation message and add the defaults to the subreddit_translations table.
        If not valid, the bot will respond with an error message. """

        subreddit = find_subreddit_in_request(message.body)
        if message.author in self.r.get_moderators(subreddit):
            ot_trans, nt_trans, deut_trans = find_default_translations(message.body)
            if ot_trans is not None:
                if (database.is_valid_translation(ot_trans, "Old Testament")
                    and database.is_valid_translation(nt_trans, "New Testament")
                    and database.is_valid_translation(deut_trans, "Deuterocanon")):
                    database.update_subreddit_translation(subreddit, ot_trans, nt_trans, deut_trans)
                    self.r.send_message("/r/" + subreddit, "/r/%s Default Translation Change Confirmation" % subreddit,
                        "The default /u/%s translation for this subreddit has been changed by /u/%s to the following:\n\n"
                        "Old Testament: %s\nNew Testament: %s\nDeuterocanon: %s\n\nIf this is a mistake,"
                        " please [click here](http://matthieugrieger.com/versebot#subreddit-translation-default)"
                        " to submit a new request." % (subreddit, REDDIT_USERNAME, str(message.author), ot_trans, nt_trans,
                            deut_trans))
                else:
                    message.reply("One or more of your translation choices is invalid. Please review your choices"
                    " and try again.")
            else:
                message.reply("YOur default translation request does not match the required format. Please do not edit"
                " the message after generating it from the website.")
        message.mark_as_read()


bot = VerseBot(REDDIT_USERNAME, REDDIT_PASSWORD)
if __name__ == "__main__":
    bot.main_loop()
