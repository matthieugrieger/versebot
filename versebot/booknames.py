from collections import OrderedDict

bookNames = OrderedDict([('genesis',1) , ('gen',1) , ('gn',1), ('exodus',2), ('exod',2), ('ex',2), ('leviticus',3),
                         ('lev',3), ('lv',3), ('numbers',4), ('num',4), ('nm',4), ('deuteronomy',5), ('deut',5),
                         ('dt',5), ('joshua',6), ('josh',6), ('judges',7), ('judg',7), ('jgs',7), ('ruth',8), ('ru',8),
                         ('1 samuel',9), ('1samuel',9), ('1 sam',9), ('1sam',9), ('1 sm',9), ('1sm',9), ('2 samuel',10), 
                         ('2samuel',10), ('2 sam',10), ('2sam',10), ('2 sm',10), ('2sm',10), ('1 kings',11), ('1kings',11),
                         ('1 kgs',11), ('1kgs',11), ('2 kings',12), ('2kings',12), ('2 kgs',12), ('2kgs',12), ('1 chronicles',13), 
                         ('1chronicles',13), ('1 chron',13), ('1chron',13), ('1 chr',13), ('1chr',13), ('2 chronicles',14), 
                         ('2chronicles',14), ('2 chron',14), ('2chron',14), ('2 chr',14), ('2chr',14), ('ezra',15), ('ezr',15), ('nehemiah',16),
                         ('neh',16), ('esther',17), ('est',17), ('job',18), ('jb',18), ('psalms',19), ('psalm',19), ('ps',19),
                         ('pss',19), ('proverbs',20), ('prov',20), ('prv',20), ('ecclesiastes',21), ('eccles',21), ('eccl',21),
                         ('song of solomon',22), ('song of songs',22), ('song of sol',22), ('sg',22), ('isaiah',23), ('isa',23),
                         ('jeremiah',24), ('jer',24), ('lamentations',25), ('lam',25), ('ezekiel',26), ('ezek',26), ('daniel',27),
                         ('dan',27), ('dn',27), ('hosea',28), ('hos',28), ('joel',29), ('jl',29), ('amos',30), ('am',30),
                         ('obadiah',31), ('obad',31), ('ob',31), ('jonah',32), ('jon',32), ('micah',33), ('mic',33), ('nahum',34),
                         ('nah',34), ('na',34), ('habakkuk',35), ('hab',35), ('hb',35), ('zephaniah',36), ('zeph',36), ('zep',36),
                         ('haggai',37), ('hag',37), ('hg',37), ('zechariah',38), ('zech',38), ('zec',38), ('malachi',39),
                         ('mal',39), ('matthew',40), ('matt',40), ('mat',40), ('mt',40), ('mark',41), ('mk',41), ('luke',42), ('lk',42),
                         ('john',43), ('jn',43), ('acts',44), ('acts of the apostles',44), ('romans',45), ('rom',45),
                         ('1 corinthians',46), ('1corinthians',46), ('1 cor',46), ('1cor',46), ('2 corinthians',47), ('2corinthians',47), 
                         ('2 cor',47), ('2cor',47), ('galatians',48), ('gal',48), ('ephesians',49), ('philippians',50), ('phil',50), 
                         ('colossians',51), ('col',51), ('1 thessalonians',52), ('1thessalonians',52), ('1 thess',52), ('1thess',52), 
                         ('1 thes',52), ('1thes',52), ('2 thessalonians',53), ('2thessalonians',53), ('2 thess',53), ('2thess',53), 
                         ('2 thes',53), ('2thes',53), ('1 timothy',54), ('1timothy',54), ('1 tim',54), ('1tim',54), ('1 tm',54), ('1tm',54), 
                         ('2 timothy', 55), ('2timothy',55), ('2 tim',55), ('2tim',55), ('2 tm',55), ('2tm',55), ('titus',56), ('ti',56),
                         ('philemon',57), ('philem',57), ('phlm',57), ('hebrews',58), ('heb',58), ('james',59), ('jas',59),
                         ('1 peter',60), ('1peter',60), ('1 pet',60), ('1pet',60), ('1 pt',60), ('1pt',60), ('2 peter',61), ('2peter',61),
                         ('2 pet',61), ('2pet',61), ('2 pt',61), ('2pt',61), ('1 john',62), ('1john',62), ('1 jn',62), ('1jn',62), ('2 john',63),
                         ('2john',63), ('2 jn',63), ('2jn',63), ('3 john',64), ('3john',64), ('3 jn',64), ('3jn',64), ('jude',65), ('revelation',66),
                         ('revelations',66), ('rev',66), ('rv',66), ('judith',67), ('judeth',67), ('jdt',67), ('wisdom',68), ('wis',68),
                         ('wisdom of solomon',68), ('tobit',69), ('tob',69), ('sirach',70), ('sir',70), ('ecclesiasticus',70), ('baruch',71),
                         ('bar',71), ('1 maccabees',72), ('1maccabees',72), ('1 macc',72), ('1macc',72), ('1 mac',72), ('1mac',72), ('2 maccabees',73), ('2maccabees',73),
                         ('2 macc',73), ('2macc',73), ('2 mac',73), ('2mac',73), ('rest of daniel',74), ('additions to daniel',74), ('adddan',74), ('song of the three children',74),
                         ('prayer of azariah',74), ('rest of esther',75), ('additions to esther',75), ('addesth',75), ('prayer of manasses',76), 
                         ('prayer of manasseh',76), ('manasses',76), ('manasseh',76), ('prman',76), ('1 esdras',80), ('1esdras',80), ('1 esd',80), 
                         ('1esd',80), ('2 esdras',81), ('2esdras',81), ('2 esd',81), ('2esd',81), ('story of susanna',87), ('susanna',87), ('sus',87), 
                         ('bel and the dragon',88), ('bel',88)])

