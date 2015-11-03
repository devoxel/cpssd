"""
pathfinder.py
=============
- Written by Aaron Delaney, 2015
- Built with https://www.python.org/
- Developed for CPSSD1 @ DCU

Command Line Interface
----------------------

Usage: pathfinder.py [OPTIONS] [table_files ...]

Prints out the amount of paths in a table from the 
top left to the bottom right.

If no table_files are provided, pathfinder.py will enter an interactive
user mode.  

Options
-------

--help
    Print this help file

--test
    Initiates test protocol.

    This uses the in-build series of tests to ensure the program works as
    intended.

--verbose:
    Enables verbose output 

    Table Files
-----------

A table file is a file representing a table, or a series of tables. 

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
$ 1100
$ 1111
```
"""

import sys

def pathfinder_cli():
    """CLI interprets the arguments and options passed to pathfinder.py """
    
    verbose = False
    done_something = False

    # The first argument is always the filename, so ignore it
    for arg in sys.argv[1:]: 
        if arg == '--verbose': 
            verbose = True
        elif arg == '--help':
            # __doc__ refers to the docstring at the begining of the file
            print(__doc__)
            done_something = True        
        elif arg == '--test':
            test_pathfinder(verbose)
            done_something = True
        else:
            read_from_file(verbose, arg)    
    if not done_something: 
        interactive_input(verbose)


def read_from_file(verbose, filename):
    pass

def interactive_input(verbose):

    prompt = "\nEnter you table by simple writing a 0 for an unpassable tile\n" +\
             "or a 1 for an unpassable tile, as a string of integers\n" +\
             "To run the path finder on your table, enter a blank line\n" +\
             "\nNote that all invalid input will be taken as a blank line." +\
             "\nCTRL-X to exit\n" +\
             "\nBlank line for to run pathfinder\n"

    while True:
        table_entered = False
        table = []
        max_columns = 0
        print prompt
        while not table_entered:
            try:
                row = []
                user_input = raw_input()

                for c in user_input:
                    row.append(int(c))

                columns = max(len(row), max_columns)                

                if len(row) == 0:
                    table_entered = True
                else:
                    table.append(row)
            except KeyboardInterrupt:
                sys.exit(0)
            except EOFError:
                sys.exit(0)
            except:
                print '\nInvalid string', user_input
                if verbose:
                    print sys.exc_info()
                table_entered = True

        for row in table:
            if len(row) < max_columns:
                print 'nice maymay'
                for i in range(0, max_columns-len(row)):
                    row.append(0)
        
        print table
        if verbose: print _formatted_table(table)       
        print 'Number of paths:', num_of_paths(verbose, table)

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
        if verbose: 
            print 'Invalid indexed table, ie: unbalanced rows'
            print sys.exc_info()
        return -1
    except TypeError:
        if verbose: 
            print 'Passed in the wrong type of table'
            print sys.exc_info()
        return -1

def test_pathfinder(verbose):
    """_test(verbose): run unit tests on pathfinder

    If verbose is true lots of stuff is printed
    """
    if verbose:
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
        if verbose:
            print '\t',list_to_test, ' should be ', expected_value
            print '\t','num_of_paths returned', value, '\n'
        assert expected_value == value

    print '++ Tests passed'
    return 0

def _formatted_table(t):
    out = '[\n'
    for v in t:
        out += '    ' + str(v) + '\n'
    return out + ']'

if __name__ == '__main__':
    try:
        pathfinder_cli()
    except SystemExit:
        print ''
        sys.exit(0)
    except:
        print '\nSomething went wrong.. '
        print sys.exc_info()
        print 'Try running with --verbose'
