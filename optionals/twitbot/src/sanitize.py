import re

_word_regex      = r"\@?\W+?"
_word_comp_regex = re.compile(_word_regex)

def strip_word(s, regex):
    return re.split(regex, s)

def break_up(s):
    return strip_word(s, _word_comp_regex)
