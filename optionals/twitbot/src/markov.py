import csv
import itertools
import random
import math

from sanitize import break_up
from helper   import safe_get

from collections import deque

def parse_corpus(csvf, lines):
    s = []
    reader = csv.reader(csvf)
    i = 0
    for row in reader:
        if i >= lines:
            break
        else:
            s.extend(break_up(row[5]))
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
        """
        """
        current_words = deque(corpus[0:3], maxlen=4)
        for i in xrange(3, len(corpus)):
            current_words.append(corpus[i])

            word1 = current_words[0]
            word2 = current_words[1]
            word3 = current_words[2]
            word4 = current_words[3]

            suffixs = (word3, word4)
            firstmap = self._chain.get(word1)
            if firstmap is None:
                self._chain[word1] = { word2: { suffixs: 1 } }
            else:
                secondmap = firstmap.get(word2)
                if secondmap is None:
                    firstmap[word2] = { suffixs: 1 }
                else:
                    if suffixs in secondmap:
                        secondmap[suffixs] += 1
                    else:
                        secondmap[suffixs] = 1

    def choose_suffix(self, keyset, mapping):
        sorted_suffixs = sorted(keyset, reverse=True, key=lambda x: mapping[x])

        total_usages = 0.0 # float here to make sure no rounding happens
        for key in sorted_suffixs:
            total_usages += mapping[key]

        accum = random.random()
        chosen = None
        other_possibilities = []

        for suffix in sorted_suffixs:
            cost = mapping[suffix] / total_usages
            accum += cost
            if accum >= 1:
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
        possible_start1 = random.choice(self._chain.keys())
        possible_start2 = random.choice(self._chain[possible_start1].keys())
        return (possible_start1, possible_start2)

    def generate(self):
        current_prefix = self.choose_start()
        s = ""
        limit = 140
        while len(s) < limit:
            print current_prefix
            s += current_prefix[0] + " " + current_prefix[1] + " "
            mapping = self._chain[current_prefix[0]][current_prefix[1]]
            current_prefix = self.choose_suffix(mapping.keys(), mapping)
        return s + "."
