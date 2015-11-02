"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.

class World(object):
    def __init__(self, assets):
        self.debug = assets.meta.debug
        self.places = assets.places
        self.entities = assets.entities
        self._current_area = assets.places.starting_location(assets.places)

    def get_description(self):
        return self._current_area.long_desc
