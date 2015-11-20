import items
import people

jail_cell_room = {
    "desc_short": "your cramped jail cell",
    "desc_long": "A small dusty stone room with just enough space for your matress and a chamber pot"
    "items": [ items.jail_window_wall, items.jail_matress, items.jail_cell_door ]
    "people": [ people.jail_guard ]
}

class Inventory(object):
    def __init__(self, seq=[]):
        self.inventory  = []
        for elm in seq:
            self.inventory.append(elm)


class Player(object):
    def __init__(self, start_room, starting_items):
        self.hp = 100
        self.current_room = start_room
        self.inventory = starting_items


class World(object):
    def __init__(self, debug = False):
        self.debug  = debug
        self.player = Player( jail_cell_door,
                              Inventory[items.rags] )


    def make_action(self, action):
        print action
