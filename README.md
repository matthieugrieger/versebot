![VerseBot](http://i.imgur.com/zzFkW5g.png)

**A reddit bot that posts Bible verses when asked to.**

* [Usage](#usage)
  * [Making Verse Quotations](#making-verse-quotations)
  * [Editing/Deleting a VerseBot Comment](#editing-deleting-a-versebot-comment)
  * [Setting a Default Translation](#setting-a-default-translation)
* [Authors](#authors)
* [License](#license)
* [Thanks](#thanks)

## USAGE
### Making Verse Quotations
VerseBot is triggered by username mentions. Verse quotations are enclosed in brackets ([]), and may specify a desired translation within. A VerseBot quotation must follow one of the following formats (in each case the translation is optional):

```
[Book Chapter Translation]
[Book Chapter:Verse Translation]
[Book Chapter:StartVerse-EndVerse Translation]
```

More quotation formats will be implemented in the future.

### Editing/Deleting a VerseBot Comment
VerseBot comments can be easily edited or deleted by clicking on the "edit" or "delete" links that can be found at the bottom of every VerseBot comment. Only the user who triggered the VerseBot response can edit or delete the comment.

### Setting a Default Translation
A default translation is the translation VerseBot defaults to for a particular user or subreddit. This means that a user/subreddit can specify a default translation, and the user(s) do not need to place the abbreviation for the translation within their comment.

Translation defaults are prioritized in the following order:

1) User Translation
2) Subreddit Translation
3) VerseBot Translation

Default translations can be set by visiting the [Default Translations section](http://matthieugrieger/versebot/#defaults) of the VerseBot website.

There are two types of default translations that can be set:

1) *User Translations* -- A set of default translations for a reddit user. Note that user default translations that have not been used for 90 days or more will be deleted to save on database storage space.

2) *Subreddit Translations* -- A set of default translations for a subreddit. This type of default translation **must** be set by a moderator of the subreddit, otherwise VerseBot will simply ignore the request. Subreddit default translations never expire.

## AUTHORS
[Matthieu Grieger](http://matthieugrieger.com)

## LICENSE
	The MIT License (MIT)

	Copyright (c) 2014, 2015 Matthieu Grieger

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in
	all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
	THE SOFTWARE.

## THANKS
* [BibleGateway](http://www.biblegateway.com) and [Bible Hub](http://biblehub.com/) for being the sources of all texts posted by VerseBot.  
* [All those who contribute](https://github.com/praw-dev/praw/graphs/contributors) to [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw).
* [Adam Grieger](https://github.com/adamgrieger) for the awesome VerseBot image at the top of this README.
