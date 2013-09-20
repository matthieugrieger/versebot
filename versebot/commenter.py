import praw
from time import ctime
from re import findall
import booknames
from collections import OrderedDict

currentComment = ''
bookNumber = 0

nivbible = OrderedDict()
esvbible = OrderedDict()
kjvbible = OrderedDict()
nrsvbible = OrderedDict()
drabible = OrderedDict()
brentonbible = OrderedDict()

def constructComment(commands, comment, niv, esv, kjv, nrsv, dra, brenton):
    global currentComment, bookNumber, nivbible, esvbible, kjvbible, nrsvbible, drabible, brentonbible

    nivbible = niv
    esvbible = esv
    kjvbible = kjv
    nrsvbible = nrsv
    drabible = dra
    brentonbible = brenton

    subreddit = comment.permalink[24:comment.permalink.find('/', 24)] # Finds subreddit of comment (might be in PRAW, but I don't know how to access it)

    currentComment = ''
    commentFooter = '\n[[Source Code](https://github.com/matthieugrieger/versebot)] [[Feedback](https://github.com/matthieugrieger/versebot/issues)] [[Contact Dev](http://www.reddit.com/message/compose/?to=mgrieger)] [[FAQ](https://github.com/matthieugrieger/versebot/blob/master/docs/VerseBot%20Info.md#faq)] [[Changelog](https://github.com/matthieugrieger/versebot/blob/master/docs/CHANGELOG.md)]'
    for command in commands:
        bookNumber = booknames.getBookNumber(command.lower())
        if bookNumber != False:
            nextCommand = parseCommand(command.lower(), subreddit)
            if nextCommand[0] != False:
                if nextCommand[2] != '0':
                    currentComment += ('**' + booknames.getBookTitle(bookNumber) + ' ' + str(nextCommand[1]) + ':' + str(nextCommand[2]) + ' (*' + 
                                       getBibleTranslation(command.lower(), bookNumber, subreddit)[1] + '*)**\n>' + nextCommand[0]) + '\n\n'
                else:
                    currentComment += ('**' + booknames.getBookTitle(bookNumber) + ' ' + str(nextCommand[1]) + ' (*' + getBibleTranslation(command.lower(), bookNumber, subreddit)[1] +
                                       '*)**\n>' + nextCommand[0]) + '\n\n'
    currentComment += commentFooter
    if currentComment != commentFooter:
        if len(currentComment) <= 3000: # Only posts generated response if it is less than or equal to 3000 characters in length
            comment.reply(currentComment)
            print('Comment posted on ' + ctime() + '.')

        else:
            errorMessage = constructErrorMessage(commands, subreddit)
            errorMessage += commentFooter
            comment.reply(errorMessage)
            print('Comment posted on ' + ctime() + '.')
        
        return True
              
    else:
        return False

def parseCommand(command, subreddit, error = False):
    global currentComment
    currentChapter = '0'
    currentVerse = '0'
    validComment = True

    if ':' in command:
        chapterAndVerse = str(findall(r'\d+:\d*(?:-\d+)?', command))
        currentChapter = (chapterAndVerse.partition(':')[0])[2:]
        currentVerse = (chapterAndVerse.partition(':')[2])[:-2]
    else:
        currentChapter = str(findall(r'\s\d+', command)).lstrip(' ')
        currentChapter = currentChapter[3:-2]
    if not error:    
        bookNumber = booknames.getBookNumber(command.lower())
        if currentVerse != '0' and currentVerse != None:
            try:
                validComment = lookupPassage(bookNumber, currentChapter, currentVerse, getBibleTranslation(command.lower(), bookNumber, subreddit)[0])
            except KeyError:
                validComment = False
        else:
            try:
                validComment = lookupPassage(bookNumber, currentChapter, False, getBibleTranslation(command.lower(), bookNumber, subreddit)[0])
            except KeyError:
                validComment = False
    
    return validComment, currentChapter, currentVerse

def lookupPassage(book = False, chapter = False, verse = False, bible = False):
    verseText = ''
    currentSelection = ''

    if book and chapter:
        if verse:
            if '-' in verse:
                startingVerse = verse.partition('-')[0]
                endingVerse = verse.partition('-')[2]
                if int(startingVerse) < int(endingVerse) + 1:
                    for ver in range(int(startingVerse), int(endingVerse) + 1):
                        verseText += '[**' + str(ver) + '**] ' + (bible[str(book)][int(chapter)][ver] + ' ')
                else:
                    return False
            else:
                verseText = '[**' + verse + '**] ' + bible[str(book)][int(chapter)][int(verse)]
        else:
            for ver in bible[str(book)][int(chapter)]:
                verseText += '[**' + str(ver) + '**] ' + (bible[str(book)][int(chapter)][ver] + ' ')
        currentSelection += verseText
        return currentSelection

