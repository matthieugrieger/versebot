# VerseBot Changelog

### May 29, 2015
* Another large update!
* VerseBot now scans its own inbox for username mentions instead of scanning every comment on reddit.
* Added user default translation requests.
* Added subreddit default translation requests.
* New translations added to BibleGateway are automatically picked up by the bot within 24 hours.
* Fixed some reddit links that caused AutoModerator to automatically delete VerseBot comments.
* Removed Heroku-related files, not hosted on Heroku any longer.
* Added a cool new header image to the README (thanks [@adamgrieger](https://github.com/adamgrieger))!
* Replaced TaggedTanakh pickle file with Bible Hub website parsing.
* Removed NJPS translation, added JPS translation.
* Added user translation cleaning function. Deletes user translations that haven't been used for 90 days or more.

### March 27, 2015
* Added default translations for [/r/TelaIgne](https://www.reddit.com/r/TelaIgne).

### March 25, 2015
* Fixed "Back" appearing at the end of every verse.

### February 27, 2015
* Updated PRAW dependency.

### January 10, 2015
* Added default translations for [/r/DebateACatholic](https://www.reddit.com/r/DebateACatholic).

### December 17, 2014
* Added default translations for [/r/3OP](http://www.reddit.com/r/3OP).

### December 13, 2014
* Added default translations for [/r/Resurrexi](http://www.reddit.com/r/Resurrexi).

### November 15, 2014
* Added "Eph" as an abbreviation for Ephesians.

### October 7, 2014
* Reformatted code spacing and comments to comply with PEP guidelines.

### August 21, 2014
* Disabled comment edit/deletion again. Still seems to not be working. I will figure this out! Sorry.

### August 20, 2014
* Re-enabled comment edit/deletion. If you find any issues, let me know!
* Fixed some weird formatting issues in config.py.
* Removed code that incorrectly marked some edit/delete messages as read.
* Updated PRAW to 2.1.18.

### August 18, 2014
* Added NABRE translation to database.
* Set default translation for /r/Catholicism and /r/divineoffice to NABRE.

### August 9, 2014
* Temporarily disabled edit/delete actions (again) until I get the chance to fix it once and for all.

### August 6, 2014
* Fixed a bug that made edit/delete actions stop working.
* Moved comment URL in edit/delete message to comment body to avoid creating a subject over 100 characters long (thanks /u/emprags!).
* Added complete translation names and translation languages to translation statistics table.
* Improved readability of some SQL scripts.

### August 5, 2014
* Added the ability for users to edit/delete VerseBot comments. Only the user who triggers the VerseBot response will have the ability to edit/delete the comment.
* Added logic for "fixing" the the book, translation, and subreddit statistics when a VerseBot response is edited/deleted.
* Added a short sentence at the end of the comment footer that gives links for editing and deleting a comment.
* Added messages.py to implement comment editing/deletion, and more functions in the future.
* Moved all regex to regex.py to clean up the code a bit.

### July 31, 2014
* Fixed Biblical references in the book of Wisdom (deuterocanon).
* Updated createdatabase.sql to reflect above change.

### July 16, 2014
* Released the [VerseBot Statistics website!](http://matthieugrieger.com/versebot/)
* Fixed a crash that occurred when trying to reply to a recently deleted comment.
* Set /r/Lectionary default translation to NRSV.

### July 12, 2014
* Changed default translation for /r/AcademicBiblical to NRSV.

### July 9, 2014
* Fixed "Back" appearing at the end of every quotation (thanks to /u/coveredinbeeees for finding this!).

### June 30, 2014
* Compatibility changes for the new version of BibleGateway.

### June 27, 2014
* Reverted to legacy BibleGateway website for compatibility reasons. Will update to the new BibleGateway eventually.

### June 18, 2014
* Updated PRAW to address an AttributeError caused by a recent reddit update.

### June 9, 2014
* Made NRSVCE the default translation of /r/divineoffice.

### May 21, 2014
* Made KJV the default translation of /r/Protestantism.

### May 12, 2014
* Made OJB the default translation of /r/AcademicBiblical.

### May 10, 2014
* Fixed NET Bible translation. Now use the keyword 'NET' to trigger this translation.
* Fixed bot choosing wrong translations.
* Set default translation for /r/Catholicism to RSVCE.
* Added bibles/NJPS.pickle to add the NJPS translation to the bot.
* Added NJPS translation to translation stats table.
* Set default translation for /r/Judaism to NJPS.
* Implemented necessary functions and logic to incorporate pickle files once again.
* Added pickler.py. This is the script that is run to generate pickle files for Bible translations from XML.
* Fixed link to Supported Translations in VerseBot Info.md.

### May 9, 2014
* Fixed the bot mistaking books such as '1 John' as just 'John'.
* Added ordereddict to requirements.txt.

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
* Added the following Bible abbreviations to booknames.py: 1Samuel, 1Sam, 1Sm, 2Samuel, 2Sam, 2Sm, 1Kings, 1Kgs, 2Kings, 2Kgs, 1Chronicles, 1Chron, 1Chr, 2Chronicles, 2Chron, 2Chr, 1Corinthians, 1Cor, 
2Corinthians, 2Cor, 1Thessalonians, 1Thess, 1Thes, 2Thessalonians, 2Thess, 2Thes, 1Timothy, 1Tim, 1Tm, 2Timothy, 2Tim, 2Tm, 1Peter, 1Pet, 1Pt, 2Peter, 2Pet, 2Pt, 1John, 1Jn, 2John, 2Jn, 3John, 3Jn.

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
