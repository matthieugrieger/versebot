"""
VerseBot for reddit
By Matthieu Grieger
config.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from os import environ
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

REDDIT_USERNAME = environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = environ["REDDIT_PASSWORD"]
HEROKU_DB = environ["DATABASE_URL"]
VERSEBOT_ADMIN = environ["VERSEBOT_ADMIN"]
LOG_LEVEL = INFO
