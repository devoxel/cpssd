thunk
=====

A text based adventure game by Aaron Delaney for CPSSD1.


Goals
--------------

- Approach modeling the game using a data-driven approach

- Make the game somewhat engaging, but short

- Have a good input engine and work out what the player means to do

- Cross-platform support



Support
--------------

The game is built on `Python 2.7.X`, and it is recommend you use
that to run from source.



Dependencies
--------------

- `pytest` -- a modular unit-test platform

I would recommend that you install install a virtual environment
but it's not required.

    pip install virtualenv
    virtualenv venv
    # Then activate the VirtualEnv
    # Linux or OSX
    source venv/bin/activate
    # Windows
    .\venv\Scripts\activate


You can automatically install the package with pip

    pip install .


Running from source
--------------------

    # Pip should setup the thunk script, so you should just be able to run
    thunk.py
    # If that doesn't work, you can run the thunk.py file in run
    python run/thunk.py
    # If this fails, pip failed to setup the file somehow
    # running thunk/game.py should work though
    python thunk/game.py


Running the tests
------------------

    py.test


Directory Structure
--------------------

#### Game Engine (located in `thunk/src/`)

The game engine is the thing that keeps the game moving. It should keep track
of game states, handle the input and views and just make the game work.

It uses game assets to build the game.

Documentation about how the game engine works is located in the README file
in the base of the `src/` folder


#### Game Assets (located in `thunk/assets/`)

The game assets area all the aspects of the game that are unique to the game.

Documentation about how the assets are organized is in the README file in the
base of the `assets/` folder.
