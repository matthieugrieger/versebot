#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import pickle
import praw
import configloader
import commenter
import time
import warnings
from sys import exit
import re

configloader.startup()
warnings.filterwarnings("ignore", category=DeprecationWarning) # Ignores DeprecationWarnings caused by PRAW

print('Loading Bible translation...')
try:
    file = open(configloader.getPickle(), 'rb')
    bible = pickle.load(file)
    print('Bible translation successfully loaded!')
except:
    print('Error while loading Bible translation. Make sure config.ini points to a valid .pk1 file.')
    sys.exit()

print('Connecting to reddit...')
try:
    r = praw.Reddit(user_agent='VerseBot by /u/mgrieger. Github: https://github.com/matthieugrieger/versebot')
    r.login(configloader.getBotUsername(), configloader.getBotPassword())
    print('Connected!')
except:
    print('Connection to reddit failed. Either reddit is down at the moment, or something in the config is incorrect.')

already_done = set()

while True:
    print('Starting next scan...')
    subreddit = r.get_subreddit(configloader.getSubreddits())
    for submission in subreddit.get_hot(limit = int(configloader.getScanLimit())):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            if comment.id not in already_done:
                versesToFind = re.findall(r'(?:\d\s)?\w+\s\d+:?\d*-?\d*', comment.body) # I love regex.
                if (len(versesToFind) != 0):
                    nextComment = commenter.constructComment(versesToFind, comment, bible)
                    already_done.add(comment.id)
                    already_done.add(nextComment)
                
    time.sleep(int(configloader.getScanDelay())) # Waits 60 seconds between scans by default
