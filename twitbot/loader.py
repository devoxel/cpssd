import sys
sys.dont_write_bytecode = True
from src.markov import MarkovChain, parse_corpus

if __name__ == "__main__":
    with open("corpuses/training.1600000.processed.noemoticon.csv", "r") as f:
        corpus = parse_corpus(f, 10000)
    mrk = MarkovChain(corpus)

    while True:
        print mrk.generate()
        raw_input("\nEnter to generate more, ctrl+z to exit\n... ")
