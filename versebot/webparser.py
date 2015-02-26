"""
VerseBot for reddit
By Matthieu Grieger
webparser.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

from warnings import filterwarnings
filterwarnings("ignore", category=DeprecationWarning)
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class WebParser:
    """ WebParser class for BibleGateway parsing methods. """
    
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
        
    def get_bible_gateway_verse(self, book, chapter, verse=None, translation="ESV"):
        """ Retrieves the text for a user-supplied verse selection that can be found on BibleGateway. """
        url = "https://www.biblegateway.com/passage/?search=%s+%s:%s&version=%s"
        
        if verse is not None:
            url = "https://www.biblegateway.com/passage/?search=%s+%s:%s&version=%s" % (book, chapter, verse, translation)
        else:
            url = "https://www.biblegateway.com/passage/?search=%s+%s&version=%s" % (book, chapter, translation)

        page = urlopen(url)
        soup = BeautifulSoup(page.read())

        verses = soup.findAll("span", {"class":"text"})

        # Check to make sure that verses have been retrieved. Some translations only support
        # Old Testament or New Testament, meaning that some queries will not return any
        # verses.
        if verses == []:
            return False

        global _verse_title
        global _trans_title
        _verse_title = soup.find("span", {"class":"passage-display-bcv"}).get_text()
        _trans_title = soup.find("span", {"class":"passage-display-version"}).get_text()

        contents = ""
        numbers = re.compile(r"(\d+)")
        for verse in verses:
            if verse.find("span", {"class":"indent-1-breaks"}) != None:
                verse.find("span", {"class":"indent-1-breaks"}).decompose()
            if verse.parent.name != "h3" and verse.parent.name != "h4":
                if "<span class=\"chapternum\">" in str(verse):
                    text = verse.get_text().replace(chapter, "1") + " "
                elif verse.get_text() == "Back":
                    text = ""
                else:
                    text = verse.get_text() + " "
                text = numbers.sub(r"[**\1**]", text, 1)
            else:
                text = "\n\n>**" + verse.get_text() + "**  \n"

            contents += re.sub(r"\[\w\]", "", text)

        return contents
