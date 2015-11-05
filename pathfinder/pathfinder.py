"""
pathfinder.py
=============
- Written by Aaron Delaney, 2015
- Built with https://www.python.org/
- Developed for CPSSD1 @ DCU

Command Line Interface
----------------------

Usage: python pathfinder.py [OPTIONS] [TABLE FILE PATHS ...]

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

Table Files
-----------

A table file is a file representing a table, or a series of tables.

You should pass in the file path, relative to where you run pathfinder.

Here is an example of a table entered in one of these files:

```
1111
1101
1111
1111
```

If you want to have multiple tables in the same file
seperate the with a newline.

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


Interactive Mode
----------------

The input is much the same as the file input.

Enter a string of characters for each row in the table and to signify
then end of table just enter a newline.

However, to save time for people entering many lines, you can enter
something like this:

```
$ 11
$ 1111
```

And pathfinder will assume you mean:

```
$ 1100 # <-- zeros were padded as an assumption
$ 1111
```
"""

import sys
import traceback

def _formatted_table(t):
    """Little helper function to print a nicly formatted table"""
    # if t looks like [[12,19,3,4],[2,6,100,1]]
    # output should be:
    #     12 19 3   4
    #     2  6  100 1
    try:
        digit_padding = 0
        for row in t:
            for v in row:
                digit_padding = max(len(str(v)), digit_padding)
        out = ""
        for row in t:
            out += '|'
            for v in row:
                s = str(v)
                padding = (digit_padding - len(s))
                out += s + ' '*padding + '|'
            out += '\n'
    except:
        out = str(t)
    return out

def pathfinder_cli():
    """CLI interprets the arguments and options passed to pathfinder.py"""

    # In order to allow verbose to be the last input the evaluations
    # must be carried out after reading all the arguments.
    verbose = False
    read_from_file = [] # list of files to print
    print_help = False
    do_tests = False

    # The first argument is always the filename, so ignore it
    for arg in sys.argv[1:]:
        if arg == '--verbose':
            verbose = True
        elif arg == '--help':
            print_help = True
        elif arg == '--test':
            do_tests = True
        else:
            read_from_file.append(arg)

    if print_help:
        # __doc__ refers to the docstring at the begining of the file
        print(__doc__)
    elif do_tests:
        test_num_of_paths(verbose)
    elif len(read_from_file) > 0:
        for path in read_from_file:
            parse_file(path, verbose)
    else:
        try:
            interactive_input(verbose)
        except KeyboardInterrupt:
            print ' Bye Bye!'
            sys.exit(0)
        except EOFError: # this makes sure people can pipe in data
            sys.exit(0)
        except SystemExit:
            sys.exit(0)

def parse_binary_string(s):
    """Removes non binary characters from a string"""
    binary_list = []
    for c in s:
        if c in '01':
            binary_list.append(int(c))
    return binary_list

def handle_table_input(string, verbose):
    table = []
    output = []
    for row in string.split('\n'): 
        current_row = parse_binary_string(row)
        print current_row
        if len(current_row) > 0:
            table.append(current_row)
        else:
            path_output = '\nNumber of paths: ' + str(num_of_paths(table, verbose))
            if verbose:
                output.append( _formatted_table(table) + path_output )
            else:
                output.append(path_output)
    return output

def parse_file(filepath, verbose):
    file_string = ''
    with open(filepath) as f:
        file_string = f.read()    
    for output in handle_table_input(file_string, verbose):
        print output 

def interactive_input(verbose):
    """Take user input from strings"""
    # this syntax is a special multiline string
    prompt = ("\nEnter your table by simple writing a 0 for an unpassable tile\n"
              "or a 1 for an unpassable tile, as a string of integers\n\n"
              "For example:\n11100111\n\n"
              "Press CTRL+C or type s to exit\n"
              "Blank line runs pathfinder on entered table\n"
              "Any unexpected value is interpreted as a newline\n"
             )
    string_seperator = "_________________________________"

    while True:
        table_entered = False
        table = []
        max_columns = 0
        print string_seperator
        print prompt
        while not table_entered:

            row = []
            user_input = raw_input()

            if user_input[0:1].lower() == 's':
                sys.exit(0)

            try:
                user_input = parse_binary_string(user_input)
                for c in user_input:
                    row.append(int(c))
            except ValueError:
                print 'Invalid character in row'
                if verbose: print traceback.format_exc()
                continue # don't evaluate the rest of this while loop

            max_columns = max(len(row), max_columns)

            if len(row) == 0:
                table_entered = True
            else:
                table.append(row)

        for row in table:
            if len(row) < max_columns:
                for i in range(0, max_columns-len(row)):
                    # lists are mutable types so this will change table too
                    row.append(0)

        print handle_table_input(table, verbose)[0]
        print string_seperator
        user_input = raw_input('\nEnter "s" to stop, otherwise continue: ')
        if user_input[0:1].lower() == 's':
            sys.exit(0)

