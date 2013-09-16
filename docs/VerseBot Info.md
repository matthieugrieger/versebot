# VerseBot Information

## FAQ

### What is VerseBot?
VerseBot is a reddit bot that is triggered by Bible verse references in reddit comments. It posts the contents of the verse selection as a reply to the comment with the Bible verse reference.

### Where is it currently being used?
VerseBot is currently running on [/r/Christianity](http://www.reddit.com/r/christianity), [/r/TrueChristian](http://www.reddit.com/r/TrueChristian), and [/r/Catholicism](http://www.reddit.com/r/Catholicism/).

### How do I use it?
If you want VerseBot to quote a Bible verse from your comment, simply surround it in brackets ([]). That's it! However, there are some small rules that your Bible quotation must follow:

* When specifying which book your verse comes from, you must use a name from [this list](https://github.com/matthieugrieger/versebot/blob/master/docs/Accepted%20Bible%20Book%20Names.md).
* You must put a space between the book name and the chapter number.
* You must only ask for one verse quotation per bracket pair. However, you can have as many bracket pairs as you want!
* At the moment, additional arguments (such as desired translation) must follow the desired verse. This may change in the future.

Other than these three things, the bot is pretty flexible!

### Can you give me some examples of how to use the bot?
Definitely! Here are some examples of _correct_ usage of the bot:

* `[John 3:16]`
* `[john 3:16 niv]`
* `[John 3:16-17]`

Here are some examples of _incorrect_ usage of the bot:

* `[John3:16]` (No space between book name and chapter number)
* `[John]` (No chapter specified)
* `[Song niv of Songs 1:1]` (Translation is in the middle of a book name)
* `[nrsv John 3:16, Genesis 1:1]` (Two verses are being quoted in one bracket pair)
* `John 3:16` (There are no brackets surrounding the verse)
* `[John 3 : 16]` (Spaces between chapter, :, and verse. Only put a space between the book name and chapter!)

_Remember, the verse quotation can be located **ANYWHERE** in your comment!_

### What translations of the Bible are supported?
Currently, VerseBot supports the following translations:

* English Standard Version (ESV)
* New International Version (NIV)
* New Revised Standard Version (NRSV)
* King James Version (KJV)

### How do I specify a translation for my verse quotation?
Easy! Just put the desired translation in the brackets next to the desired verse. 

Example: `[John 3:16 NIV]` or `[john 3:16 kjv]`. If no translation is specified, the bot defaults to ESV.

### Can I quote verses from Deuterocanonical books?
Yes, it is now possible to quote verses from the Deuterocanon. Please take a look at the [Accepted Bible Names](https://github.com/matthieugrieger/versebot/blob/master/docs/Accepted%20Bible%20Book%20Names.md) list to see which books are supported.

**NOTE:** The formatting of Additions to Esther is a bit strange. The verses start from 10:4, not 1:1 like most Bible books. Keep this in mind if you want to quote a verse from Additions to Esther.

### Why is the bot not responding to my comment?
This could be attributed to a few different things:
* Your verse quotation doesn't follow the guidelines specified above.
* The bot is down temporarily for maintenance/updates.
* Heroku (where this bot is hosted) is down or is restarting apps. Heroku provides a [status page](https://status.heroku.com/) that you can check for Heroku downtimes.
* The bot is trying to keep up with commands (there is a 30 second sleep period between comment scans).
* The bot has crashed. This should be rare, but even if it does happen Heroku automatically restarts crashed apps within 10 minutes.

### What should I do if I still have questions?
Just ask me! You can [contact me on reddit](http://www.reddit.com/message/compose/?to=mgrieger).