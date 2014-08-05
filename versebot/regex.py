#---------------------#
# VerseBot for reddit #
# By Matthieu Grieger #
#---------------------#

from re import findall

# Finds bracketed portions of text within a comment body that allows characters
# that are often included in a verse quotation.
def find_bracketed_text(comment_text):
    return findall(r'\[[\w\s:,-]+](?!\()', comment_text)

# Finds possible verses within a bracketed portion of a comment's body.
# Ex: Passing in [John 3:16] would return John 3:16.
def find_verses(bracketed_text):
    return findall(r'(?:\d\w*\s)?(?:\w+\s\w+\s\w+)?(?:\w+\s\w+\s\w+\s\w+)?\w+\s\d+:?\d*-?\d*(?:\s\w+\s?-?\w*)?', bracketed_text)

# Finds all comment titles in a VerseBot comment. Used to correct database statistics after a user requests that their VerseBot
# response be edited or deleted.    
def find_already_quoted_verses(comment_body):
	return findall(r'\[\*\*(.{4,})\*\*\]', comment_body)

# Finds the translation abbreviation in a verse quotation title.	
def find_translation_in_title(title):
	return findall(r'\((.+)\)', title)[0]
