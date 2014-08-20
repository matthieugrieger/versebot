#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

from os import environ

def get_bot_username():
	return environ['USERNAME']

def get_bot_password():
	return environ['PASSWORD']
    
def get_database():
	return environ['HEROKU_POSTGRESQL_ONYX_URL']

def get_local_bible(translation):
	return 'bibles/' + translation + '.pickle'
	
