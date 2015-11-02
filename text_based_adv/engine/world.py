"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.

class World(object):
    def __init__(self, assets):
        self.debug = assets.meta.debug
        self.assets = assets
        self.current_area = assets.meta.places.starting_location