def getBibleTranslation(commentText, bookNum, subreddit):
    global nivbible, esvbible, kjvbible, nrsvbible, drabible, brentonbible
    if 67 <= bookNum <= 88: # Uses KJV bible if an Deuterocanon chapter is selected
        if subreddit == 'OrthodoxChristianity':
            return brentonbible, 'Brenton\'s Septuagint'
        else:
            return kjvbible, 'KJV Deuterocanon'
    else:
        if 'niv' in commentText:
            return nivbible, 'NIV'
        elif 'esv' in commentText:
            return esvbible, 'ESV'
        elif 'kjv' in commentText:
            return kjvbible, 'KJV'
        elif 'nrsv' in commentText:
            return nrsvbible, 'NRSV'
        elif 'dra' in commentText or 'duoay' in commentText or 'rheims' in commentText:
            return drabible, 'DRA'
        elif 'brenton' in commentText:
            return brentonbible, 'Brenton\'s Septuagint'
        else: # Uses the default translation for each subreddit
            if subreddit == 'Christianity' or subreddit == 'TrueChristian':
                return esvbible, 'ESV'
            elif subreddit == 'Catholicism':
                return drabible, 'DRA'
            elif subreddit == 'OrthodoxChristianity':
                if 40 <= bookNum <= 66:
                    return esvbible, 'ESV'
                else:
                    return brentonbible, 'Brenton\'s Septuagint'
            else:
                return esvbible, 'ESV'

def constructErrorMessage(commands, subreddit):
    msg = 'It seems that the verses you tried to quote were too long (over 3000 characters). Instead, here are links to the verses!\n\n'
    for command in commands:
        linkVerse = '0'
        bookNum = booknames.getBookNumber(command.lower())
        linkBook = booknames.getBookTitle(bookNum)
        linkCommand = parseCommand(command.lower(), subreddit, True)
        linkChapter = str(linkCommand[1])
        linkVerse = str(linkCommand[2])
        linkTranslation = getBibleTranslation(command.lower(), bookNum, subreddit)[1]
        if linkTranslation == 'Brenton\'s Septuagint': # BibleGateway does not support Brenton's Septuagint
            if linkVerse != '0':
                errorLink = ('http://www.studybible.info/Brenton/' + linkBook + '%20' + linkChapter + ':' + linkVerse).replace(' ', '%20')
                msg += ('- [' + linkBook + ' ' + linkChapter + ':' + linkVerse + ' (' + linkTranslation + ')](' + errorLink + ')\n')
            else:
                errorLink = ('http://www.studybible.info/Brenton/' + linkBook + '%20' + linkChapter).replace(' ', '%20')
                msg += ('- [' + linkBook + ' ' + linkChapter + ' (' + linkTranslation + ')](' + errorLink + ')\n')
        elif 67 <= bookNum <= 88: # Contains a book from the deuterocanon, meaning http://www.kingjamesbibleonline.org/ must be used instead.
            if linkVerse != '0':
                errorLink = ('http://www.kingjamesbibleonline.org/' + linkBook + '-' + linkChapter + '-' + linkVerse + '/').replace(' ', '-')
                msg += ('- [' + linkBook + ' ' + linkChapter + ':' + linkVerse + ' (' + linkTranslation + ')](' + errorLink + ')\n')
            else:
                errorLink = ('http://www.kingjamesbibleonline.org/' + linkBook + '-Chapter-' + linkChapter + '/').replace(' ', '-')
                msg += ('- [' + linkBook + ' ' + linkChapter + ' (' + linkTranslation + ')](' + errorLink + ')\n')
        else: # Use BibleGateway if none of the above stipulations are met
            if linkVerse != '0':
                errorLink = ('http://www.biblegateway.com/passage/?search=' + linkBook + '%20' + linkChapter + ':' + linkVerse + '&version=' + linkTranslation).replace(' ', '%20')
                msg += ('- [' + linkBook + ' ' + linkChapter + ':' + linkVerse + ' (' + linkTranslation + ')](' + errorLink + ')\n')
            else:
                errorLink = ('http://www.biblegateway.com/passage/?search=' + linkBook + '%20' + linkChapter + '&version=' + linkTranslation).replace(' ', '%20')
                msg += ('- [' + linkBook + ' ' + linkChapter + ' (' + linkTranslation + ')](' + errorLink + ')\n')

    return msg