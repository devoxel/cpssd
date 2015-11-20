import sys
sys.dont_write_bytecode = True

from thunk.game import Game

thunk = Game()
thunk.play()
