"""
--> See README.md for info

Author: Aaron Delaney
Email:  aaron.delaney29@mail.dcu.ie
Date:   20/11/2015
"""

import csv
import random
import math
import string

from sanitize import break_up, clean_sentence
from helper   import safe_get

# the deque is a python queue-like object
# https://docs.python.org/2/library/collections.html#collections.deque
from collections import deque

def parse_corpus(csvf, col, lines):
    """Read in a corpus from a file and return a list of strings in the list"""
    s = []
    reader = csv.reader(csvf)
    i = 0
    for row in reader:
        if i >= lines:
            break
        else:
            s.extend(break_up(row[col]))
            i += 1
    return s

class MarkovChain(object):
    def __init__(self, corpus):
        """ MarkovChain(corpus) -> returns MarkovChain built with corpus

        Arguments
        ---------
        #### corpus
            type: list of strings

        Chain Storage
        -------------
        The Markov Chain is stored in a large dictionary where
        Prefix objects map to Suffix objects.

        These objects are based on the Words object which handles
        the overrides. The object also handles removing punctuation
        and handling probability of each word being a starting word,
        ending word, etc.
        """
        self._chain  = {}
        self._build_chain(corpus)


    def _build_chain(self, corpus):
        """ Build the MarkovChain

        Structure of MarkovChain representation:

            {
              prefix1: {
                prefix2following1: { suffix1: times appeared, ...}, ...
              } ...
            }

        prefix2following1 indicates we are keeping track of two words, rather
        than one.
        """
        current_words = deque(corpus[0:2], maxlen=3)
        for i in xrange(2, len(corpus)):
            current_words.append(corpus[i])

            word1 = current_words[0]
            word2 = current_words[1]
            word3 = current_words[2]

            suffix = word3
            firstmap = self._chain.get(word1)
            if firstmap is None:
                self._chain[word1] = { word2: { suffix: 1 } }
            else:
                secondmap = firstmap.get(word2)
                if secondmap is None:
                    firstmap[word2] = { suffix: 1 }
                else:
                    if suffix in secondmap:
                        secondmap[suffix] += 1
                    else:
                        secondmap[suffix] = 1

    def choose_suffix(self, keyset, mapping):
        """ Choose a suffix based on it's probability

        Here we try to choose a good suffix, given a mapping (which is
        essentially the dictionary providing the suffixs)

        Note that in case we don't find a suffix naturally,
        we do store a set of other options
        """
        sorted_suffixs = sorted(keyset, reverse=True, key=lambda x: mapping[x])

        total_usages = 0.0 # float here to make sure no rounding happens
        for key in sorted_suffixs:
            total_usages += mapping[key]

        # try to be reasonable fair, so use uniform
        accum_goal = random.uniform(0, total_usages)
        accum = 0
        chosen = None
        other_possibilities = []

        for suffix in sorted_suffixs:
            accum += mapping[suffix]
            if accum >= accum_goal:
                chosen = suffix
            elif suffix in self._chain:
                other_possibilities.append(suffix)

        if chosen is None:
            if len(other_possibilities) > 0:
                chosen = other_possibilities.pop()
            else:
                raise ValueError

        return chosen

    def choose_start(self):
        """Choose a random start location"""
        possible_start1 = random.choice(self._chain.keys())
        possible_start2 = random.choice(self._chain[possible_start1].keys())
        return (possible_start1, possible_start2)

    def check_end(self, prefix):
        """Provide a probability that the prefix ends the sentence.
        This probability is accumulated over time.
        """
        p = 0
        for c in prefix:
            if c in ".!":
                p += .5 # average 2 sentences
                break
            elif c in "@":
                p += .25 # don't want too many @s
                break
        return p

    def generate(self):
        """Generate a sentence based off the generated chain"""
        current_prefix = deque(self.choose_start(), maxlen=2)

        s = ""
        limit = 140
        exit_chance = 0

        while len(s) <= limit:
            if len(s) + len(current_prefix[0]) > limit:
                break
            if current_prefix[0] in string.punctuation:
                s += current_prefix[0].lower()
            else:
                s += " " + current_prefix[0]

            exit_chance += self.check_end(current_prefix[0])
            if exit_chance > 1:
                break

            mapping = self._chain[current_prefix[0]][current_prefix[1]]
            suffix = self.choose_suffix(mapping.keys(), mapping)
            current_prefix.append(suffix)

        return clean_sentence(s)
