"""
--> See README.md for info

Author: Aaron Delaney
Email:  aaron.delaney29@mail.dcu.ie
Date:   20/11/2015
"""

import re

_word_regex      = r"\s+" # split by space characters
# compiling the regex first will make it nicer
_word_comp_regex = re.compile(_word_regex)

def strip_word(s, regex):
    return re.split(regex, s)

def break_up(s):
    return strip_word(s, _word_comp_regex)
