- pathfinder.py

Written by Aaron Delaney, 2015

Built with https://www.python.org/
Developed for CPSSD1 @ DCU
Last Accessed: 06/11/2015

MUST HAVE INSTALLED:

  Python 2.7.X

NOTABLE OTHER SOFTWARE USED:

  Used pdoc to generate html documenation
  - https://github.com/BurntSushi/pdoc


DOCS

- Readable HTML documentation has been placed in
      docs/pathfinder.m.html
- If there is an error in that for any reason, refer to the rest of this file.


USAGE

     python pathfinder.py [OPTIONS] [TABLE FILE PATHS ...]

  Prints out the amount of paths in a table from the
  top left to the bottom right.

  Interactive mode:

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

  TABLE FILE PATHS refers to paths to table files. Please use paths python can
  understand, so relative to pathfinder.py, or absolute.


TABLE FILES
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


EXAMPLES
-------

# Testing
$ python pathfinder.py --verbose --test

# Using example files
$ python pathfinder.py --verbose example_tables.txt

# Interactive mode
$ python pathfinder.py --verbose


INPUT ASSUMPTIONS
-----------------

To save time for people entering many lines, you can enter
something like this:

$ 11
$ 1111

And pathfinder will assume you mean:

$ 1100 # <-- zeros were padded as an assumption
$ 1111


INTERACTIVE MODE
----------------

The input is much the same as the file input.

Enter a string of characters for each row in the table and to signify
then end of table just enter a newline.
