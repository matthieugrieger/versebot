# VerseBot Changelog

### August 24, 2013
* Fixed replies with multiple verse quotations outputting the desired verses in random order.
* Updated PRAW in requirements.txt to 2.1.5.

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