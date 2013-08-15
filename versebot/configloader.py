from os import environ

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