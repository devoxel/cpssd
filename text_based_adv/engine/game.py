"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.

import controller
import world

class Game(object):
    def __init__(self, assets):
        self.debug = assets.meta.debug
        self.assets = assets
        self.prompt_controller = controller.Prompt()
        self.player = assets.entities.Player(self.prompt_controller)

    def run(self):
        pass
