import praw
from time import ctime

currentComment = ''

def constructComment(commands, comment, bible, translation):
    global currentComment
    currentComment = ''
    commentFooter = '\n[[Source Code](https://github.com/matthieugrieger/versebot)] [[Feedback](https://github.com/matthieugrieger/versebot/issues)] [[Contact Dev](http://www.reddit.com/message/compose/?to=mgrieger)]'
    for command in commands:
        nextCommand = parseCommand(command, bible)
        if nextCommand != False:
            currentComment += ('**' + command.title() + ' (*' + translation + '*)**\n>' + nextCommand)
            currentComment += ' \n\n'
    currentComment += commentFooter
    if currentComment != commentFooter:
        newComment = comment.reply(currentComment).id
        print('Comment posted on ' + ctime() + '.')
        return newComment # Returns comment id of reply to keep bot from replying to itself
    else:
        return False

def parseCommand(command, bible):
    global currentComment
    currentChapter = '0'
    currentVerse = '0'
    validComment = True

    if command[0].isdigit():
        currentBook = command[0 : find_nth(command, ' ', 2)].title()
    else:
        currentBook = command[0 : command.find(' ')].title()
    if ':' in command:
        if command[0].isdigit():
            currentChapter = command[find_nth(command, ' ', 2) : command.find(':')]
        else:
            currentChapter = command[command.find(' ') : command.find(':')]
        currentVerse = command[command.find(':') + 1 :]
    else:
        currentChapter = command[command.find(' ') :]
    if currentVerse != '0':
        try:
            validComment = lookupPassage(currentBook, currentChapter, currentVerse, bible)
        except KeyError:
            validComment = False
    else:
        try:
            validComment = lookupPassage(currentBook, currentChapter, False, bible)
        except KeyError:
            validComment = False
    
    return validComment

def lookupPassage(book = False, chapter = False, verse = False, bible = False):
    verseText = ''
    currentSelection = ''

    if book and chapter:
        if verse:
            if '-' in verse:
                startingVerse = verse.partition('-')[0]
                endingVerse = verse.partition('-')[2]
                for ver in range(int(startingVerse), int(endingVerse) + 1):
                    verseText += '[**' + str(ver) + '**] ' + (bible[book][int(chapter)][ver] + ' ')
            else:
                verseText = '[**' + verse + '**] ' + bible[book][int(chapter)][int(verse)]
        else:
            for ver in bible[book][int(chapter)]:
                verseText += '[**' + str(ver) + '**] ' + (bible[book][int(chapter)][ver] + ' ')
        currentSelection += verseText
        return currentSelection

def find_nth(str, search, n):
    start = str.find(search)
    while start >= 0 and n > 1:
        start = str.find(search, start+len(search))
        n -= 1
    return start
