"""
#---------------------#
| VerseBot for reddit |
| By Matthieu Grieger |
#---------------------#
"""

from re import findall


def find_bracketed_text(comment_text):
	""" Finds bracketed portions of text within a comment body that allows characters
	that are often included in a verse quotation. """
	
    return findall(r'\[[\w\s:,-]+](?!\()', comment_text)


def find_verses(bracketed_text):
	""" Finds possible verses within a bracketed portion of a comment's body.
	Ex: Passing in [John 3:16] would return John 3:16. """
	
    return findall(r'(?:\d\w*\s)?(?:\w+\s\w+\s\w+)?(?:\w+\s\w+\s\w+\s\w+)?\w+\s\d+:?\d*-?\d*(?:\s\w+\s?-?\w*)?', bracketed_text)

   
def find_already_quoted_verses(comment_body):
	""" Finds all comment titles in a VerseBot comment. Used to correct database statistics
	after a user requests that their VerseBot response be edited or deleted. """
	
	return findall(r'\[\*\*(.{4,})\*\*\]', comment_body)

	
def find_translation_in_title(title):
	""" Finds the translation abbreviation in a verse quotation title. """
	
	return findall(r'\((.+)\)', title)[0]