def num_of_paths(table, verbose, num_rows=None, num_cols=None):
    """num_of_paths -> returns int

    Finds the total possible of ways to traverse a table from the top left
    to the bottom right.

    The table can consist of 1s and 0s.

    1s represent a movable location.
    0s represent a location that is blocked off.

    Table Input Format
     [
       [1,1,0,0],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]
     ]
    The table should be accessed by table[y][x]
    """
    try:
        num_paths = 0
        if num_rows == None: num_rows = len(table)
        if num_cols == None: num_cols = len(table[0])
        value_table = [[ 0 for j in range(0, num_cols) ] for i in range(0, num_rows)]
        for cur_y in range(0, num_rows):
            if len(table[cur_y]) != num_cols:
                raise IndexError # we explicitly wants correct tables
            for cur_x in range(0, num_cols):
                value = table[cur_y][cur_x]
                if value != 0 and value != 1:
                    raise TypeError
                if value == 1:  # tile is visitable
                    left = cur_x - 1
                    up   = cur_y - 1
                    if cur_x == 0 and cur_y == 0:
                        prev_left_value = 1
                        prev_up_value = 0
                    elif cur_x == 0:
                        prev_left_value = 0
                        prev_up_value = value_table[up][cur_x]
                    elif cur_y == 0:
                        prev_up_value = 0
                        prev_left_value = value_table[cur_y][left]
                    else:
                        prev_up_value = value_table[up][cur_x]
                        prev_left_value = value_table[cur_y][left]
                    new_value = prev_left_value + prev_up_value
                    value_table[cur_y][cur_x] = new_value
        if verbose:
            print _formatted_table(value_table)
        return value_table[num_rows-1][num_cols-1]
    except IndexError:
        if verbose:
            print '\nInvalid table, eg: unbalanced rows'
            print traceback.format_exc()
        return -1
    except TypeError:
        if verbose:
            print traceback.format_exc()
            print '\nPassed in the wrong data'
        return -1

def test_num_of_paths(verbose):
    """_test(verbose): run unit tests on num_of_paths

    If verbose is true lots of stuff is printed
    """
    if verbose:
        print '\n# Testing pathfinder.py'

    test_data = {
        'empty_list' : ([], -1),
        'basic1' : ([[1]], 1),
        'basic2' : ([[0]], 0),
        'basic3' : ([ [1,1], [1,1] ], 2),
        'basic4' : ([ [1,1], [1,1], [1,1] ], 3),
        'square_easy' : ([[1,1,1],[1,1,1],[1,1,1]],  6),
        'square_hard' : ([[1,0,0], [1,1,0],[1,1,1]], 2),
        'table_strange' : ([[1] for i in range(0,13)], 1),
        'invalid_table' : ([1,1,1], -1),
        'invalid_table2' : ("table!?", -1),
        'invalid_table3' : ([[1,1,1], [1,1,1,1]], -1),
        'invalid_table4' : ([['foo', 'bar'], ['spam', 'eggs']], -1),
    }

    for key in test_data:
        list_to_test    = test_data[key][0]
        expected_value  = test_data[key][1]
        # verbose is false because we don't need to see things
        # multiple tinmes
        value           = num_of_paths(list_to_test, verbose=False)
        if verbose:
            print '-', 'testing:\n', _formatted_table(list_to_test)
            print '-', 'should return ', expected_value
            print '-', 'returned', value, '\n'
        try:
            assert expected_value == value
        except AssertionError:
            if verbose: print traceback.format_exc()
            print '++ Test failed. Run with --verbose'
            sys.exit(1)

    print '++ Tests passed'
    return 0


if __name__ == '__main__':
    pathfinder_cli()
