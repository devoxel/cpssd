"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.
from place import Place

class CastleStairs(Place):
    def __init__(items, places):
        short_desc  = "a long hallway with many doors"
        long_desc   = "It's stone walls reminds you that tomorrow"

        pathways = [
            entities.pathway.AjarDoor(places.CastleStairs())
        ]
