import configparser

config = configparser.ConfigParser()

def startup():    
    print('Loading config file...')
    config.read('config.ini')
    print('Config file loaded!')

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
    return ConfigSectionMap('Options')['scan-limit']

def getScanDelay():
    return ConfigSectionMap('Options')['scan-delay']