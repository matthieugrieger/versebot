"""
#---------------------#
| VerseBot for reddit |
| By Matthieu Grieger |
#---------------------#
"""

from re import search
from ordereddict import OrderedDict


def get_book_number(phrase):
	""" Find book number of requested book of the Bible. Used to handle multiple forms
	of writing a certain Bible book. """
	
	book_names = OrderedDict([('genesis',1) , ('gen',1) , ('gn',1), ('bereshit', 1), ('exodus',2), ('exod',2), ('ex',2), ('shemot',2), ('leviticus',3),
						 ('lev',3), ('lv',3), ('vayikra',3), ('numbers',4), ('num',4), ('nm',4), ('bemidbar',4), ('deuteronomy',5), ('deut',5),
						 ('dt',5), ('devarim',5), ('joshua',6), ('josh',6), ('yehoshua',6), ('judges',7), ('judg',7), ('jgs',7), ('shoftim',7), ('ruth',8), ('ru',8),
						 ('1 samuel',9), ('1samuel',9), ('1 sam',9), ('1sam',9), ('1 sm',9), ('1sm',9), ('1 shmuel',9), ('1shmuel',9), ('2 samuel',10),
						 ('2samuel',10), ('2 sam',10), ('2sam',10), ('2 sm',10), ('2sm',10), ('2 shmuel',10), ('2shmuel',10), ('1 kings',11), ('1kings',11),
						 ('1 kgs',11), ('1kgs',11), ('1 melachim',11), ('1melachim',11), ('2 kings',12), ('2kings',12), ('2 kgs',12), ('2kgs',12), ('2 melachim',12), ('2melachim',12),
						 ('1 chronicles',13), ('1chronicles',13), ('1 chron',13), ('1chron',13), ('1 chr',13), ('1chr',13), ('2 chronicles',14),
						 ('2chronicles',14), ('2 chron',14), ('2chron',14), ('2 chr',14), ('2chr',14), ('ezra',15), ('ezr',15), ('nehemiah',16),
						 ('neh',16), ('esther',17), ('est',17), ('job',18), ('jb',18), ('psalms',19), ('psalm',19), ('ps',19),
						 ('pss',19), ('proverbs',20), ('prov',20), ('prv',20), ('ecclesiastes',21), ('eccles',21), ('eccl',21),
						 ('song of solomon',22), ('song of songs',22), ('song of sol',22), ('sg',22), ('isaiah',23), ('isa',23), ('yeshayahu',23), ('yeshaya',23),
						 ('jeremiah',24), ('jer',24), ('yirmiyahu',24), ('yirmiyah',24), ('lamentations',25), ('lam',25), ('ezekiel',26), ('ezek',26), ('yechezkel',26), ('daniel',27),
						 ('dan',27), ('dn',27), ('hosea',28), ('hos',28), ('hoshea',28), ('joel',29), ('jl',29), ('yoel',29), ('amos',30), ('am',30),
						 ('obadiah',31), ('obad',31), ('ob',31), ('ovadiah',31), ('ovadyah',31), ('jonah',32), ('jon',32), ('micah',33), ('mic',33), ('michah',33), ('nahum',34),
						 ('nah',34), ('na',34), ('nachum',34), ('habakkuk',35), ('hab',35), ('hb',35), ('chavakuk',35), ('zephaniah',36), ('zeph',36), ('zep',36), ('tzefaniah',36), ('tzefanyah',36),
						 ('haggai',37), ('hag',37), ('hg',37), ('chaggai',37), ('zechariah',38), ('zech',38), ('zec',38), ('zecharya',38), ('zecharyah',38), ('zechariyah',38), ('malachi',39),
						 ('mal',39), ('matthew',40), ('mathew',40), ('matt',40), ('mat',40), ('mt',40), ('mark',41), ('mk',41), ('luke',42), ('lk',42),
						 ('john',43), ('jn',43), ('acts',44), ('acts of the apostles',44), ('romans',45), ('rom',45),
						 ('1 corinthians',46), ('1corinthians',46), ('1 cor',46), ('1cor',46), ('2 corinthians',47), ('2corinthians',47),
						 ('2 cor',47), ('2cor',47), ('galatians',48), ('gal',48), ('ephesians',49), ('eph',49), ('philippians',50), ('phil',50),
						 ('colossians',51), ('col',51), ('1 thessalonians',52), ('1thessalonians',52), ('1 thess',52), ('1thess',52),
						 ('1 thes',52), ('1thes',52), ('2 thessalonians',53), ('2thessalonians',53), ('2 thess',53), ('2thess',53),
						 ('2 thes',53), ('2thes',53), ('1 timothy',54), ('1timothy',54), ('1st timothy',54), ('1 tim',54), ('1tim',54), ('1 tm',54), ('1tm',54),
						 ('2 timothy', 55), ('2timothy',55), ('2nd timothy',55), ('2 tim',55), ('2tim',55), ('2 tm',55), ('2tm',55), ('titus',56), ('ti',56),
						 ('philemon',57), ('philem',57), ('phlm',57), ('hebrews',58), ('heb',58), ('james',59), ('jas',59),
						 ('1 peter',60), ('1peter',60), ('1 pet',60), ('1pet',60), ('1 pt',60), ('1pt',60), ('2 peter',61), ('2peter',61),
						 ('2 pet',61), ('2pet',61), ('2 pt',61), ('2pt',61), ('1 john',62), ('1john',62), ('1 jn',62), ('1jn',62), ('2 john',63),
						 ('2john',63), ('2 jn',63), ('2jn',63), ('3 john',64), ('3john',64), ('3 jn',64), ('3jn',64), ('jude',65), ('revelation',66),
						 ('revelations',66), ('rev',66), ('rv',66), ('judith',67), ('judeth',67), ('jdt',67), ('wisdom',68), ('wis',68), ('wisdom of solomon', 68),
						 ('tobit',69), ('tob',69), ('sirach',70), ('sir',70), ('ecclesiasticus',70), ('baruch',71), ('bar',71), ('1 maccabees',72),
						 ('1maccabees',72), ('1 macc',72), ('1macc',72), ('1 mac',72), ('1mac', 72), ('2 maccabees',73), ('2maccabees',73), ('2 macc', 73),
						 ('2macc',73), ('2 mac',73), ('2mac',73), ('3 maccabees',74), ('3maccabees',74), ('3 macc',74), ('3macc',74), ('3 mac',74), ('3mac',74),
						 ('4 maccabees',75), ('4maccabees',75), ('4 macc',75), ('4macc',75), ('4 mac',75), ('4mac',75), ('rest of daniel',76), ('additions to daniel',76),
						 ('adddan',76), ('song of the three children',76), ('prayer of azariah',76), ('rest of esther',77), ('additions to esther',77), ('addesth',77),
						 ('prayer of manasses',78), ('prayer of manasseh',78), ('manasses',78), ('manasseh',78), ('prman',78), ('1 esdras',79), ('1esdras',79), ('1 esd',79),
						 ('1esd',79), ('2 esdras',80), ('2esdras',80), ('2 esd',80), ('2esd',80), ('story of susanna',81), ('susanna',81), ('sus',81), ('bel and the dragon',82), ('bel',82)])

	sorted_books = OrderedDict(sorted(book_names.items(), key=lambda t: len(t[0]), reverse=True))
	for key, value in sorted_books.items():
		if search(r'\b' + key + r'\b', phrase):
			return value
	return False


