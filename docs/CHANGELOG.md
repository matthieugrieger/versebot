# VerseBot Changelog

### May 9, 2014
* Fixed the bot mistaking books such as '1 John' as just 'John'.

### May 8, 2014
* HUGE update!
* Completely refactored codebase.
* VerseBot now uses [BibleGateway](http://www.biblegateway.com) as its source for Bible texts. Because of this, VerseBot now supports over 100 translations in 62 languages!
* Bot automatically recognizes new translations on BibleGateway every 24 hours or so (whenever the bot is restarted automatically).
* Added helpers.py to handle all BibleGateway functions (and possibly more in the future).
* Changed method of retrieving new comments. Now uses PRAW's comment stream.
* Bot now scans ALL subreddits (will be monitored for reliability).
* Updated comment ids table to hold timestamp of reply.
* Now automatically deletes all comment ids in the database 2 days old or older on startup.
* Added book stats table.
* Added translation stats table.
* Added subreddit stats table.
* Updated createdatabase.sql to reflect database changes.
* Moved all database actions to database.py.
* Rewritten for transition to Python 2.7.6 for better library support.
* Changed runtime.txt to Python 2.7.6.
* Updated PRAW and psycopg2, added BeautifulSoupv4.
* Added tests/tests.py to implement unit tests.
* Removed Bible pickle files (no longer needed).
* Renamed configloader.py to config.py.
* Cleaned up config in config.py, removed all references to pickle file locations.
* Renamed booknames.py to data.py.
* Changed bookNames datatype in data.py from OrderedDict to Dict. OrderedDict was not needed anymore.
* Got rid of temp.txt. Not needed anymore.
* Appropriately renders titles in verse contents, much like BibleGateway.
* Now retrieves verse and translation titles from BibleGateway for more detail.
* Added docs/Supported Translations.md.

### March 28, 2014
* VerseBot released on [/r/christiansupport](http://www.reddit.com/r/christiansupport).

### March 21, 2014
* Added New Living Translation (NLT).

### March 9, 2014
* VerseBot released on [/r/ReformedBaptist](http://www.reddit.com/r/ReformedBaptist).

### January 9, 2014
* VerseBot released on [/r/NTChristian](http://www.reddit.com/r/NTChristian).
* VerseBot released on [/r/HolyBible](http://www.reddit.com/r/HolyBible).
* Removed some redundant code.

### January 8, 2014
* VerseBot released on [/r/Protestantism](http://www.reddit.com/r/Protestantism).
* VerseBot released on [/r/divineoffice](http://www.reddit.com/r/divineoffice).

### December 25, 2013
* Removed Nova Vulgata footer announcement.
* Merry Christmas!

### December 22, 2013
* Nova Vulgata (A Latin translation) added to VerseBot.
* Removed some redundant code.
* Added a small update notice on the comment footer. Will probably be changed later for easier updating in the future.

### December 20, 2013
* VerseBot released on [/r/DebateAChristian](http://www.reddit.com/r/DebateAChristian).

### November 29, 2013
* Fixed an incorrect verse in the ESV translation.

### November 15, 2013
* VerseBot released on [/r/Reformed](http://www.reddit.com/r/Reformed).

### October 28, 2013
* Added Hebrew names for some of the Old Testament books.

### October 24, 2013
* Added JPS Tanakh translation.
* Released bot on [/r/Judaism](http://www.reddit.com/r/Judaism).

### September 27, 2013
* Complete rewrite of VerseBot code. Should be much easier to update/understand now.
* Code is more thoroughly commented.
* VerseBot no longer replies to comments with verse text from a different book of the Bible. Example: interpreting [1 Timohty 1:1] as Titus 1:1 (misspelled on purpose).
* Horizontal rule added to bottom of comment before comment footer.
* Fixed slight formatting error.
* Added 'Mathew' (Matthew) to list of accepted bible names.

### September 26, 2013
* Verse titles now link to full chapter for context.
* Added 1st Timothy and 2nd Timothy to list of Bible abbreviations.
* Made a slight change to regex to allow for the change above.

### September 22, 2013
* VerseBot released on [/r/SOTE](http://www.reddit.com/r/SOTE).
* Set following translation default: SOTE = ESV.

### September 19, 2013
* Added Brenton's Septuagint.
* Set following translation default: OrthodoxChristianity = Brenton's Septuagint.

### September 17, 2013
* Added Douay-Rheims American translation.
* Added ability to set subreddit-specific default translations.
* Set the following translation defaults: Christianity = ESV, TrueChristian = ESV, Catholicism = Douay-Rheims.

### September 16, 2013
* VerseBot released on [/r/Catholicism](http://www.reddit.com/r/Catholicism/).
* VerseBot released on [/r/OrthodoxChristianity](http://www.reddit.com/r/OrthodoxChristianity).

### September 13, 2013
* Updated PRAW to 2.1.6. This fixes spamming during times when reddit is under heavy load.
* Restructured database. Now only stores the comment ids of comments that have been replied to.
* Added a Python set that keeps track of comment ids from the current session. This is to further protect against spamming in the event the bot loses connection to the database.
* Renamed .p extensions to .pickle. The .p files were being incorrectly recognized by Github as OpenEdge ABL files.
* Added 1 Macc, 1 Mac, 2 Macc, and 2 Mac to the list of Bible abbreviations.
* Attempt at fixing situation where a valid comment is not replied to.

### September 5, 2013
* Added KJV Deuterocanon to bot
* Changed .pk1 file extensions to .p
* kjv.pk1 is now kjvapocrypha.p (still includes books not in the apocrypha)

### August 28, 2013
* Removed old, unused code.

### August 26, 2013
* Now correctly handles case where the starting verse is greater than the ending verse (e.g. John 3:17-16).

### August 24, 2013
* Fixed replies with multiple verse quotations outputting the desired verses in random order.
* Updated PRAW in requirements.txt to 2.1.5.
* Added the following Bible abbreviations to booknames.py: 1Samuel, 1Sam, 1Sm, 2Samuel, 2Sam, 2Sm, 1Kings, 1Kgs, 2Kings, 2Kgs, 1Chronicles, 1Chron, 1Chr, 2Chronicles, 2Chron, 2Chr, 1Corinthians, 1Cor, 2Corinthians, 2Cor, 1Thessalonians, 1Thess, 1Thes, 2Thessalonians, 2Thess, 2Thes, 1Timothy, 1Tim, 1Tm, 2Timothy, 2Tim, 2Tm, 1Peter, 1Pet, 1Pt, 2Peter, 2Pet, 2Pt, 1John, 1Jn, 2John, 2Jn, 3John, 3Jn.

### August 23, 2013
* Altered message that is displayed when quoted verses exceed the character limit.
* Fixed bot replying to links when not directly called upon.

### August 22, 2013
* Added 'mat' (Matthew) to the list of accepted Bible names/abbreviations.
* Changed character limit from 2000 to 3000 (still experimenting with this).

### August 21, 2013
* Bot now scans new subreddit comments instead of comments from the top ten hot threads.
* Bot is now triggered by verse quotations within brackets.
* Bot will now post alternate comment if constructed comment exceeds 2000 characters.
* Added booknames.py, a dictionary with a collection of accepted Bible names (including abbreviations).
* Repickled Bible translation files to use book numbers instead of book names to cooperate with booknames.py.
* Added docs/Accepted Bible Names.md.
* Added docs/VerseBot Info.md.
* Added CHANGELOG.md.
* Removed 'Starting next scan...' console output.
