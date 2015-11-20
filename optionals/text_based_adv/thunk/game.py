"""
=_
"""
import sys

from control import Controller
from world   import World

class Game(object):
    def __init__(self):
        self.input  = Controller()
        self.world  = World(debug=True)

    def output(self, o):
        print '\n'*100, o

    def play(self):
        world_output = self.world.start
        while True:
            try:
                self.output(world_output)
                action = self.input.get_action()
                world_output = self.world.make_action(action)
            except SystemExit:
                print "\nBye Bye"
                sys.exit(0)
