# VerseBot
A reddit bot that is triggered by Bible verse references in reddit comments. It posts the contents of the verse selection as a reply to the comment with the Bible verse reference.

## Usage
### Installation
First, you will want to install PRAW ([Python Reddit API Wrapper](https://github.com/praw-dev/praw)).
Once PRAW is installed, just load up the .py file in a text editor and make the following changes:

Next, you will want to edit the options for the bot by editing `config.ini`.

Once that's done, run `versebot.py` and it should be running fine!

### Triggering the bot
The syntax is now less strict than it was in the previous versions. Here's some examples of ways to trigger the bot:
* Bible chapter reference (ex. `Psalms 23`)
* Bible verse range reference (ex. `John 3:16-17`)
* Bible verse reference (ex. `John 3:16`)

The bot will scan for verse references that follow the form outlined above.

## Authors
Matthieu Grieger

## License
	The MIT License (MIT)

	Copyright (c) 2013 Matthieu Grieger

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

## Thanks
[Jeffrey Ness](https://github.com/jness) for the Pickle file included in this project.