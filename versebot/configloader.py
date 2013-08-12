import configparser
from sys import exit

config = configparser.ConfigParser()

def startup():    
    print('Loading config file...')
    try:
        config.read('config.ini')
        print('Config file loaded!')
    except:
        print('Error while loading config.ini')
        sys.exit()

def ConfigSectionMap(section):
    dict = {}
    options = config.options(section)
    for option in options:
        try:
            dict[option] = config.get(section, option)
            if dict[option] == -1:
                DebugPrint('Skip: %s' % option)
        except:
            print('Exception on %s!' % option)
            dict[option] = None
    return dict

def getPickle():
    return ConfigSectionMap('Options')['pickle']

def getBotUsername():
    return ConfigSectionMap('Options')['bot-username']

def getBotPassword():
    return ConfigSectionMap('Options')['bot-password']

def getSubreddits():
    return ConfigSectionMap('Options')['subreddits']

def getScanLimit():
    return int(ConfigSectionMap('Options')['scan-limit'])

def getScanDelay():
    return int(ConfigSectionMap('Options')['scan-delay'])