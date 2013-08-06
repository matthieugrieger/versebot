#---------------------#
# VerseBot for Reddit #
# By Matthieu Grieger #
#---------------------#

import pickle
import praw
import time

file = open('kjv.pk1', 'rb')
bible = pickle.load(file)

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
            print('Comment posted on ' + time.ctime() + '.')
            already_done.add(comment.id)
        else:
            print('No comment was provided.')
    else:
        return False

r = praw.Reddit(user_agent='VerseBot by /u/mgrieger')
r.login('bot-username', 'bot-password')

already_done = set()

while True:
    subreddit = r.get_subreddit('desired-subreddit')
    for submission in subreddit.get_hot(limit = 10):
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
