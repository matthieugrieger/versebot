from os import environ

#global bible, username, password, subreddits, commentfile

#def getEnvVariables(): # Reduces load on Heroku a tiny bit (loads environment variables just once)
#    bible = environ['BIBLE']
#    username = environ['USERNAME']
#    password = environ['PASSWORD']
#    subreddits = environ['SUBREDDITS']
#    commentfile = environ['COMMENTFILE']

def getBible():
    return environ['BIBLE']

def getBotUsername():
    return environ['USERNAME']

def getBotPassword():
    return environ['PASSWORD']

def getSubreddits():
    return environ['SUBREDDITS']

def getCommentIdFile():
    return environ['COMMENTFILE']