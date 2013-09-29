from collections import OrderedDict
from re import findall
import booknames

# Class that holds the properties of a Bible verse. This includes the book, chapter,
# verse (or range of verses), and translation. Also within this class are multiple
# methods used by VerseBot.
class Verse:
    
    _verseData = list()
    _ESV = OrderedDict()
    _NIV = OrderedDict()
    _NRSV = OrderedDict()
    _KJV = OrderedDict()
    _DRA = OrderedDict()
    _Brenton = OrderedDict()
    _invalidComment = False

    # Initializes Verse object with data from the command(s)
    def __init__(self, verseList, comment, translations):
        self._ESV = translations[0]
        self._NIV = translations[1]
        self._NRSV = translations[2]
        self._KJV = translations[3]
        self._DRA = translations[4]
        self._Brenton = translations[5]
        
        for verse in verseList:
            verseBookNum = booknames.getBookNumber(verse.lower())
            if verseBookNum != False:
                verseSubreddit = comment.permalink[24:comment.permalink.find('/', 24)]
                verseBookName = booknames.getBookTitle(verseBookNum)
                verseChapter = self.__getChapterAndVerse(verse.lower())[0]
                verseSelection = self.__getChapterAndVerse(verse.lower())[1]
                verseTranslation = self.__getBibleTranslation(verse.lower(), verseSubreddit, verseBookNum)
                verseContent = self.__getVerseContent(verseBookNum, verseChapter, verseSelection, verseTranslation)

                if verseContent != False:
                    self._verseData.append((verseBookName, verseChapter, verseSelection, verseTranslation, verseContent, verseSubreddit))
        
        if len(self._verseData) == 0:
            self._invalidComment = True

        return

    # Constructs reddit comment.
    def getComment(self):
        if not self._invalidComment:
            comment = ''
            for curVerData in self._verseData:
                # These assignments technically aren't necessary, it just makes the code below a lot easier to
                # understand.
                book = curVerData[0]
                chap = curVerData[1]
                ver = curVerData[2]
                translation = curVerData[3]
                content = curVerData[4]
                subreddit = curVerData[5]
                contextLink = self.__getContextLink(book, chap, translation)

                if ver != '0':
                    comment += ('[**' + book + ' ' + chap + ':' + ver + ' (*' + 
                                translation + '*)**](' + contextLink + ')\n>' + content) + '\n\n'
                else:
                    comment += ('[**' + book + ' ' + chap + ' (*' + translation + '*)**](' + 
                                contextLink + ')\n>' + content) + '\n\n'

            if 0 < len(comment) <= self.__getCharLimit():
                comment += self.__getCommentFooter()
                return comment
            else:
                comment = self.__getOverflowComment()
                comment += self.__getCommentFooter()
                return comment
        else:
            return False

    # Clears contents of _verseData.
    def clearVerses(self):
        self._verseData.clear()
        return

    # Finds chapter number and verse number within current verse request.
    def __getChapterAndVerse(self, verse):
        chap = '0'
        ver = '0'
        if ':' in verse:
            chapterAndVerse = str(findall(r'\d+:\d*(?:-\d+)?', verse))
            chap = (chapterAndVerse.partition(':')[0])[2:]
            ver = (chapterAndVerse.partition(':')[2])[:-2]
        else:
            chap = str(findall(r'\s\d+', verse)).lstrip(' ')
            chap = chap[3:-2]
        
        return chap, ver

    # Determines the correct Bible translation to use for the current verse. It first looks for a user-specified
    # translation. If there is no translation specified, it will then use the default translation for the subreddit
    # in which the comment was posted.
    def __getBibleTranslation(self, commentText, subreddit, book):
        if 67 <= book <= 88: # Uses KJV bible if an Deuterocanon chapter is selected
            if subreddit == 'OrthodoxChristianity':
                return 'Brenton\'s Septuagint'
            else:
                return 'KJV Deuterocanon'
        else:
            if 'niv' in commentText:
                return 'NIV'
            elif 'esv' in commentText:
                return 'ESV'
            elif 'kjv' in commentText:
                return 'KJV'
            elif 'nrsv' in commentText:
                return 'NRSV'
            elif 'dra' in commentText or 'duoay' in commentText or 'rheims' in commentText:
                return 'DRA'
            elif 'brenton' in commentText or 'septuagint' in commentText:
                return 'Brenton\'s Septuagint'
            else: # Uses the default translation for each subreddit
                if subreddit == 'Christianity' or subreddit == 'TrueChristian' or subreddit == 'SOTE':
                    return 'ESV'
                elif subreddit == 'Catholicism':
                    return 'DRA'
                elif subreddit == 'OrthodoxChristianity':
                    if 40 <= bookNum <= 66:
                        return 'ESV'
                    else:
                        return 'Brenton\'s Septuagint'
                else:
                    return 'ESV'
    
    # Retrieves the contents of the selected verse(s) from the pickle files loaded at the beginning of the program.
    # It then constructs the verse contents into part of a comment.
    def __getVerseContent(self, book = False, chap = False, ver = False, translation = False):
        verseText = ''
        currentSelection = ''

        if translation == 'ESV':
            bible = self._ESV
        elif translation == 'NIV':
            bible = self._NIV
        elif translation == 'NRSV':
            bible = self._NRSV
        elif translation == 'KJV' or translation == 'KJV Deuterocanon':
            bible = self._KJV
        elif translation == 'DRA':
            bible = self._DRA
        elif translation == 'Brenton\'s Septuagint':
            bible = self._Brenton

        if book and chap:
            try:
                if ver != '0':
                    if '-' in ver:
                        startingVer = ver.partition('-')[0]
                        endingVer = ver.partition('-')[2]
                        if int(startingVer) < int(endingVer) + 1:
                            for verse in range(int(startingVer), int(endingVer) + 1):
                                verseText += '[**' + str(verse) + '**] ' + (bible[str(book)][int(chap)][verse] + ' ')
                        else:
                            return False
                    else:
                        verseText = '[**' + ver + '**] ' + bible[str(book)][int(chap)][int(ver)]
                else:
                    for verse in bible[str(book)][int(chap)]:
                        verseText += '[**' + str(verse) + '**] ' + (bible[str(book)][int(chap)][verse] + ' ')
                currentSelection += verseText

                return currentSelection
            except KeyError:
                return False
    
    # Simply returns the comment footer found at the bottom of every comment posted by the bot.
    def __getCommentFooter(self):
        return ('\n***\n[[Source Code](https://github.com/matthieugrieger/versebot)]'
               + ' [[Feedback](https://github.com/matthieugrieger/versebot/issues)]' 
               + ' [[Contact Dev](http://www.reddit.com/message/compose/?to=mgrieger)]'
               + ' [[FAQ](https://github.com/matthieugrieger/versebot/blob/master/docs/VerseBot%20Info.md#faq)]' 
               + ' [[Changelog](https://github.com/matthieugrieger/versebot/blob/master/docs/CHANGELOG.md)]')

    # Takes the verse's book name, chapter, and translation as parameters. The function then constructs
    # the appropriate context link. This link appears on each verse title.
    def __getContextLink(self, bookName, chap, translation):
        if translation == 'Brenton\'s Septuagint':
            link = ('http://studybible.info/Brenton/' + bookName + '%20' + chap).replace(' ', '%20')
        elif translation == 'KJV Deuterocanon':
            link = ('http://kingjamesbibleonline.org/' + bookName + '-Chapter-' + chap + '/').replace(' ', '-')
        else:
            link = ('http://www.biblegateway.com/passage/?search=' + bookName + '%20' + chap + '&version=' + translation).replace(' ', '%20')

        return link

    # Constructs and returns an overflow comment whenever the comment exceeds the character limit set by
    # __getCharLimit(). Instead of posting the contents of the verse(s) in the comment, it links to webpages
    # that contain the contents of the verse(s).
    def __getOverflowComment(self):
        comment = 'The contents of the verse(s) you quoted exceed the character limit (4000 characters). Instead, here are links to the verse(s)!\n\n'
        for curVerData in self._verseData:
            book = curVerData[0]
            chap = curVerData[1]
            ver = curVerData[2]
            translation = curVerData[3]

            if translation == 'Brenton\'s Septuagint':
                if ver != '0':
                    overflowLink = ('http://www.studybible.info/Brenton/' + book + '%20' + chap + ':' + ver).replace(' ', '%20')
                    comment += ('- [' + book + ' ' + chap + ':' + ver + ' (' + translation + ')](' + overflowLink + ')\n')
                else:
                    overflowLink = ('http://www.studybible.info/Brenton/' + book + '%20' + chap).replace(' ', '%20')
                    comment += ('- [' + book + ' ' + chap + ' (' + translation + ')](' + overflowLink + ')\n')
            elif translation == 'KJV Deuterocanon':
                 if ver != '0':
                    overflowLink = ('http://www.kingjamesbibleonline.org/' + book + '-' + chap + '-' + ver + '/').replace(' ', '-')
                    comment += ('- [' + book + ' ' + chap + ':' + ver + ' (' + translation + ')](' + overflowLink + ')\n')
                 else:
                    overflowLink = ('http://www.kingjamesbibleonline.org/' + book + '-Chapter-' + chap + '/').replace(' ', '-')
                    comment += ('- [' + book + ' ' + chap + ' (' + translation + ')](' + overflowLink + ')\n')
            else:
                if ver != '0':
                    overflowLink = ('http://www.biblegateway.com/passage/?search=' + book + '%20' + chap + ':' + 
                                    ver + '&version=' + translation).replace(' ', '%20')
                    comment += ('- [' + book + ' ' + chap + ':' + ver + ' (' + translation + ')](' + overflowLink + ')\n')
                else:
                    overflowLink = ('http://www.biblegateway.com/passage/?search=' + book + '%20' + chap + 
                                 '&version=' + translation).replace(' ', '%20')
                    comment += ('- [' + book + ' ' + chap + ' (' + translation + ')](' + overflowLink + ')\n')
        
        return comment
    
    # Just returns the current character limit for the reddit comment. Makes it easy to find/change in the future.
    # NOTE: reddit's character limit is 10,000 characters by default.
    def __getCharLimit(self):
        return 4000



