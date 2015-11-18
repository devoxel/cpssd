import sys
from src.markov import MarkovChain, parse_corpus
from src.helper import safe_get

import cProfile

if __name__ == "__main__":

    lines = safe_get(sys.argv, 1, 160000)

    with open("corpuses/training.1600000.processed.noemoticon.csv", "r") as f:
        corpus = parse_corpus(f, lines)
        print "Done parsing corpus!"

    mrk = MarkovChain(corpus)
    print "Done parsing MarkovChain\n\n"

    while True:
        print mrk.generate()
        raw_input("\nEnter to generate more, ctrl+z to exit\n... ")
