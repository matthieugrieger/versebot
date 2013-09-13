# VerseBot
A reddit bot that is triggered by Bible verse references in reddit comments. It posts the contents of the verse selection as a reply to the comment with the Bible verse reference.

[See the bot in action!](http://www.reddit.com/user/VerseBot)

## Usage
### Installation
First, you will want to install PRAW ([Python Reddit API Wrapper](https://github.com/praw-dev/praw)).
Once PRAW is installed, you will also need to install [psycopg2](http://initd.org/psycopg/docs/install.html#install-from-a-package). This is used to connect to the PostgreSQL database.

In order to run the bot as-is, you must use [Heroku](https://www.heroku.com/). In order to use Heroku, you must register an account and install [Heroku Toolbelt](https://toolbelt.heroku.com/).

Once the bot is deployed to Heroku, you must set your environment variables. Below are the required variables that need to be set:

* `NIVBIBLE`: File path to niv.pickle
* `ESVBIBLE`: File path to esv.pickle
* `KJVBIBLE`: File path to kjvapocrypha.pickle
* `NRSVBIBLE`: File path to nrsv.pickle
* `USERNAME`: reddit username of the account you want the bot to run on
* `PASSWORD`: Password of aforementioned reddit account
* `SUBREDDITS`: List of subreddits you want the bot to run on (multiple subreddits can be added if they are separated with + signs)

Refer to the [Heroku config vars documentation](https://devcenter.heroku.com/articles/config-vars) to learn how to set the environment variables.

Lastly, you must setup a Heroku Postgres database for storing comment ids. Go to the [Heroku Postgres addon page](https://addons.heroku.com/heroku-postgresql), choose a plan (dev plan works fine), and add it to your Heroku app.

To setup the database, simply execute this command in GIT Bash:

`$ cat createtable.sql | heroku pg:psql DATABASE_URL`

For the above command to work, you must have [PostgreSQL](http://www.postgresql.org/download/) installed on your computer. Also, you may have to change DATABASE_URL to the environment variable specific to your database. To find it, just type `heroku config` in Git Bash.

### Triggering the bot
[Refer to the VerseBot FAQ](https://github.com/matthieugrieger/versebot/blob/master/docs/VerseBot%20Info.md#faq).

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
[Jeffrey Ness](https://github.com/jness) for [this blog post](http://blog.flip-edesign.com/_rst/Using_a_KJV_Bible_with_Pickle_and_Python.html).