def get_book_title(book_num):
	""" Find appropriate book name for certain book number. Used to create title for
	verse and to construct BibleGateway URLs. """
	
	book_titles = {1:'Genesis', 2:'Exodus', 3:'Leviticus', 4:'Numbers', 5:'Deuteronomy', 6:'Joshua', 7:'Judges', 8:'Ruth',
				9:'1 Samuel', 10:'2 Samuel', 11:'1 Kings', 12:'2 Kings', 13:'1 Chronicles', 14:'2 Chronicles', 15: 'Ezra',
				16:'Nehemiah', 17:'Esther', 18:'Job', 19:'Psalms', 20:'Proverbs', 21:'Ecclesiastes', 22:'Song of Songs',
				23:'Isaiah', 24:'Jeremiah', 25:'Lamentations', 26:'Ezekiel', 27:'Daniel', 28:'Hosea', 29:'Joel', 30:'Amos',
				31:'Obadiah', 32:'Jonah', 33:'Micah', 34:'Nahum', 35:'Habakkuk', 36:'Zephaniah', 37:'Haggai', 38:'Zechariah',
				39:'Malachi', 40:'Matthew', 41:'Mark', 42:'Luke', 43:'John', 44:'Acts', 45:'Romans', 46:'1 Corinthians',
				47:'2 Corinthians', 48:'Galatians', 49:'Ephesians', 50:'Philippians', 51:'Colossians', 52:'1 Thessalonians',
				53:'2 Thessalonians', 54:'1 Timothy', 55:'2 Timothy', 56:'Titus', 57:'Philemon', 58:'Hebrews', 59:'James',
				60:'1 Peter', 61:'2 Peter', 62:'1 John', 63:'2 John', 64:'3 John', 65:'Jude', 66:'Revelation',
				67:'Judith', 68:'Wisdom', 69:'Tobit', 70:'Ecclesiasticus', 71:'Baruch', 72:'1 Maccabees',
				73:'2 Maccabees', 74:'3 Maccabees', 75:'4 Maccabees', 76:'Prayer of Azariah', 77:'Additions to Esther',
				78:'Prayer of Manasseh', 79:'1 Esdras', 80:'2 Esdras', 81:'Susanna', 82:'Bel and the Dragon'}

	return book_titles[book_num]


