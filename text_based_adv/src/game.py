"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.

import controller

class Game(object):
    def __init__(self, assets):
        if assets.meta.debug == True:
            self.debug = True
            print '# Initializing game'

        self.prompt_controller = controller.Prompt()
        self.player = assets.entities.Player(self.prompt_controller)

    def run(self):
        if self.debug: print '# Game running'
