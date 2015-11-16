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

class Suffix(object):
    def __init__(self, word):
        self._len = 1
        self.ending_word = 1.
        self.starting_word = 1.
        self.balance_ending_probability(word)
        self.balance_starting_probability(word)

    def balance_ending_probability(self, s):
        p = 1.
        if s[-1] != '.':
            if safe_get(s[-3:-2], 0) == '.':
                p *= .75
            else:
                p *= .25
        self.ending_word *= p

    def balance_starting_probability(self, s):
        p = 1.
        if s[0] == s[0].capitalize():
            p *= .85
        self.starting_word *= p

    def add(self, s):
        self.balance_ending_probability(s)
        self.balance_starting_probability(s)
        self._len += 1

    def __len__(self):
        return self._len

    def __hash__(self):
        return hash(repr(self))


class MarkovChain(object):
    def __init__(self):
        self._chain = {}
        self._prefixs = {}

    def build_chain(self, corpus):
        for i in xrange(0, len(corpus)):
            prefix = safe_get( corpus[i:i+1],   0)
            suffix = safe_get( corpus[i+1:i+2], 0)
            if prefix is not None and suffix is not None:
                clean_prefix = clean_up(prefix)
                clean_suffix = clean_up(suffix)
                
                if clean_prefix not in self._prefixs:
                    self._prefixs[clean_prefix] = Suffix(prefix)
                else:
                    self._prefixs[clean_prefix].add(prefix)

                prefix = clean_up(prefix)
                if prefix not in self._chain:
                    self._chain[prefix] = { clean_suffix: Suffix(suffix) }
                elif prefix in self._chain:
                    if clean_suffix in self._chain[prefix]:
                        self._chain[prefix][clean_suffix].add(suffix)
                    else:
                        self._chain[prefix][clean_suffix] = Suffix(suffix)

    def generate(self):
        starts = random.sample(self._prefixs, 25)
        sorted_starts = sorted(self._prefixs.keys(), 
                        key=lambda x: self._prefixs[x].starting_word, reverse=True)
        p =  int( abs(random.gauss(0, .2) * len(sorted_starts) ) )
        current = sorted_starts[p]
        s = ""
        limit = 140
        while len(s) + len(current) < limit:
            s += current + " "
            sorted_suffixs = sorted(self._chain[current].keys(), 
                                key= lambda x: len(self._chain[current][x]), reverse=True)
            accum = random.random()
            changed = False
            first_possible = None
            for key in sorted_suffixs:
                if key in self._chain:
                    if first_possible is None:
                        first_possible = key
                    cost = len(self._chain[current][key])/len(sorted_suffixs)
                    accum += cost
                    if accum >= 1:
                        current = key
                        changed = True
            if not changed:
                current = first_possible
        return s
