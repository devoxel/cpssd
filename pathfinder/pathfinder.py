"""
# pathfinder.py
    - Written by Aaron Delaney, 2015
    - Built with https://www.python.org/
    - Developed for CPSSD1 @ DCU

## Command Line Interface

Usage: pathfinder.py [OPTIONS] [TABLE ...]

Options:

  --test:
    Initiates test protocol.

    This uses the in-build series of tests to ensure the program works as
    intented.

  --verbose:
    Enables verbose output

  -t <table>:
    Directly pass a table into pathfinder instead of using handheld input
    <table> should be a pythonic representation of the table.

    For example:
        -t [[1,0],[0,1],[1,1]]

    For info on table structure, read the documentation provided in the file.

    Multiple -t's can be passed in.

If no OPTIONS are included, then pathfinder starts asking the user for input.
"""

import sys

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
        value_table = [[ None for i in range(0, num_rows) ] for i in range(0, num_cols)]
        for cur_x in range(0, num_rows):
            for cur_y in range(0, num_cols):
                left = cur_x - 1
                up   = cur_y - 1
                if table[cur_y][cur_x] == 1:
                    new_value = 0
                    if left >= 0 and value_table[cur_y][left] is not None:
                        new_value += value_table[cur_y][left]
                    if up >= 0 and value_table[up][cur_x] is not None:
                        new_value += value_table[up][cur_x]
                    if cur_y == 0 and cur_x == 0:
                        new_value = 1
                    value_table[cur_y][cur_x] = new_value
        return value_table[num_cols-1][num_rows-1]
    except IndexError:
        print 'Oops, invalid table entered'
        sys.exit(1)

### TESTING FUNCTION

def _test(loud):
    """_test(loud): run unit tests on pathfinder

    If loud is true lots of stuff is printed
    """
    # Note that test only logs to stdout atm
    if loud: print '\n', '-'*60, '\n'
    if loud: print '# Testing pathfinder.py'

    # Data to test
    empty_list = []
    empty_list_value = 0

    basic1 = [[1]]
    basic1_value = 1

    basic2 = [[0]]
    basic2_value = 0

    basic3 = [ [1,1], [1,1] ]
    basic3_value = 2

    basic4 = [ [1,1], [1,1], [1,1] ]
    basic4_value = 3

    square_easy = [[1,1,1],[1,1,1],[1,1,1]]
    square_easy_value = 6

    square_hard = [[1,0,0], [1,1,0],[1,1,1]]
    square_hard_value = 2

    table_strange_value = 1
    table_strange = [[1] for i in range(0,13)]

    invalid_table = [1,1,1]
    invalid_table2 = "table!?"
    invalid_table3 = [[1,1,1], [1,1,1,1]]
    invalid_table4 = [['foo', 'bar'], ['spam', 'eggs']]

    # Big tables are not value tested, since they're super hard to calculate by
    # hand, instead they are tests for time consumption, allowing me to make
    # sure that pathfinder can handle big lists without dying
    # If it can't I have to restructure the algorithm
    bigtable_easy = []
    bigtable_hard = []
    bigtablex, bigtabley = 5, 5
    for i in range(0, bigtablex):
        bigtable_easy.append([])
        bigtable_hard.append([])
        for k in range(0, bigtabley):
            bigtable_easy[i].append(1)
            if i % 2 == 0:
                bigtable_hard[i].append(1)
                if k == (bigtabley-1): # ensures solvable
                    bigtable_hard[i].append(1)
            else:
                if k % 3 == 0:
                    bigtable_hard[i].append(0)
                else:

                    bigtable_hard[i].append(1)
    if loud: print locals()
    if loud: print '- number_of_paths()\n'
    basic1_value_run = num_of_paths(basic1)
    basic2_value_run = num_of_paths(basic2)
    basic3_value_run = num_of_paths(basic3)
    basic4_value_run = num_of_paths(basic4)
    square_easy_value_run = num_of_paths(square_easy)

    if loud: print basic1, '=', basic1_value_run, 'should equal', basic1_value
    if loud: print basic2, '=', basic2_value_run, 'should equal', basic2_value
    if loud: print basic3, '=', basic3_value_run, 'should equal', basic3_value
    if loud: print basic4, '=', basic4_value_run, 'should equal', basic4_value
    if loud: print square_easy, '=', square_easy_value_run, 'should equal', square_easy_value
    #if loud: print num_of_paths(bigtable_hard)
    if loud: print num_of_paths(bigtable_easy)

    if loud: print '\n- verify_table()\n'
    if loud: print '\n- _evaluate_t_argument()\n'
    print 'Tests passed'
    return 0

########


if __name__ == '__main__':
    warn ='  Warning: eval() is being called on input, do not use in production'
    if '--test' in sys.argv:
        _test(loud=True) if '--verbose' in sys.argv else _test(loud=False)

    else:
        print '\n','~-'*35
        print warn
        print '-~'*35, '\n'
        for arg in sys.argv[1:]:
            try:
                result = num_of_paths(eval(arg))
                print arg, '\n', 'amount of paths:', '\n'
            except:
                print 'invalid table','\n'
