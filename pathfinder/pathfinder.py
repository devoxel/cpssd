"""
# pathfinder.py
    - Written by Aaron Delaney, 2015
    - Built with https://www.python.org/
    - Developed for CPSSD1 @ DCU

## Command Line Interface

Usage: pathfinder.py [OPTIONS]

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

from ast import literal_eval # parse python literals safetly

def on_table(point, rows, cols):
    x_on = point[0] < cols and point[0] >= 0
    y_on = point[1] < rows and point[1] >= 0
    return x_on or y_on

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
    The table should be accessed by table[row][col]
    """
    X, Y = 0, 1 # makes the code more readable
    if num_rows == None: num_rows = len(table)
    if num_cols == None: num_cols = len(table[0]) 
    
    num_paths = 0
    end_node  = (num_rows-1, num_cols-1)

    to_visit = [(0, 0)]
    visited = {}

    while True:
        if len(to_visit) == 0: 
             break

        visiting = to_visit.pop()
        print visiting
        if visiting == end_node:
            visited[visiting] = True
            num_paths += 1
        else:
            left = visiting[X] + 1, visiting[Y]
            down = visiting[X],     visiting[Y] + 1
            dead_end = True
            
            if left in visited:
                if visited[left] is True: 
                    num_paths += 1
                    visited[visiting] = True
            else:
                if on_table(left, num_rows, num_cols): 
                    if table[left[Y]][left[X]] == 1:
                        to_visit.append(left)
                    else:
                        visited[left] = False

            if down in visited: 
                if visited[down] is True:
                    num_paths += 1
                    visited[visiting] = True
            else:
                if on_table(down, num_rows, num_cols):
                    if table[down[Y]][down[X]] == 1:
                        to_visit.append(down)
                    else:
                        visited[down] = False

    return num_paths

def verify_table(l):
    """ Given l, test if it meets the requirements for a table.
    If the table is valid:
        return rows, columns
    If the table is invalid:
        return False

    Table Input Format
     [
       [1,1,0,0],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]
     ]
    """
    try:
        if not (type(l) is list):
            return False
        rows = len(l)
        if rows == 0:
            return False
        cols = len(l[0])
        for row in l:
            if len(row) != cols:
                return False
            for value in l:
                if value != 1 or value != 0:
                    return False
        return rows, cols
    except:
        return False

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

    table_strange = [[1] for i in range(0,13)]
    table_strange_value = 1

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
    bigtablex, bigtabley = 4, 4
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

    if loud: print _readable_dict(locals())
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

# helper functions to make loud testing easier

def _readable_dict(d):
    """Returns a readable string representation of a dictionary"""
    output = "\n"
    for key in d:
        value = d[key]
        if type(value) is list:
            output +=  str(key) + ': ' + _readable_list(value, prepend='  ') + '\n'
        else:
            output +=  str(key) + ': ' + str(value) + '\n\n'
    return output

def _readable_list(l, prepend=""):
    """Returns a readable string representation of a list

    Optional Arugments:
    - prepend: some text to prepend to each list
    """
    output = "[\n"
    for value in l:
        output += prepend + str(value) + ', \n'
    output += ']'
    return output

########

def _evaluate_t_argument():
    next_table = False
    for arg in sys.argv:
        if arg == '-t':
            next_table = True
        if next_table:
            table = verify_table(literal_eval(arg))
            rows, cols = table.len(), table[0]
            print arg, '\n\tpaths:', num_of_paths(table, rows, cols)

if __name__ == '__main__':
    if '--test' in sys.argv:
        _test(loud=True) if '--verbose' in sys.argv else _test(loud=False)

    if '-t' in sys.argv:
        _evaluate_t_argument()
