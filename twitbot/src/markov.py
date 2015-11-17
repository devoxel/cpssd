import csv
import itertools
import random
import math

from sanitize import clean_up, break_up
from helper   import safe_get

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


class WordPair(object):
    def __init__(self, *args):
        self._words = []
        self._str = ""
        for word in args:
            if word is not None:
                self._words.append(clean_up(word))
                self._str += " " + word

        if self._words > 0:
            self._words = tuple(self._words)
        else:
            self._words = None

        self._len = 1

    def __repr__(self):
        return repr(self._words) + '*' + repr(self._len)

    def __len__(self):
        return self._len

    def __eq__(self, other):
        return self._words == other._words

    def __hash__(self):
        return hash(self._words)

    def __str__(self):
        return self._str

class Prefix(WordPair):
    pass

class Suffix(WordPair):
    def add(self):
        self._len += 1


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
        self._chain = {}
        self.build_chain(corpus)


    def build_chain(self, corpus):
        """
        """
        for i in xrange(0, len(corpus)):
            word1 = safe_get(corpus[i:i+1], 0)
            word2 = safe_get(corpus[i+1:i+2], 0)
            word3 = safe_get(corpus[i+2:i+3], 0)
            word4 = safe_get(corpus[i+4:i+5], 0)

            prefix = Prefix(word1, word2)
            suffix = Suffix(word3, word4)
            mapped_suffixs = self._chain.get(prefix)
            if mapped_suffixs is None:
                self._chain[prefix] = [suffix]
            else:
                if suffix in mapped_suffixs:
                    mapped_suffixs[mapped_suffixs.index(suffix)].add()
                else:
                    mapped_suffixs.append(suffix)

    def generate(self):
        possible_starts = random.sample(self._chain.keys(), 50)

        sorted_starts = sorted( possible_starts,
                                key=lambda x: len(self._chain[x]) )
        accum = 1 - abs(random.gauss(0, .25))
        while accum

        s = ""
        limit = 140
        current_prefix = sorted_starts.pop()
        while len(s) < limit:
            s += str(current_prefix)
            sorted_suffixs = sorted( self._chain[current_prefix], reverse=True,
                                     key=lambda x: len(x) )
            print current_prefix
            print sorted_suffixs
            # work on the probabilities like accumulators
            accum = 1
            chosen = False
            i = 0
            while accum > 0:
                if suffix in self._chain:
                    cost = len(sorted_suffixs[i]) // len(sorted_suffixs)
                    accum -= cost
                i += 1

            if not chosen and len(other_possibilities) > 0:
                current_prefix = other_possibilities.pop()
            else:
                break

        return s + "."
