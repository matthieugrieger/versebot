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
		"gen":"Genesis",
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
	}
