"""
VerseBot for reddit
By Matthieu Grieger
regex.py
Copyright (c) 2015 Matthieu Grieger (MIT License)
"""

import re

def find_verses(message_body):
    """ Uses regex to search comment body for verse quotations. Returns
    a list of matches if found, None otherwise. """
    
    regex = (r"(?<=\[)(?P<book>[\d\w\s]+)(?P<chapter>\d+)\:?(?P<verse>\d+"
        + r"\-?\d*)?\s*\(?(?P<translation>[\w\-\d]+)?\)?(?=\])")
    
    return re.findall(regex, message_body)
