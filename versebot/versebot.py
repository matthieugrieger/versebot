#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

import pickle
import configloader
import praw
import psycopg2
import urllib.parse
from verse import Verse
from sys import exit
from re import findall
from time import sleep
from os import environ
from warnings import filterwarnings

# Ignores ResourceWarnings when using pickle files. May need to look into this later, but it seems to work fine.
filterwarnings("ignore", category=ResourceWarning)
# Ignores DeprecationWarnings caused by PRAW
filterwarnings("ignore", category=DeprecationWarning) 

print('Starting up VerseBot...')

# Loads Bible translation pickle files into memory.
print('Loading Bible translations...')
try:
    esvbible = pickle.load(open(configloader.getESV(), 'rb'))
    nivbible = pickle.load(open(configloader.getNIV(), 'rb'))
    nrsvbible = pickle.load(open(configloader.getNRSV(), 'rb'))
    kjvbible = pickle.load(open(configloader.getKJV(), 'rb'))
    drabible = pickle.load(open(configloader.getDRA(), 'rb'))
    brentonbible = pickle.load(open(configloader.getBrenton(), 'rb'))
    bibles = (esvbible, nivbible, nrsvbible, kjvbible, drabible, brentonbible)
    print('Bible translations successfully loaded!')
except:
    print('Error while loading Bible translations. Make sure the environment vars point to correct paths.')
    exit()

# Connects to reddit via PRAW.
print('Connecting to reddit...')
try:
    r = praw.Reddit(user_agent='VerseBot by /u/mgrieger. Github: https://github.com/matthieugrieger/versebot')
    r.login(configloader.getBotUsername(), configloader.getBotPassword())
    print('Connected to reddit!')
except:
    print('Connection to reddit failed. Either reddit is down at the moment, or something in the config is incorrect.')
    exit()

# Connects to a PostgreSQL database used to store comment ids.
print('Connecting to database...')
urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(environ['HEROKU_POSTGRESQL_ONYX_URL'])
try:
    conn = psycopg2.connect(
    database = url.path[1:],
    user = url.username,
    password = url.password,
    host = url.hostname,
    port = url.port)
    
    cur = conn.cursor()
    print('Connected to database!')
except:
    print('Connection to database failed.')
    exit()

# Fills text file previous comment ids from PostgreSQL database.
print('Setting up tmp.txt...')
try:
    io = open('tmp.txt', 'w')
    cur.copy_to(io, 'commentids', sep='|')
    io.close()
    print('tmp.txt ready!')
except:
    print('Error when setting up tmp.txt.')
    exit()

commentsAdded = False
lookupList = list()
comment_ids_this_session = set() # This is to help protect against spamming when connection to database is lost.

print('Beginning to scan comments...')
# This loop runs every 30 seconds.
while True:
    if commentsAdded:
        # Copies new comment ids from database into txt file for searching.
        io = open('tmp.txt', 'w')
        cur.copy_to(io, 'commentids', sep='|')
        io.close()
    subreddit = r.get_subreddit(configloader.getSubreddits())
    subreddit_comments = subreddit.get_comments()

    for comment in subreddit_comments:
        if comment.author != configloader.getBotUsername() and comment.id not in open('tmp.txt').read() and comment.id not in comment_ids_this_session:
            comment_ids_this_session.add(comment.id)
            versesToFind = findall(r'\[[\w\s:,-]+](?!\()', comment.body) # Uses regex to find potential verses in comment body.
            if len(versesToFind) != 0:
                for ver in versesToFind:
                    # This regex is ugly, I will look into making it prettier later.
                    nextVer = findall(r'(?:\d\w*\s)?(?:\w+\s\w+\s\w+)?(?:\w+\s\w+\s\w+\s\w+)?\w+\s\d+:?\d*-?\d*(?:\s\w+)?', ver)
                    lookupList.append(str(nextVer))

                if len(lookupList) != 0:
                    verseObject = Verse(lookupList, comment, bibles)
                    nextComment = verseObject.getComment()
                    if nextComment != False:
                        comment.reply(nextComment)
                    verseObject.clearVerses()
                else:
                    nextComment = False

                if nextComment != False:
                    print('Inserting new comment id to database...')
                    try:
                        cur.execute("""INSERT INTO commentids VALUES (%s);""", (comment.id,))
                        conn.commit()
                    except:
                        print('Database insert failed.')
                        exit()
                    commentsAdded = True
                    lookupList.clear()
                else:
                    commentsAdded = False
                    try:    
                        # Removes comment id from set if the comment was not replied to. This should prevent situations where the comment
                        # has a valid command and the bot does not reply because the reply operation failed the first time through.
                        comment_ids_this_session.remove(comment.id)
                    except KeyError:
                        pass
                    lookupList.clear()
    
    sleep(30)