pathfinder.py
Written by Aaron Delaney, 2015

Built with https://www.python.org/
Developed for CPSSD1 @ DCU
Last Accessed: 06/11/2015

Dependencies:
  Python 2.7.X

Other References:
  Used pdoc to generate html documenation, https://github.com/BurntSushi/pdoc

See docs/pathfinder.m.html for the pdoc generated html

-------------------------------------------------------------------------

Usage:
     python pathfinder.py [OPTIONS] [TABLE FILE PATHS ...]

Prints out the amount of paths in a table from the
top left to the bottom right.

If no table_files are provided, pathfinder.py will enter an interactive
user mode.

Options
-------

--verbose:
    Enables verbose output

--help
    Print this help file

--test
    Initiates test protocol.

    This uses the in-build series of tests to ensure the num_of_paths works as
    intended.

TABLE FILE PATHS
----------------

Table file paths refer to paths to table files.

Table Files
-----------

A table file is a file representing a table, or a series of tables.

You should pass in the file path, relative to where you run pathfinder.

Here is an example of a table entered in one of these files:

1111
1101
1111
1111

If you want to have multiple tables in the same file
separate the with a newline.

It's important you get the size right here, unlike in
the user interactive mode.

Examples
-------

# Testing
$ python pathfinder.py --verbose --test

# Using example files
$ python pathfinder.py --verbose example_tables.txt

# Interactive mode
$ python pathfinder.py --verbose

Input Assumptions
-----------------

To save time for people entering many lines, you can enter
something like this:

$ 11
$ 1111

And pathfinder will assume you mean:

$ 1100 # <-- zeros were padded as an assumption
$ 1111

Interactive Mode
----------------

The input is much the same as the file input.

Enter a string of characters for each row in the table and to signify
then end of table just enter a newline.
