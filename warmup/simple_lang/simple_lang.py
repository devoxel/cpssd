"""
Usage: simple_lang.py filname [word word ...]
"""

import sys

def probability_of_sentence(s, corpus):
    p = 1.0
    for c in s:
        p *= (corpus[c] / corpus['__lenght__'])
    return p

def generate_corpus(f):
    corpus = { '__lenght__': 0. }
    for line in f:                        
        sentence = line.strip('\n').split()
        for word in sentence:        
            if word in corpus:
                corpus[word] += 1
            else:
                corpus[word] = 1
            corpus['__lenght__'] += 1
    return corpus

if __name__ == '__main__':
    len_args = len(sys.argv)

    if len_args > 2:
        with open(sys.argv[1]) as f:
            corpus = generate_corpus(f)
        
        seq = []
        for i in range(2, len_args):
            seq.append(sys.argv[i])
        
        m = ('the', 1)
        for key in corpus:
            if m[1] > corpus[key]:
                m[1] = corpus[key]
                m[0] = key
        print m
        print probability_of_sentence(seq, corpus)
    else:
        print __doc__
