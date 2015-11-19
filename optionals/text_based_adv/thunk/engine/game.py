"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.

import controller
import world

class Game(object):
    def __init__(self, assets):
        self.world = world
        self.debug = assets.meta.debug
        self.entities = assets.entities
        self.actions = assets.actions
        self.prompt_controller = controller.Prompt()
        self.player = assets.entities.Player(self.prompt_controller)

    def run(self):
        user_input = self.prompt_controller('$')
        if user_input in self.actions:
            print "Horray"
