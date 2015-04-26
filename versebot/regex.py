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
        r"\-?\d*)?\s*\(?(?P<translation>[\w\-\d]+)?\)?(?=\])")

    matches = re.findall(regex, message_body)
    if len(matches) == 0:
        return None
    else:
        return matches


def find_already_quoted_verses(message_body):
    """ Uses regex to search an existing VerseBot response for verse
    quotations. Used for removing invalid statistics from database. """

    regex = (r"\[\*\*(?P<book>[\d\w\s]+)\d+\:?\d*\-?\d*\s\|\s[\w\d\s]+"
        r"\((?P<translation>[\w\-\d]+)?\)")

    matches = re.findall(regex, message_body)
    if len(matches) == 0:
        return None
    else:
        return matches


def find_default_translations(message_body):
    """ Uses regex to search a private message for default translations
    when a user sends a default translation request. """

    regex = (r"OT\:\s(?P<ot>[\w\-\d]+),\sNT\:\s(?P<nt>[\w\-\d]+),"
        r"\sDeut\:\s(?P<deut>[\w\-\d]+)")

    match = re.findall(regex, message_body)
    if len(match) == 0:
        return None, None, None
    else:
        return match[0][0], match[0][1], match[0][2]


def find_subreddit_in_request(message_body):
    """ Uses regex to search a private message for a subreddit when a
    user sends a default translation request. """

    regex = (r"Subreddit\:\s(?P<subreddit>[\w\d_]+)")

    match = re.findall(regex, message_body)
    if len(match) == 0:
        return None
    else:
        return match[0][0]
