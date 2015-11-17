# Created by
#  Aaron Delaney - @devoxel - devoxel.net
# Created for CPSSD First Year Practicium
# All Right Reserved

import sys
import math

# https://docs.python.org/2/library/timeit.html
import timeit # cool library that handles timing functions

class Context(object):
    """A wrapper for global objects"""
    mode = None
    words = None
    modes = ['--palindrom', '--anagram', '--test', '--h']
    arguments = sys.argv
    time_str = '  time (s):\t{}'
    def __init__(self):
        try:
            self.mode = sys.argv[1]
            self.words = sys.argv[2:]
            if len(self.words) == 0 and self.mode != '-h':
                self.words = [ "redivider", "noon", "civic", "radar",
                         "modemimodem", "MadamImAdam", "aaAbbbB", 'fabda']
        except IndexError:
            self.mode = '--h'

context = Context()

# It should be noted that the names of all these functions is exactly mirroring
# the arguments passed in, hence why the names are uninformative
# I could provide better names but I would be overriding python keyword names
# .. for example help() instead of h()

def h():
    print '\nUsage: python yp.py [MODE] [WORD]...'
    print 'Checks if a word is a palindrome using various methods'
    print '\nModes:'
    print '  --palindrome \t\t check if a word is a palindrome'
    print '  --anagram    \t\t check if any anagram of a word is a palindrome'
    print '  --test       \t\t test both modes with the same set of words'
    print '  --h          \t\t print this help file'

def recursive_palindrome_checker():
    print '> Rercursive Palindrome Checker'
    def is_palindrome(s):
        if len(s) > 1:
            return s[0] == s[-1] and is_palindrome(s[1:len(s)-1])
        else:
            return True
    for word in context.words:
        print ' ', word, ':\t', is_palindrome(word.lower())

def iterative_palindrome_checker():
    print '\n> Iterative Palindrom Checker'
    for word in context.words:
        word_lower = word.lower()
        is_palindrome = True
        mid_length = len(word)/2
        for i in xrange(0, mid_length):
            is_palindrome = is_palindrome and (word_lower[i] == word_lower[-(i+1)])
        print ' ', word, ':\t', is_palindrome

def palindrome():
    print context.time_str.format(timeit.timeit(recursive_palindrome_checker, number=1))
    print context.time_str.format(timeit.timeit(iterative_palindrome_checker, number=1))

def anagram_checker():
    print '\n> Anagram Palindrome Possibility'
    def is_even(n):
        return n % 2 == 0

    def count_characters(word):
        character_count = {}
        for c in word:
            if c in character_count:
                character_count[c] += 1
            else:
                character_count[c] = 1
        return character_count

    for word in context.words:
        word_lower = word.lower()
        character_count = count_characters(word_lower)
        is_palindrome = True
        allow_odd = not is_even(len(word_lower)) # allow 1 odd chacter if not even
        for count in character_count.values():
            if not is_even(count) and allow_odd == True:
                allow_odd = False
            else:
                is_palindrome = (is_palindrome and is_even(count))
        print ' ', word, ':\t', is_palindrome

def anagram():
    print context.time_str.format(timeit.timeit(anagram_checker, number=1))

def test():
    palindrome()
    anagram()

if __name__ == '__main__':
    try:
        if context.mode in context.modes:
            exec(context.mode.lstrip('-')+'()')
        else:
            raise IndexError
    except IndexError:
        h()
        sys.exit(1)
    except:
        print sys.exc_info() # for debugging
        sys.exit(1)
    sys.exit(0)
