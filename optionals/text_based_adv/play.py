#!/usr/bin/python
"""
This file handles connecting the data to the game engine.

It serves therefore as the entry point for the game itself.
"""

import assets
from engine.game import Game

if __name__ == '__main__':
    closed_circuit = Game(assets)
    closed_circuit.run()
