"""
File docs here, when they're ready!
"""
# Created by Aaron Delaney, see README.md for more information.
from place import Place

class CastleBedroom(Place):
    def __init__(items, entities):
        short_desc  = "a dimly lit room, your bedroom"
        long_desc   = "Your bedroom is nice, but it looks like it needs to be cleaned"

        pathways = {
            entities.pathway.ajar_door: places.CastleStairs()
        }
