
# Usage

It's recommnded to use `toggleboard.py` from the terminal.

    cd <location>
    python toggleboard.py
 
# Testing

Since many errors are silenced with python's try except syntax
I allow for an optional argument, `--debug`, to be passed into 
`toggleboard.py`, like so:

    python toggleboard.py --debug

You can also pass in `--test` to initiate some internal 
class method and function tests to ensure the program is
working correctly, and can handle bad input elegantly.

# Controls

To use WASD controls instead of coordinate input, use
--control-wasd, like so:

    python toggleboard.py --control-wasd/--control-coord

