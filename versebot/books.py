"""
VerseBot for reddit
By Matthieu Grieger
books.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

def get_book(name):
    """ Retrieves a standardized book name to replace the one
    provided by the user. """
    
    books = {
        "gen":"Genesis",  # Old Testament
        "gn":"Genesis",
        "bereshit":"Genesis",
        "exodus":"Exodus",
        "exod":"Exodus",
        "ex":"Exodus",
        "shemot":"Exodus",
        "leviticus":"Leviticus",
        "lev":"Leviticus",
        "lv":"Leviticus",
        "vayikra":"Leviticus",
        "numbers":"Numbers",
        "num":"Numbers",
        "nm":"Numbers",
        "bemidbar":"Numbers",
        "deuteronomy":"Deuteronomy",
        "deut":"Deuteronomy",
        "dt":"Deuteronomy",
        "devarim":"Deuteronomy",
        "joshua":"Joshua",
        "josh":"Joshua",
        "yehoshua":"Joshua",
        "judges":"Judges",
        "judg":"Judges",
        "jgs":"Judges",
        "shoftim":"Judges",
        "ruth":"Ruth",
        "ru":"Ruth",
        "1samuel":"1 Samuel",
        "1sam":"1 Samuel",
        "1sm":"1 Samuel",
        "1shmuel":"1 Samuel",
        "2samuel":"2 Samuel",
        "2sam":"2 Samuel",
        "2sm":"2 Samuel",
        "2shmuel":"2 Samuel",
        "1kings":"1 Kings",
        "1kgs":"1 Kings",
        "1melachim":"1 Kings",
        "2kings":"2 Kings",
        "2kgs":"2 Kings",
        "2melachim":"2 Kings",
        "1chronicles":"1 Chronicles",
        "1chron":"1 Chronicles",
        "1chr":"1 Chronicles",
        "2chronicles":"2 Chronicles",
        "2chron":"2 Chronicles",
        "2chr":"2 Chronicles",
        "ezra":"Ezra",
        "ezr":"Ezra",
        "nehemiah":"Nehemiah",
        "neh":"Nehemiah",
        "esther":"Esther",
        "est":"Esther",
        "job":"Job",
        "jb":"Job",
        "psalms":"Psalms",
        "psalm":"Psalms",
        "ps":"Psalms",
        "pss":"Psalms",
        "proverbs":"Proverbs",
        "prov":"Proverbs",
        "prv":"Proverbs",
        "ecclesiastes":"Ecclesiastes",
        "eccles":"Ecclesiastes",
        "eccl":"Ecclesiastes",
        "songofsolomon":"Song of Songs",
        "songofsongs":"Song of Songs",
        "songofsol":"Song of Songs",
        "sg":"Song of Songs",
        "isaiah":"Isaiah",
        "isa":"Isaiah",
        "yeshayahu":"Isaiah",
        "yeshaya":"Isaiah",
        "jeremiah":"Jeremiah",
        "jer":"Jeremiah",
        "yirmiyahu":"Jeremiah",
        "yirmiyah":"Jeremiah",
        "lamentations":"Lamentations",
        "lam":"Lamentations",
        "ezekiel":"Ezekiel",
        "ezek":"Ezekiel",
        "yechezkel":"Ezekiel",
        "daniel":"Daniel",
        "dan":"Daniel",
        "dn":"Daniel",
        "hosea":"Hosea",
        "hos":"Hosea",
        "hoshea":"Hosea",
        "joel":"Joel",
        "jl":"Joel",
        "yoel":"Joel",
        "amos":"Amos",
        "am":"Amos",
        "obadiah":"Obadiah",
        "obad":"Obadiah",
        "ob":"Obadiah",
        "ovadiah":"Obadiah",
        "ovadyah":"Obadiah",
        "jonah":"Jonah",
        "jon":"Jonah",
        "micah":"Micah",
        "mic":"Micah",
        "michah":"Micah",
        "nahum":"Nahum",
        "nah":"Nahum",
        "na":"Nahum",
        "nachum":"Nahum",
        "habakkuk":"Habakkuk",
        "hab":"Habakkuk",
        "hb":"Habakkuk",
        "chavakuk":"Habakkuk",
        "zephaniah":"Zephaniah",
        "zeph":"Zephaniah",
        "zep":"Zephaniah",
        "tzefaniah":"Zephaniah",
        "tzefanyah":"Zephaniah",
        "haggai":"Haggai",
        "hag":"Haggai",
        "hg":"Haggai",
        "chaggai":"Haggai",
        "zechariah":"Zechariah",
        "zech":"Zechariah",
        "zec":"Zechariah",
        "zecharya":"Zechariah",
        "zecharyah":"Zechariah",
        "zechariyah":"Zechariah",
        "malachi":"Malachi",
        "mal":"Malachi",
        "matthew":"Matthew",  # New Testament
        "mathew":"Matthew",
        "matt":"Matthew",
        "mat":"Matthew",
        "mt":"Matthew",
        "mark":"Mark",
        "mk":"Mark",
        "luke":"Luke",
        "lk":"Luke",
        "john":"John",
        "jn":"John",
        "acts":"Acts",
        "actsoftheapostles":"Acts",
        "romans":"Romans",
        "rom":"Romans",
        "1corinthians":"1 Corinthians",
        "1cor":"1 Corinthians",
        "2corinthians":"2 Corinthians",
        "2cor":"2 Corinthians",
        "galatians":"Galatians",
        "gal":"Galatians",
        "ephesians":"Ephesians",
        "eph":"Ephesians",
        "philippians":"Philippians",
        "phil":"Philippians",
        "colossians":"Colossians",
        "col":"Colossians",
        "1thessalonians":"1 Thessalonians",
        "1thess":"1 Thessalonians",
        "1thes":"1 Thessalonians",
        "2thessalonians":"2 Thessalonians",
        "2thess":"2 Thessalonians",
        "2thes":"2 Thessalonians",
        "1timothy":"1 Timothy",
        "1tim":"1 Timothy",
        "1tm":"1 Timothy",
        "2timothy":"2 Timothy",
        "2tim":"2 Timothy",
        "2tm":"2 Timothy",
        "titus":"Titus",
        "ti":"Titus",
        "philemon":"Philemon",
        "philem":"Philemon",
        "phlm":"Philemon",
        "hebrews":"Hebrews",
        "heb":"Hebrews",
        "james":"James",
        "jas":"James",
        "1peter":"1 Peter",
        "1pet":"1 Peter",
        "1pt":"1 Peter",
        "2peter":"2 Peter",
        "2pet":"2 Peter",
        "2pt":"2 Peter",
        "1john":"1 John",
        "1jn":"1 John",
        "2john":"2 John",
        "2jn":"2 John",
        "3john":"3 John",
        "3jn":"3 John",
        "jude":"Jude",
        "revelation":"Revelation",
        "revelations":"Revelation",
        "rev":"Revelation",
        "rv":"Revelation",
        "judith":"Judith",  # Deuterocanon
        "judeth":"Judith",
        "jdt":"Judith",
        "wisdom":"Wisdom",
        "wis":"Wisdom",
        "wisdomofsolomon":"Wisdom",
        "tobit":"Tobit",
        "tob":"Tobit",
        "sirach":"Ecclesiasticus",
        "sir":"Ecclesiasticus",
        "ecclesiasticus":"Ecclesiasticus",
        "baruch":"Baruch",
        "bar":"Baruch",
        "1maccabees":"1 Maccabees",
        "1macc":"1 Maccabees",
        "1mac":"1 Maccabees",
        "2maccabees":"2 Maccabees",
        "2macc":"2 Maccabees",
        "2mac":"2 Maccabees",
        "3maccabees":"3 Maccabees",
        "3macc":"3 Maccabees",
        "3mac":"3 Maccabees",
        "4maccabees":"4 Maccabees",
        "4macc":"4 Maccabees",
        "4mac":"4 Maccabees",
        "restofdaniel":"Prayer of Azariah",
        "additionstodaniel":"Prayer of Azariah",
        "adddan":"Prayer of Azariah",
        "songofthethreechildren":"Prayer of Azariah",
        "prayerofazariah":"Prayer of Azariah",
        "restofesther":"Additions to Esther",
        "additionstoesther":"Additions to Esther",
        "addesth":"Additions to Esther",
        "prayerofmanasses":"Prayer of Manasseh",
        "prayerofmanasseh":"Prayer of Manasseh",
        "manasses":"Prayer of Manasseh",
        "manasseh":"Prayer of Manasseh",
        "prman":"Prayer of Manasseh",
        "1esdras":"1 Esdras",
        "1esd":"1 Esdras",
        "2esdras":"2 Esdras",
        "2esd":"2 Esdras",
        "storyofsusanna":"Susanna",
        "susanna":"Susanna",
        "sus":"Susanna",
        "belandthedragon":"Bel and the Dragon",
        "bel":"Bel and the Dragon"
    }
    
    try:
        converted_name = books[name.lower().replace(" ", "")]
        return converted_name
    except KeyError:
        return False
