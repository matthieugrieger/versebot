import praw
import time
from sys import exit

currentComment = '>'

def constructComment(commands, comment, bible):
    global currentComment
    currentComment = '>'
    for command in commands:
        parseCommand(command, bible)
        comment.reply(currentComment)
        print('\tComment posted on ' + time.ctime() + '.')

def parseCommand(command, bible):
    currentChapter = 0
    currentVerse = 0
    currentBook = command[0 : command.find(' ')]
    if ':' in command:
        currentChapter = int(command[command.find(' ') : command.find(':')])
        currentVerse = int(command[command.find(':') + 1 : ])
    else:
        currentChapter = int(command[command.find(' ') :])

    if currentVerse != 0:
        lookupPassage(currentBook, currentChapter, currentVerse, bible)
    else:
        lookupPassage(currentBook, currentChapter, False, bible)

def lookupPassage(book = False, chapter = False, verse = False, bible = False):
    verseText = ''
    global currentComment

    if book and chapter:
        if verse:
            verseText = '^' + str(verse) + ' ' + bible[book][chapter][verse]
        else:
            for ver in bible[book][chapter]:
                verseText += '^' + str(ver) + ' ' + (bible[book][chapter][ver] + ' ')
        currentComment += verseText
        return True
    else:
        return False
