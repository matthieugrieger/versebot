"""
#---------------------#
| VerseBot for reddit |
| By Matthieu Grieger |
#---------------------#
"""

from bs4 import BeautifulSoup
from collections import namedtuple
from config import get_local_bible
from data import get_book_title
import pickle
import re
import urllib2

_supported_translations = list()
_verse_title = ''
_verse_translation = ''


def get_verse_contents(book_name, book_num, chapter, verse, translation):
	""" Calls the appropriate helper function to retrieve the contents of a verse. """
	
	if translation == 'NJPS':
		contents = _get_local_contents(book_num, chapter, verse, translation)
	else:
		contents = _get_biblegateway_contents(book_name, chapter, verse, translation)

	return contents


def _get_biblegateway_contents(book_name, chapter, verse, translation):
	""" Retrieve the contents of the Bible passage the user requested. Obtains and
	parses the text from BibleGateway.com. """
	
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
	_verse_title = soup.find('span', {'class':'passage-display-bcv'}).get_text()
	_trans_title = soup.find('span', {'class':'passage-display-version'}).get_text()

	contents = ''
	for verse in verses:
		if verse.find('span', {'class':'indent-1-breaks'}) != None:
			verse.find('span', {'class':'indent-1-breaks'}).decompose()
		if verse.parent.name != 'h3' and verse.parent.name != 'h4':
			if '<span class="chapternum">' in str(verse):
				text = verse.get_text().replace(chapter, '1') + ' '
			elif verse.get_text() == 'Back':
				text = ''
			else:
				text = verse.get_text() + ' '
			numbers = re.compile(r'(\d+)')
			text = numbers.sub(r'[**\1**]', text, 1)
		else:
			text = '\n\n>**' + verse.get_text() + '**  \n'


		contents += re.sub(r'\[\w\]', '', text)

	return contents


def _get_local_contents(book_num, chapter, verse, translation):
	""" Retrieve the contents of the Bible passage the user requested.
	Obtains text from local pickle file. Used for translations
	that BibleGateway does not support. """
	
	f = open(get_local_bible(translation), 'rb')
	bible = pickle.load(f)
	f.close()

	global _verse_title
	global _trans_title

	if verse != '0':
		_verse_title = get_book_title(book_num) + ' ' + chapter + ':' + verse
	else:
		_verse_title = get_book_title(book_num) + ' ' + chapter
	# This will need to be changed if more pickle files are added.
	_trans_title = 'JPS Tanakh (NJPS)'

	verse_text = ''
	if book_num and chapter:
		try:
			if verse != '0':
				if '-' in verse:
					starting_ver = verse.partition('-')[0]
					ending_ver = verse.partition('-')[2]
					if int(starting_ver) < int(ending_ver) + 1:
						for ver in range(int(starting_ver), int(ending_ver) + 1):
							verse_text += '[**' + str(ver) + '**] ' + (bible[str(book_num)][int(chapter)][ver] + ' ')
					else:
						return False
				else:
					verse_text = '[**' + verse + '**] ' + bible[str(book_num)][int(chapter)][int(verse)]
			else:
				for ver in bible[str(book_num)][int(chapter)]:
					verse_text += '[**' + str(ver) + '**] ' + (bible[str(book_num)][int(chapter)][ver] + ' ')

			return verse_text
		except KeyError:
			return False


def find_supported_translations():
	""" Retrieves the translations that are supported by the bot. """
	
	global _supported_translations
	url = 'http://www.biblegateway.com/versions/'

	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())

	translations = soup.find('select', {'class':'search-translation-select'})
	trans = translations.findAll('option')
	for t in trans:
		if t.has_attr('value') and not t.has_attr('class'):
			cur_trans = t['value']
			_supported_translations.append(cur_trans)

	# Add local translations to supported translations list
	_supported_translations.append('NJPS')


def get_supported_translations():
	""" Retrieves the translations that are supported by the bot. """
	
	_supported_translations.sort(key=len, reverse=True)
	return _supported_translations


def get_verse_title():
	""" Returns the verse title provided by BibleGateway. """
	
	return _verse_title


def get_translation_title():
	""" Returns the translation title provided by BibleGateway. """
	return _trans_title
