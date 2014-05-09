#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

from bs4 import BeautifulSoup
from collections import namedtuple
import re
import urllib2

_supported_translations = list()
_verse_title = ''
_verse_translation = ''

# Retrieve the contents of the Bible passage the user requested. Obtains and
# parses the text from BibleGateway.com.
def get_verse_contents(book_name, chapter, verse, translation):
	if verse != '0':
		url = ('http://www.biblegateway.com/passage/?search=' + book_name + '+' + chapter + ':' + verse + '&version=' + translation).replace(' ', '%20')
	else:
		url = ('http://www.biblegateway.com/passage/?search=' + book_name + '+' + chapter + '&version=' + translation).replace(' ', '%20')
			
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	
	verses = soup.findAll('span', {'class':'text'})
	
	# Check to make sure that verses have been retrieved. Some translations only support
	# Old Testament or New Testament, meaning that some queries will not return any
	# verses.
	if verses == []:
		return False
	
	global _verse_title
	global _trans_title
	
	heading = soup.find('div', {'class':'heading'})
	_verse_title = heading.h3.get_text()
	_trans_title = heading.p.get_text()
	
	contents = ''
	for verse in verses:
		if verse.find('span', {'class':'indent-1-breaks'}) != None:
			verse.find('span', {'class':'indent-1-breaks'}).decompose()
		if verse.parent.name != 'h3' and verse.parent.name != 'h4':
			if '<span class="chapternum">' in str(verse):
				text = verse.get_text().replace(chapter, '1') + ' '
			else:
				text = verse.get_text() + ' '
			numbers = re.compile(r'(\d+)')
			text = numbers.sub(r'[**\1**]', text, 1)
		else:
			text = '\n\n>**' + verse.get_text() + '**  \n'
			
		
		contents += re.sub(r'\[\w\]', '', text)
		
	return contents

# Retrieves the translations that are supported by the bot. 	
def find_supported_translations():
	global _supported_translations
	url = 'http://www.biblegateway.com/versions/'
		
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
		
	translations = soup.findAll('tr')
		
	for translation in translations:
		if 'Text' in translation.get_text():
			trans = translation.findAll('td')
			for t in trans:
				if t.a != None:
					cur_trans = t.a.get_text()
					if cur_trans != 'Text':
						_supported_translations.append(cur_trans[cur_trans.rfind('(')+1:cur_trans.rfind(')')])

# Simply returns the list of supported translations.	
def get_supported_translations():
	_supported_translations.sort(key=len, reverse=True)
	return _supported_translations

# Returns the verse title provided by BibleGateway.
def get_verse_title():
	return _verse_title
	
# Returns the translation title provided by BibleGateway.	
def get_translation_title():
	return _trans_title
