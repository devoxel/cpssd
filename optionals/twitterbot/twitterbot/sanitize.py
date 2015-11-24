"""
--> See README.md for info

Author: Aaron Delaney
Email:  aaron.delaney29@mail.dcu.ie
Date:   20/11/2015
"""

import re
import string

_word_regex      = r"\s+" # split by space characters

# compiling the regex first will make it faster
# since if it's uncompiled, it's recompiled on a call to re 
_word_comp_regex = re.compile(_word_regex)

def strip_word(s, regex):
    return re.split(regex, s)

def break_up(s):
    return strip_word(s, _word_comp_regex)

def clean_sentence(s):
    is_cap = True
    out = ""
    for word in s.split():
        clean_word = word.strip()
        if is_cap:
            out += clean_word.capitalize()
            is_cap = False
        else:
            out += clean_word
        if clean_word in string.punctuation:
            is_cap = True
        out += " "
    return out
