import sys
sys.dont_write_bytecode = True
from src.markov import MarkovChain, parse_corpus

if __name__ == "__main__":
    mrk = MarkovChain()
    with open("corpuses/training.1600000.processed.noemoticon.csv", "r") as f:
        corpus = parse_corpus(f, 10000 )
    mrk.build_chain(corpus)

    while True:
        print mrk.generate()
        raw_input("... enter to generate more")
