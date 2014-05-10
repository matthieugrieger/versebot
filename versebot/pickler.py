from xml.dom import minidom
from ordereddict import OrderedDict
import pickle

dom = minidom.parse('jps.xml')

bible = OrderedDict()
for book in dom.getElementsByTagName('BIBLEBOOK'):
    book_number = book.getAttribute('bnumber')
    bible[book_number] = {}
    for chapter in book.getElementsByTagName('CHAPTER'):
        chapter_number = chapter.getAttribute('cnumber')
        bible[book_number][int(chapter_number)] = {}
        for verse in chapter.getElementsByTagName('VERS'):
            verse_number = verse.getAttribute('vnumber')
            if verse.firstChild != None:
                verse_text = verse.firstChild.wholeText
                bible[book_number][int(chapter_number)][int(verse_number)] = verse_text

f = open('NJPS.pickle', 'wb')
pickle.dump(bible, f)
f.close()
