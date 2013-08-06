# VerseBot

## What is VerseBot?
VerseBot is a Reddit bot that quotes Bible verses when asked.

## Usage
First, you will want to install PRAW ([Python Reddit API Wrapper](https://github.com/praw-dev/praw)).
Once PRAW is installed, just load up the .py file in a text editor and make the following changes:

Set the desired Reddit account the bot will use by replacing `'bot-username'` and `'bot-password'` on this line:
`r.login('bot-username', 'bot-password')`

Set the desired subreddits that you want the bot to work on by replacing `'desired-subreddit'` on this line:
`subreddit = r.get_subreddit('desired-subreddit')`

## Authors
Matthieu Grieger

## License
Feel free to do whatever you want with it.

## Thanks
[Jeffrey Ness](https://github.com/jness) for the Pickle file included in this project.