from pathway import Pathway

class AjarDoor(Pathway):
    def __init__(self, linked_area):
        self.linked_area = linked_area
        self.desc = "A door that is slightly open"
