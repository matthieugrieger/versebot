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
from commenter import constructComment
from sys import exit
from warnings import filterwarnings
from time import sleep
from re import findall
from os import environ

filterwarnings("ignore", category=DeprecationWarning) # Ignores DeprecationWarnings caused by PRAW
filterwarnings("ignore", category=ResourceWarning) # Ignores ResourceWarnings when using pickle files. May need to look into this later, but it seems to work fine.

print('Loading Bible translations...')
try:
    nivbible = pickle.load(open(configloader.getNIV(), 'rb'))
    esvbible = pickle.load(open(configloader.getESV(), 'rb'))
    kjvbible = pickle.load(open(configloader.getKJV(), 'rb'))
    nrsvbible = pickle.load(open(configloader.getNRSV(), 'rb'))
    print('Bible translations successfully loaded!')
except:
    print('Error while loading Bible translations. Make sure the environment vars point to correct paths.')
    exit()

def getNIVBible():
    return nivbible

def getESVBible():
    return esvbible

def getKJVBible():
    return kjvbible

def getNRSVBible():
    return nrsvbible

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
lookupList = set()

while True:

    if commentsAdded:
        io = open('tmp.txt', 'w')
        cur.copy_to(io, 'commentids', sep='|')
        io.close()
    # Removed print('Starting next scan...'). Filled up the Heroku logs too much.
    subreddit = r.get_subreddit(configloader.getSubreddits())
    subreddit_comments = subreddit.get_comments()
    for comment in subreddit_comments:
        if comment.id not in open('tmp.txt').read():
            versesToFind = findall(r'\[[\w\s:,-]+]', comment.body) # Uses regex to find verses in comment body
            if (len(versesToFind) != 0):
                for ver in versesToFind:
                    nextVer = findall(r'(?:\d\s)?(?:\w+\s\w+\s\w+)?(?:\w+\s\w+\s\w+\s\w+)?\w+\s\d+:?\d*-?\d*(?:\s\w+)?', ver) # Regex to find valid commands in brackets. Looks really ugly, can probably be made better.
                    lookupList.add(str(nextVer))

                if len(lookupList) != 0:
                    # nextComment = False when only chapter is specified, needs to be fixed
                    nextComment = constructComment(lookupList, comment, nivbible, esvbible, kjvbible, nrsvbible)
                else:
                    nextComment = False

                if nextComment != False:
                    print('Inserting new comment ids to database...')
                    cur.execute("""INSERT INTO commentids VALUES (%s);""", (comment.id,))
                    cur.execute("""INSERT INTO commentids VALUES (%s);""", (nextComment,))
                    conn.commit()
                    commentsAdded = True
                    lookupList.clear()
                else:
                    print('Inserting comment id of comment with invalid command...')
                    cur.execute("""INSERT INTO commentids VALUES (%s);""", (comment.id,)) # Adds comment id with invalid command so it is ignored in the future
                    conn.commit()
                    commentsAdded = True
                    lookupList.clear()
    sleep(30) # Waits 30 seconds between scans by default