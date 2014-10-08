"""
#---------------------#
| VerseBot for reddit |
| By Matthieu Grieger |
#---------------------#
"""

from os import environ


def get_bot_username():
	""" Returns the username of the bot, stored in the USERNAME environment
	variable. """
	
	return environ['USERNAME']


def get_bot_password():
	""" Returns the password of the bot, stored in the PASSWORD environment
	variable. """
	
	return environ['PASSWORD']

    
def get_database():
	""" Returns the URL to the PostgreSQL database, stored in the
	HEROKU_POSTGRESQL_ONYX_URL environment variable. """
	
	return environ['HEROKU_POSTGRESQL_ONYX_URL']


def get_local_bible(translation):
	""" Returns the .pickle file for the specified translation. """
	
	return 'bibles/' + translation + '.pickle'
	
