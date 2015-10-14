
import math

def get_perm(s, words=''):
    if len(s) == 1:
        return s
    else:
        for i in xrange(0, len(s)):
            new_word = s[:i] + s[i+1:]   
            perms = get_perm(new_word, words)
            words += s[i] + perms
    return words

print get_perm(' asdf ')
