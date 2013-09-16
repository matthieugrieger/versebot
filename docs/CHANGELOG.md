# VerseBot Changelog

### September 16, 2013
* VerseBot released on [/r/Catholicism](http://www.reddit.com/r/Catholicism/).

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