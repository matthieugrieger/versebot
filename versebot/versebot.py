#---------------------#
# VerseBot for Reddit #
# By Matthieu Grieger #
#---------------------#

import pickle
import praw
import time
import configloader

configloader.startup()

print('Loading Bible translation...')
file = open(configloader.getPickle(), 'rb')
bible = pickle.load(file)
print('Bible translation successfully loaded!')

def verseReply(book = False, chapter = False, verse = False, com = False):
    verseText = ""
    if book and chapter:
        if verse:
            verseText = bible[book][chapter][verse]
        else:
            for ver in bible[book][chapter]:
                verseText += (bible[book][chapter][ver] + " ")
        if com != False:
            com.reply('**' + book + ' ' + str(chapter) + ':' + str(verse) + '**'
                      + '\n>' + verseText)
            print('\tComment posted on ' + time.ctime() + '.')
            already_done.add(comment.id)
        else:
            print('\tNo comment was provided.')
    else:
        return False

r = praw.Reddit(user_agent='VerseBot by /u/mgrieger')
r.login(configloader.getBotUsername(), configloader.getBotPassword())

already_done = set()

while True:
    print('Starting next scan...')
    subreddit = r.get_subreddit(configloader.getSubreddits())
    for submission in subreddit.get_hot(limit = int(configloader.getScanLimit())):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            if 'VerseBot:' in comment.body:
                if comment.id not in already_done:
                    bookBegin = comment.body.find('VerseBot: ') + 10
                    bookEnd = comment.body.find(' ', bookBegin)
                    desiredBook = comment.body[bookBegin : bookEnd]
                    chapterEnd = comment.body.find(':', bookEnd + 1)
                    desiredChapter = int(comment.body[(bookEnd + 1) : chapterEnd])
                    desiredVerse = None
                    if comment.body[chapterEnd + 1] == '.':
                        desiredVerse = False
                    else:
                        desiredVerse = int(comment.body[chapterEnd + 1 : comment.body.find('.', chapterEnd + 1)])
                    verseReply(book = desiredBook, chapter = desiredChapter, verse = desiredVerse, com = comment)
    time.sleep(10)
