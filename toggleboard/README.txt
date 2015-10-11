
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

# README

I reccomend you open README.html in a modern browser to see
details on design of the code. It's included in the toggleboard
opening but it's rendered nicely in the html.

# References
Text Generated on:
    http://patorjk.com/software/taag/

Written by Aaron Delaney for CPPSD1 Assignment 3