def get_tanakh_name(book_name):
	""" Retrieves book name used by TaggedTanakh to construct links to their website. """
	
	tanakh_names = {'Genesis':'Gen', 'Exodus':'Exod', 'Leviticus':'Lev', 'Numbers':'Num', 'Deuteronomy':'Deut', 'Joshua':'Josh',
			   'Judges':'Judg', '1 Samuel':'1%20Sam', '2 Samuel':'2%20Sam', '1 Kings':'1%20Kings', '2 Kings':'2%20Kings',
			   'Isaiah':'Isa', 'Jeremiah':'Jer', 'Ezekiel':'Ezek', 'Hosea':'Hosea', 'Joel':'Joel', 'Amos':'Amos', 'Obadiah':'Obad',
			   'Jonah':'Jon', 'Micah':'Mic', 'Nahum':'Nah', 'Habakkuk':'Hab', 'Zephaniah':'Zeph', 'Haggai':'Hag', 'Zechariah':'Zech',
			   'Malachi':'Mal', 'Psalms':'Ps', 'Proverbs':'Prov', 'Job':'Job', 'Song of Songs':'Songs', 'Ruth':'Ruth', 'Lamentations':'Lam',
			   'Ecclesiastes':'Eccles', 'Esther':'Esther', 'Daniel':'Dan', 'Ezra':'Ezra', 'Nehemiah':'Neh', '1 Chronicles':'1%20Chron',
			   '2 Chronicles':'2%20Chron'}
	return tanakh_names[book_name]


def get_default_translation(subreddit, book_num):
	""" Finds default translation for the specified subreddit. This function is called
	whenever a user doesn't specify a translation. NOTE: Subreddits with ESV as the
	default translation are not listed in default_translations, as this is the overall
	default translation for the bot. """
	
	default_translations = {'Catholicism':'NABRE', 'Judaism':'NJPS', 'AcademicBiblical':'NRSV', 'Protestantism':'KJV', 'latterdaysaints':'KJV', 'divineoffice':'NABRE', 'Lectionary':'NRSV', 'Resurrexi':'NABRE', '3OP':'NABRE', 'DebateACatholic':'NABRE'}
	default_deutero_translations = {'Catholicism':'DRA', 'Resurrexi':'DRA', '3OP':'DRA', 'DebateACatholic':'DRA'}

	if book_num >= 67:
		if book_num != 74 and book_num != 75: # Not all translations support 3 and 4 Maccabees (just in case)
			try:
				return default_deutero_translations[subreddit]
			except KeyError:
				return 'NRSV'
		else:
			return 'NRSV'
	else:
		try:
			return default_translations[subreddit]
		except KeyError:
			return 'ESV'
