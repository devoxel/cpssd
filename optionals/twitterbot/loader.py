"""
--> See README.md for info

Author: Aaron Delaney
Email:  aaron.delaney29@mail.dcu.ie
Date:   20/11/2015
"""

import sys
import traceback

from twitterbot.markov import MarkovChain, parse_corpus
from twitterbot.helper import safe_get

# import cProfile
#   Used to profile code, no longer needed
# - To see profiling, use cProfile.run("MarkovChain(corpus)")

if "--debug" in sys.argv:
    debug = True
    sys.argv.remove("--debug")
else:
    debug = False

if __name__ == "__main__":

    try:
        # note that third arguments here are default values if the index is
        # not in position indicated in argument 2
        corpus  = safe_get(sys.argv, 1, "corpora/training.1600000.processed.noemoticon.csv")
        col     = safe_get(sys.argv, 2, 5)
        lines   = safe_get(sys.argv, 3, 750000)

        with open(corpus, "r") as f:
            corpus = parse_corpus(f, col, lines)
            print "Done reading corpus that consisted of", lines, "lines."

        mrk = MarkovChain(corpus)
        print "Done creating the MarkovChain object\n\n"
    except:
        print "Looks like you put in the arguments wrong, check the README"
        print "Make sure the file is relative to where you run the command"
        if debug: traceback.print_exc()
        sys.exit(1)

    while True:
        print mrk.generate()
        try:
            raw_input("\n+ Enter to generate more, CTRL-C to exit\n")
        except KeyboardInterrupt:
            print # move the terminal down so the next line is empty
            sys.exit(0)
        except:
            print "Oops, looks like something went wrong with generation"
            if debug: traceback.print_exc()
