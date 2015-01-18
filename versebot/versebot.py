"""
VerseBot for reddit
By Matthieu Grieger
versebot.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

import praw
from config import *

def main():
    """ Main program. Continually checks message inbox for new comments to handle."""
    try:
        r = praw.Reddit(user_agent = ("VerseBot by /u/mgrieger. GitHub: https://github.com/matthieugrieger/versebot"))
        r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
    except:
        exit()

if __name__ == "__main__":
    main()
