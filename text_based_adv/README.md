# Closed Circuit

A text based adventure game by Aaron Delaney for CPSSD1.

## Goals

- Approach modeling the game using a data-driven approach
- Make the game somewhat engaging, but short
- Have a good input engine, work out what the player means to do
- Cross-platform support (which python does great)

### This game is divided into two parts:

#### Game Engine (located in `src/`)

The game engine is the thing that keeps the game moving. It should keep track
of game states, handle the input and views and just make the game work.

It uses game assets to build the game.

Documentation about how the game engine works is located in the README file
in the base of the `src/` folder

#### Game Assets (located in `assets/`)

The game assets area all the aspects of the game that are unique to the game.

Documentation about how the assets are organized is in the README file in the
base of the `assets/` folder.
