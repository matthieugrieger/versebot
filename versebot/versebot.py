#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import pickle
import praw
import configloader
import os
from sys import exit
from warnings import filterwarnings
from commenter import constructComment
from time import sleep
from re import findall

filterwarnings("ignore", category=DeprecationWarning) # Ignores DeprecationWarnings caused by PRAW
filterwarnings("ignore", category=ResourceWarning) # Ignores ResourceWarnings when using pickle files. May need to look into this later, but it seems to work fine.

print('Loading Bible translation...')
try:
    file = open(configloader.getBible(), 'rb')
    bible = pickle.load(file)
    print('Bible translation successfully loaded!')
except:
    print('Error while loading Bible translation. Make sure config.ini points to a valid pickle file.')
    exit()

print('Connecting to reddit...')
try:
    r = praw.Reddit(user_agent='VerseBot by /u/mgrieger. Github: https://github.com/matthieugrieger/versebot')
    r.login(configloader.getBotUsername(), configloader.getBotPassword())
    print('Connected!')
except:
    print('Connection to reddit failed. Either reddit is down at the moment, or something in the config is incorrect.')
    exit()

if not os.path.exists('data'): # Makes data folder if it doesn't already exist
    os.makedirs('data')

comment_ids = None
try:
    comment_ids = pickle.load(open(configloader.getCommentIdFile(), 'rb'))
except EOFError:
    comment_ids = set()

while True:
    print('Starting next scan...')
    subreddit = r.get_subreddit(configloader.getSubreddits())
    for submission in subreddit.get_hot(limit = 10):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            if comment.id not in comment_ids:
                versesToFind = findall(r'(?:\d\s)?\w+\s\d+:?\d*-?\d*', comment.body) # Uses regex to find verses in comment body
                if (len(versesToFind) != 0):
                    nextComment = constructComment(versesToFind, comment, bible)
                    comment_ids.add(comment.id)
                    comment_ids.add(nextComment)
                    print('Dumping new comment ids to file...')
                    pickle.dump(comment_ids, open(configloader.getCommentIdFile(), 'wb')) # Dumps new comment ids to file
                
    sleep(30) # Waits 30 seconds between scans by default
