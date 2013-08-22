from os import environ

def getNIV():
    return environ['NIVBIBLE']

def getESV():
    return environ['ESVBIBLE']

def getKJV():
    return environ['KJVBIBLE']

def getNRSV():
    return environ['NRSVBIBLE']

def getBotUsername():
    return environ['USERNAME']

def getBotPassword():
    return environ['PASSWORD']

def getSubreddits():
    return environ['SUBREDDITS']