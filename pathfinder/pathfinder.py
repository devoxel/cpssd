"""
# pathfinder.py
    - Written by Aaron Delaney, 2015
    - Built with https://www.python.org/
    - Developed for CPSSD1 @ DCU

## Command Line Interface

Usage: pathfinder.py [OPTIONS]

Options:

  --help:
    Print this help file

  --test:
    Initiates test protocol.

    This uses the in-build series of tests to ensure the program works as
    intended.

  --verbose:
    Enables verbose output

CLI:
  The command line interface is simple but powerful.

      Table Input Format:
      [ [1,1,0,0], [1,1,1,1], [1,1,1,1], [1,1,1,1] ]

  To use it normally just run the script.

  However to use it effienctly you can just make a file with your tables and
  use bash (or your equivalent) to pass the arguments in, like so:

    $ cat example_tables.txt | python pathfinder.py

"""

import sys

from ast import literal_eval # Important to safely parse user inputted data

def _cli():
    """CLI handles all the user interaction over the command line."""

    if '--verbose' in sys.argv: loud = True
    else: loud = False

    if '--help' in sys.argv:
        print(__doc__) # the beauty of docstrings in one line
    elif '--test' in sys.argv:
        _test(loud)
    else:
        _get_user_input(loud)

def _get_user_input(loud):
    running = True
    print 'CTRL-X or EOF to exit'

    prompt = "Enter your table like a pythonic data structure\n"
    while running:
        try:
            user_input = raw_input(prompt)
            table = literal_eval(user_input)
            print _nice_table(table)
            print 'Number of paths:', num_of_paths(table)
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
        except:
            print '\nInvalid string', user_input
            if loud:
                print sys.exc_info()
            print

def num_of_paths(table, num_rows=None, num_cols=None):
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
        if num_rows == None: num_rows = len(table[0])
        if num_cols == None: num_cols = len(table)
        value_table = [[ 0 for i in range(0, num_rows) ] for i in range(0, num_cols)]
        for cur_x in range(0, num_rows):
            if len(table[cur_x]) != num_rows:
                raise IndexError
            for cur_y in range(0, num_cols):
                left = cur_x - 1
                up   = cur_y - 1
                value = table[cur_y][cur_x]
                if type(value) is not int:
                    raise IndexError
                if value == 1:
                    new_value = 0
                    if left >= 0 and value_table[cur_y][left] is not 0:
                        new_value += value_table[cur_y][left]
                    if up >= 0 and value_table[up][cur_x] is not 0:
                        new_value += value_table[up][cur_x]
                    if cur_y == 0 and cur_x == 0:
                        new_value = 1
                    value_table[cur_y][cur_x] = new_value
        return value_table[num_cols-1][num_rows-1]
    except IndexError:
        return -1
    except TypeError:
        return -1

def _test(loud):
    """_test(loud): run unit tests on pathfinder

    If loud is true lots of stuff is printed.
    """
    if loud:
        print '\n', '~-'*15, '\n', '# Testing pathfinder.py', '\n','-~'*15

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
        value           = num_of_paths(list_to_test)
        if loud:
            print '\t',list_to_test, ' should be ', expected_value
            print '\t','num_of_paths returned', value, '\n'
        assert expected_value == value

    print '++ Tests passed'
    return 0

def _nice_table(t):
    out = '[\n'
    for v in t:
        out += '    ' + str(v) + '\n'
    return out + ']'

if __name__ == '__main__':
    try:
        _cli()
    except SystemExit:
        print ''
        sys.exit(0)
    except:
        print '\nSomething went wrong.. '
        print sys.exc_info()
        print 'Try running with --verbose'
