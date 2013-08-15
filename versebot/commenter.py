import praw
from time import ctime

currentComment = ''

def constructComment(commands, comment, bible):
    global currentComment
    currentComment = ''
    for command in commands:
        currentComment += ('**' + command.title() + ' (*KJV*)**\n>')
        parseCommand(command, bible)
        currentComment += ' \n\n'
    currentComment += "\n[[Source Code](https://github.com/matthieugrieger/versebot)] [[Feedback](https://github.com/matthieugrieger/versebot/issues)] [[Contact Dev](http://www.reddit.com/message/compose/?to=mgrieger)]"
    newComment = comment.reply(currentComment).id
    print('Comment posted on ' + ctime() + '.')
    
    return newComment # Returns comment id of reply to keep bot from replying to itself

def parseCommand(command, bible):
    currentChapter = '0'
    currentVerse = '0'
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
                    verseText += '[**' + str(ver) + '**] ' + (bible[book][int(chapter)][ver] + ' ')
            else:
                verseText = '[**' + verse + '**] ' + bible[book][int(chapter)][int(verse)]
        else:
            for ver in bible[book][int(chapter)]:
                verseText += '[**' + str(ver) + '**] ' + (bible[book][int(chapter)][ver] + ' ')
        currentComment += verseText
        return True
    else:
        return False

def find_nth(str, search, n):
    start = str.find(search)
    while start >= 0 and n > 1:
        start = str.find(search, start+len(search))
        n -= 1
    return start