# Used for retrieving string used for verse title
bookTitles = {1:'Genesis', 2:'Exodus', 3:'Leviticus', 4:'Numbers', 5:'Deuteronomy', 6:'Joshua', 7:'Judges', 8:'Ruth',
                9:'1 Samuel', 10:'2 Samuel', 11:'1 Kings', 12:'2 Kings', 13:'1 Chronicles', 14:'2 Chronicles', 15: 'Ezra',
                16:'Nehemiah', 17:'Esther', 18:'Job', 19:'Psalms', 20:'Proverbs', 21:'Ecclesiastes', 22:'Song of Songs',
                23:'Isaiah', 24:'Jeremiah', 25:'Lamentations', 26:'Ezekiel', 27:'Daniel', 28:'Hosea', 29:'Joel', 30:'Amos',
                31:'Obadiah', 32:'Jonah', 33:'Micah', 34:'Nahum', 35:'Habakkuk', 36:'Zephaniah', 37:'Haggai', 38:'Zechariah',
                39:'Malachi', 40:'Matthew', 41:'Mark', 42:'Luke', 43:'John', 44:'Acts', 45:'Romans', 46:'1 Corinthians',
                47:'2 Corinthians', 48:'Galatians', 49:'Ephesians', 50:'Philippians', 51:'Colossians', 52:'1 Thessalonians',
                53:'2 Thessalonians', 54:'1 Timothy', 55:'2 Timothy', 56:'Titus', 57:'Philemon', 58:'Hebrews', 59:'James',
                60:'1 Peter', 61:'2 Peter', 62:'1 John', 63:'2 John', 64:'3 John', 65:'Jude', 66:'Revelation', 67:'Judith',
                68:'Wisdom of Solomon', 69:'Tobit', 70:'Ecclesiasticus', 71:'Baruch', 72:'1 Maccabees', 73:'2 Maccabees', 74:'Prayer of Azariah',
                75:'Additions to Esther', 76:'Prayer of Manasseh', 80:'1 Esdras', 81:'2 Esdras', 87:'Susanna', 88:'Bel and the Dragon'}

# First, this function sorts the keys in bookNames, longest strings first. This is to avoid incorrect triggers.
# Example: Misinterpreting [1 John 1:1] as John 1:1 since the string 'John' IS in '1 John'
def getBookNumber(phrase): 
    sortedBookNames = OrderedDict(sorted(bookNames.items(), key=lambda t: len(t[0]), reverse = True))
    for key, value in sortedBookNames.items():
        if key in phrase:
            return value
    return False

def getBookTitle(bookNum):
    return bookTitles[bookNum]