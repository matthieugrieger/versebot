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

def main():
    """ Main program. Continually checks message inbox for new comments to handle."""
    try:
        r = praw.Reddit(user_agent = ("VerseBot by /u/mgrieger. GitHub: https://github.com/matthieugrieger/versebot"))
        r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
    except:
        exit()
        
    database.connect()
    # Find supported translations here!
    while True:
        messages = r.get_unread()
        for message in messages:
            if message.subject == "username mention":
                verses = regex.find_verses(message.body)
                if verses != None:
                    response = Response(message)
                    for verse in verses:
                        response.add_verse(Verse(verse[0], verse[1], verse[2], verse[3]))
                    message.reply(response.construct_message())
                else:
                    r.send_message(message.author, NO_VERSE_FOUND_SUBJECT, NO_VERSE_FOUND_MSG)
            elif message.subject == "Edit Request":
                pass
            elif message.subject == "Delete Request":
                pass
            message.mark_as_read()
        sleep(30)

if __name__ == "__main__":
    main()
