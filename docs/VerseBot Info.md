# VerseBot Information

## FAQ

### What is VerseBot?
VerseBot is a reddit bot that is triggered by Bible verse references in reddit comments. It posts the contents of the verse selection as a reply to the comment with the Bible verse reference.

### Where is it currently being used?
VerseBot is currently running on [/r/Christianity](http://www.reddit.com/r/christianity) and [/r/TrueChristian](http://www.reddit.com/r/TrueChristian).

### How do I use it?
If you want VerseBot to quote a Bible verse from your comment, simply surround it in brackets ([]). That's it! However, there are some small rules that your Bible quotation must follow:

* When specifying which book your verse comes from, you must use a name from [this list](https://github.com/matthieugrieger/versebot/blob/master/docs/Accepted%20Bible%20Book%20Names.md).
* You must put a space between the book name and the chapter number.
* You must only ask for one verse quotation per bracket pair. However, you can have as many bracket pairs as you want!

Other than these three things, the bot is pretty flexible!

### Can you give me some examples of how to use the bot?
Definitely! Here are some examples of _correct_ usage of the bot:

* `[John 3:16]`
* `[john 3:16 niv]`
* `[NRSV jn 3:16]`

Here are some examples of _incorrect_ usage of the bot:

* `[John3:16]` (No space between book name and chapter number)
* `[John]` (No chapter specified)
* `[Song niv of Songs 1:1]` (Translation is in the middle of a book name)
* `[nrsv John 3:16, Genesis 1:1]` (Two verses are being quoted in one bracket pair)
* `John 3:16` (There are no brackets surrounding the verse)

_Remember, the verse quotation can be located **ANYWHERE** in your comment!_

### What translations of the Bible are supported?
Currently, VerseBot supports the following translations:

* English Standard Version (ESV)
* New International Version (NIV)
* New Revised Standard Version (NRSV)
* King James Version (KJV)

### How do I specify a translation for my verse quotation?
Easy! Just put the desired translation in the brackets next to the desired verse. 

Example: `[NIV John 3:16]` or `[john 3:16 kjv]`. If no translation is specified, the bot defaults to ESV.

### Why is the bot not responding to my comment?
This could be attributed to a few different things:
* Your verse quotation doesn't follow the guidelines specified above.
* The bot is down temporarily for maintenance/updates.
* Heroku (where this bot is hosted) is down or is restarting apps.
* The bot is trying to keep up with commands (there is a 30 second sleep period between comment scans).
* The bot has crashed. This should be rare, but even if it does happen Heroku automatically restarts crashed apps within 10 minutes.

### What should I do if I still have questions?
Just ask me! You can [contact me on reddit](http://www.reddit.com/message/compose/?to=mgrieger).