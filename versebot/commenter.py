import praw
import time
from sys import exit

currentComment = ''

def constructComment(commands, comment, bible):
    global currentComment
    currentComment = ''
    for command in commands:
        currentComment += ('**' + command + ' (*KJV*)**\n>')
        parseCommand(command, bible)
        currentComment += ' \n\n'
    newComment = comment.reply(currentComment).id
    print('\tComment posted on ' + time.ctime() + '.')
    
    return newComment # Returns comment id of reply to keep bot from replying to itself

def parseCommand(command, bible):
    currentChapter = '0'
    currentVerse = '0'
    currentBook = command[0 : command.find(' ')]
    if ':' in command:
        currentChapter = command[command.find(' ') : command.find(':')]
        currentVerse = command[command.find(':') + 1 : ]
    else:
        currentChapter = command[command.find(' ') :]

    if currentVerse != '0':
        lookupPassage(currentBook, currentChapter, currentVerse, bible)
    else:
        lookupPassage(currentBook, currentChapter, False, bible)

def lookupPassage(book = False, chapter = False, verse = False, bible = False):
    verseText = ''
    global currentComment

    if book and chapter:
        if verse:
            if '-' in verse:
                startingVerse = verse.partition('-')[0]
                endingVerse = verse.partition('-')[2]
                for ver in range(int(startingVerse), int(endingVerse) + 1):
                    verseText += '[*' + str(ver) + '*] ' + (bible[book][int(chapter)][ver] + ' ')
            else:
                verseText = '[*' + verse + '*] ' + bible[book][int(chapter)][int(verse)]
        else:
            for ver in bible[book][int(chapter)]:
                verseText += '[*' + str(ver) + '*] ' + (bible[book][int(chapter)][ver] + ' ')
        currentComment += verseText
        return True
    else:
        return False
