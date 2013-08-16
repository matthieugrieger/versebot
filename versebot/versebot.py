#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import pickle
import praw
import configloader
import os
import psycopg2
import urllib.parse
from sys import exit
from warnings import filterwarnings
from commenter import constructComment
from time import sleep
from re import findall
from os import environ

filterwarnings("ignore", category=DeprecationWarning) # Ignores DeprecationWarnings caused by PRAW
filterwarnings("ignore", category=ResourceWarning) # Ignores ResourceWarnings when using pickle files. May need to look into this later, but it seems to work fine.

print('Loading Bible translations...')
try:
    nivfile = open(configloader.getNIV(), 'rb')
    nivbible = pickle.load(nivfile)
    esvfile = open(configloader.getESV(), 'rb')
    esvbible = pickle.load(esvfile)
    kjvfile = open(configloader.getKJV(), 'rb')
    kjvbible = pickle.load(kjvfile)
    nrsvfile = open(configloader.getNRSV(), 'rb')
    nrsvbible = pickle.load(nrsvfile)
    print('Bible translations successfully loaded!')
except:
    print('Error while loading Bible translations. Make sure the environment vars point to correct paths.')
    exit()

print('Connecting to reddit...')
try:
    r = praw.Reddit(user_agent='VerseBot by /u/mgrieger. Github: https://github.com/matthieugrieger/versebot')
    r.login(configloader.getBotUsername(), configloader.getBotPassword())
    print('Connected!')
except:
    print('Connection to reddit failed. Either reddit is down at the moment, or something in the config is incorrect.')
    exit()

print('Connecting to database...')
urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(environ['HEROKU_POSTGRESQL_ONYX_URL'])
conn = psycopg2.connect(
    database = url.path[1:],
    user = url.username,
    password = url.password,
    host = url.hostname,
    port = url.port
)
cur = conn.cursor()

io = open('tmp.txt', 'w')
cur.copy_to(io, 'commentids', sep='|')
io.close()
commentsAdded = False

def findTranslation(commentText):
    if 'niv' in commentText:
        return nivbible, 'NIV'
    elif 'esv' in commentText:
        return esvbible, 'ESV'
    elif 'kjv' in commentText:
        return kjvbible, 'KJV'
    elif 'nrsv' in commentText:
        return nrsvbible, 'NRSV'
    else:
        return esvbible, 'ESV'

while True:
    if commentsAdded:
        io = open('tmp.txt', 'w')
        cur.copy_to(io, 'commentids', sep='|')
        io.close()
    print('Starting next scan...')
    subreddit = r.get_subreddit(configloader.getSubreddits())
    for submission in subreddit.get_hot(limit = 10):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            if comment.id not in open('tmp.txt').read() and 'vb' in comment.body.lower():
                versesToFind = findall(r'(?:\d\s)?\w+\s\d+:?\d*-?\d*', comment.body) # Uses regex to find verses in comment body
                if (len(versesToFind) != 0):
                    bible = findTranslation(comment.body.lower())[0]
                    translation = findTranslation(comment.body.lower())[1]
                    nextComment = constructComment(versesToFind, comment, bible, translation)
                    if nextComment != False:
                        print('Inserting new comment ids to database...')
                        cur.execute("""INSERT INTO commentids VALUES (%s);""", (comment.id,))
                        cur.execute("""INSERT INTO commentids VALUES (%s);""", (nextComment,))
                        conn.commit()
                        commentsAdded = True
                    else:
                        print('Inserting comment id of comment with invalid command...')
                        cur.execute("""INSERT INTO commentids VALUES (%s);""", (comment.id,)) # Adds comment id with invalid command so it is ignored in the future
                        conn.commit()
                        commentsAdded = True
    sleep(30) # Waits 30 seconds between scans by default