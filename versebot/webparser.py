"""
VerseBot for reddit
By Matthieu Grieger
webparser.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Parser:
    """ Parser class for BibleGateway parsing methods. """
    
    def __init__(self):
        """ Initializes translations attribute and checks if there are any new translations
        to add to the database. """
        self.translations = self.find_supported_translations()
        self.translations.sort(key=len, reverse=True)
        
    def find_supported_translations(self):
        """ Retrieves a list of supported translations from BibleGateway's translation
        page. """
        url = "https://www.biblegateway.com/versions/"
        translations = list()
        
        page = urlopen(url)
        soup = BeautifulSoup(page.read())
        
        translations_select = soup.find("select", {"class":"search-translation-select"})
        trans = translations_select.findAll("option")
        for t in trans:
            if t.has_attr("value") and not t.has_attr("class"):
                cur_trans = t["value"]
                translations.append(cur_trans)

        # Add local translations to supported translations list
        translations.append("NJPS")
        
        return translations
