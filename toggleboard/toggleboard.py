"""

toggleboard.py
- Written by Aaron Delaney for CPPSD1 Practicium Mandatory Assignment 3
- For instructions see ./README.txt or ./README.html
- ASCII Text generated on http://patorjk.com/software/taag/

## Basic Design

The game uses a couple of important classes

- Constants handles most game data and is initalized globally
 as constants

- GridPoint is an x,y type object. For exmample:
      gp = GridPoint(10,11)
      gp.x - gp.y
      > -1
  It also has some helper methods and overloads adding and printing.
  I use it for sizes also, so I can access the sizes with x and y

- InputManager handles all input. Ensure constants.InputType is set correctly

- Board is an important class that handles point flipping and knowing when the
  board is done. Go read it to understand!

- Game contains the main game loop and error handling, as well as a nice 
  little easter egg: when you say oui to the first question, when you win 
  you get a queen song!

- smart_input is a sweet little function I wrote to handle input 
  by passing in some functions. It trys to transform the input and
  if it fails just asks again.
  I should write a better one that allows changing the context, 
  but it wasn't neccessary for this project

- Other stuff might be hanging around too, just check out the comments

"""

import os  # used for cross platform terminal clearing
import sys # used for special input, sys.exc_info() and sys.exit()

from time import sleep

class Constants(object):
    WelcomeMsg = """
      _                    _      _                         _
     | |                  | |    | |                       | |
     | |_ ___   __ _  __ _| | ___| |__   ___   __ _ _ __ __| |
     | __/ _ \ / _` |/ _` | |/ _ \ '_ \ / _ \ / _` | '__/ _` |
     | || (_) | (_| | (_| | |  __/ |_) | (_) | (_| | | | (_| |
      \__\___/ \__, |\__, |_|\___|_.__/ \___/ \__,_|_|  \__,_|
                __/ | __/ | ~~~ created by Aaron Delaney ~~~~
               |___/ |___/ ~~~~~ for CPPSD1 2015/2016 ~~~~~~~

     | press ctrl-C to quit | pass in --debug to see errors |
    """
    ControlUp = 'w'
    ControlDown = 's'
    ControlLeft = 'a'
    ControlRight = 'd'
    ControlFlip = 'e'
    Controls = [ControlUp, ControlDown, ControlLeft, ControlRight, ControlFlip]
    InputCoord = 'coord'
    InputWASD = 'wasd'
    InputTypes = [InputCoord, InputWASD]
    SelectedInput = InputCoord
    InputWASDPrompt = "w: up | a: left | s: down | d: right | e: flip\n"
    InputCoordPrompt = "(row, column) to co-ord: "
    debug = False
    Congrats = """
 _       __     ____         __                     __   __
| |     / /__  / / /  ____  / /___ ___  _____  ____/ /  / /
| | /| / / _ \/ / /  / __ \/ / __ `/ / / / _ \/ __  /  / / 
| |/ |/ /  __/ / /  / /_/ / / /_/ / /_/ /  __/ /_/ /  /_/  
|__/|__/\___/_/_/  / .___/_/\__,_/\__, /\___/\__,_/  (_)   
                  /_/            /____/                    
    """

# GLOBALS ALERT!! DANGER! BEWARE! WATCH OUT! CAREFUL! #

constants = Constants()

#######################################################

def clear_terminal():
    print '\n'*100
    return 0

def limit(n, biggest=24):
    return min(n, biggest)

def smart_input(prompt, transform_func=None, \
                error_message="Oops, bad input!", debug = False):
    """smart_input -> returns user input
    
    Arguments:
    - prompt: a string that's printed to prompt for input
    - transform_func: a reference to a function to call
      on the input. This method is called with one argument, the string
      the user inputs. Additional arguments can not be passed.        
    - error_message: string to print if the transform_func throws
      an error
    """
    value = raw_input(prompt)
    if transform_func is not None:
        # Since I want to be able to parse multiple 
        # transform functions, I will try to iterate
        # over it first. If it fails I'll try it as a
        # reference. This is an example of implicit duck programming
        #  (if it quacks like a duck)
        while True:
            try:
                for func in transform_func:                
                    value = func(value)
                break
            except TypeError, e:
                value = transform_func(value)
                if debug: 
                    print '> passed in single value to smart_input' 
                break
            except:
                print error_message
                if debug: print sys.exc_info()
                value = raw_input(prompt)
    if debug: print 'value taken as:\t', value    
    return value

class InputManager(object):
    """InputManager() -> Returns InputManager instance
    
    Important Methods:
        get_input() -> Gets user input based on what is set
         in constants.InputType

    Notes:
        Makes use of some fancy static-method stuff, including
        a nice little recursive input method. Read up on the
        @staticmethod directive for more information.
    """
    def get_input(self):
        """Gets user input based on what is set in constants.InputType"""
        if constants.SelectedInput == constants.InputWASD:
            return self._get_wasd_input()
        elif constants.SelectedInput == constants.InputCoord:
            return self._get_coord_input()    

    def _get_wasd_input(self):
        return smart_input(constants.InputWASDPrompt, \
                           self._validate_wasd_input, \
                           constants.debug)
    
    def _get_coord_input(self):
        return smart_input(constants.InputCoordPrompt, \
                           self._validate_coord, \
                           constants.debug)   
    @staticmethod    
    def _validate_coord(coord):
        coord = coord.strip('()')
        coord = coord.rsplit(',')
        coordx = int(coord[0])
        coordy = int(coord[1])
        if constants.debug == True:
            print '(X, Y)', coordx, coordy
            sleep(.5) # This allows it it to be read before rerender
        return GridPoint(coordx, coordy)

    @staticmethod
    def _validate_wasd_input(s):
        s = InputManager._process_wasd_input(s)
        if s == '':
            raise Exception
        else:
            return s

    @staticmethod
    def _process_wasd_input(s):
        """Recursive method of validating user input"""
        if len(s) == 0:
            return ''
        c = s[0].lower()
        if c in constants.Controls:
            return c + InputManager._process_wasd_input(s[1:])

class Game(object):
    """The Game Handler, used for Game.run()
    
    If the project grew more, it may be worth moving the Constants
    object to the Game object, so as to remove the global variable
    and make the Game object more useful. For now that's not neccesary.
    """
    def run(self):
        print constants.WelcomeMsg

        sizex = smart_input("size (x): ", 
                            transform_func=(int, abs, limit),
                            debug=constants.debug)
        sizey = smart_input("size (y): ", 
                            transform_func=(int, abs, limit), 
                            debug=constants.debug)
        size = GridPoint(sizex, sizey)

        game_board = Board(size)
        renderer = Renderer(game_board)
        input_manager = InputManager()

        easter_egg = raw_input("\nAre you ready to play? ").lower() == "oui"
        changed = True
        while True:
            if changed:
                renderer.render_board(game_board)
                changed = False
            try:
                user_input = input_manager.get_input()
                game_board.handle_input(user_input)
                changed = True
            except IndexError, e:
                if constants.debug: print e
                print "Oops, looks like your integer went out of bounds"
            except ValueError, e:
                if constants.debug: print e
                print "Oops, looks like you entered an invalid integer"
            except KeyboardInterrupt:
                print '\nSee ya!'
                sys.exit(-1)
            except:
                if constants.debug: print sys.exc_info()
                print 'What even was that input?'
            if game_board.finished():
                renderer.render_board(game_board) # Show them they're finished
                print 'Oh.. you won!'
                sleep(.5) # these sleep calls make the game feel fun
                print '...'
                sleep(2) # adding tension for the big finale
                if easter_egg:
                    print 'You found the easter egg! :)'
                    sleep(1)
                    import webbrowser
                    webbrowser.open("https://youtu.be/rY0WxgSXdEE?t=7")
                print constants.Congrats
                sys.exit(0)

class GridPoint(object):
    """GridPoint(x,y ) -> Return a GridPoint object

    A gridpoint encapsulates some useful methods and allows you to
    access the point with .x and .y 

    GridPoints also support addition, so:
        p1 + p2 = GridPoint(p1.x + p2.x, p1.y+p2.y)
    
    Print them normally, print p1
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adjacent_points(self):
        """Return the 4 adjacent grid points"""
        return  [GridPoint(self.x + 1, self.y),
                 GridPoint(self.x - 1, self.y),
                 GridPoint(self.x,     self.y + 1),
                 GridPoint(self.x,     self.y - 1)]

    def ongrid(self, size):
        """Returns true if the point is on a grid of size: size

        size should have an x and y componant.
        GridPoint.ongrid() assumes a zero indexed grid"""
        valid =  self.x >= 0 and self.x < size.x and \
                 self.y >= 0 and self.y < size.y
        return valid

    def __add__(self, other):
        return GridPoint(self.x+other.x, self.y+other.y)

    def __str__(self):
        return '( ' + str(self.x) + ', ' + str(self.y) + ')'

class Renderer(object):
    """Renderer(game_board) -> Renderer object
    
    Important Methods:
        generate_board(game_board) -> str :
          This does a nice render of the game board based on game
          positions
        render_board(board):
          Clears the terminal and prints the board to the screen
    """
    def __init__(self, game_board):
        self._header = self._make_vertical_header(game_board) + '\n'

    def generate_board(self, game_board):
        output = ''
        output += self._header
        for y in range(0, len(game_board.grid)):
            output += str(y) + ((3 - len(str(y)))*' ') + '|'
            for x in range(0, len(game_board.grid[y])):
                cell = game_board.grid[y][x]
                selected_cell = game_board.current_pos.x == x and \
                                game_board.current_pos.y == y
                if cell:
                    output += 'X'
                else:
                    output += '0'
                if selected_cell and not constants.SelectedInput == constants.InputCoord:
                    output += '< '
                else:
                    output += '  '
            output += '\n'
        return output

    def _make_vertical_header(self, game_board):
        """ Generate a nice looking header for the board """
        # this function is weird and I should make it better
        output = ""
        output += '    '
        for i in range(0, game_board.size.x):
            output += str(i) + (' ' * (3 - len(str(i))))
        output += '\n   ' + '---' * game_board.size.x
        return output

    def render_board(self, board):
        clear_terminal()
        print self.generate_board(board)

class Board(object):
    """A Board which holds the state of each cell, and provides
    useful methods to handle the state of the cells.

    Board(size) -> Returns Board Object:
     size must be a sequence-type object with two positive integers
     it defines the size of the board

    Instance Methods:
      Board.flip(pos):
        Flips the board position as per game rules
      Board.finished() -> Returns bool:
        Returns True if the game is complete, when all the grid-cells
        are true
      Board.handle_input(input):
        Handles user input elegently based on the type of game input
        defined in constants.InputType.
    """
    UpVector    = GridPoint(0, -1)
    DownVector  = GridPoint(0,  1)
    LeftVector  = GridPoint(-1, 0)
    RightVector = GridPoint(1,  0)
    def __init__(self, size):
        self.size = size
        self.grid = []
        self.current_pos = GridPoint(0, 0)
        # generate a grid like so: [row, row ...] | where row: [cell cell ...]
        for y in range(0, size.y):
            self.grid.append([])
            for x in range(0, size.x):
                self.grid[y].append(False)
        # these two variables will allow me to check if the game is finished
        self.total_cells = size.x * size.y
        self.total_toggled = 0 

    def handle_input(self, user_input):
        """"""
        if constants.debug: print 'handling: ', user_input
        if constants.SelectedInput == constants.InputWASD:
            if constants.debug: print 'input is wasd'
            self._handle_input_wasd(user_input)
        elif constants.SelectedInput == constants.InputCoord:
            if constants.debug: print 'input is coord'
            self._handle_input_coord(user_input)            
    
    def _handle_input_wasd(self, directions):
        for c in directions:
            self._process_single_input(c)

    def _handle_input_coord(self, coords):
        self.flip(coords)
        
    def _process_single_input(self, c):
        if c == constants.ControlUp:
            self.current_pos = self._push_current_pos(self.UpVector)
        elif c == constants.ControlDown:
            self.current_pos = self._push_current_pos(self.DownVector)
        elif c == constants.ControlLeft:
            self.current_pos = self._push_current_pos(self.LeftVector)
        elif c == constants.ControlRight:
            self.current_pos = self._push_current_pos(self.RightVector)
        elif c == constants.ControlFlip:
            self.flip()

    def _push_current_pos(self, direction):
        """ This method is some internal handling on position 
        movement. It essetially ensures the position doesn't
        escape the board boundries. 

        Note: it should only be called when InputWASD is the Input type
          (see constants.InputType)
        """
        new_pos = self.current_pos + direction
        if constants.debug: print new_pos
        if new_pos.ongrid(self.size):
            return new_pos
        else:
            return self.current_pos

    def flip(self, point=None):
        """flip(point):
        Flips the game board accordig the game rules
        Arugments:
         point must be a GridPoint object or referencable by 
         point.x and point.y
        """
        if constants.debug: print 'flipping ', point        
        if point == None:
            point = self.current_pos
        self.grid[point.y][point.x] = not self.grid[point.y][point.x]
        self._update_total_toggled(self.grid[point.y][point.x])
        for adj_point in point.adjacent_points():
            if adj_point.ongrid(self.size):
                self.grid[adj_point.y][adj_point.x] = \
                                 not self.grid[adj_point.y][adj_point.x]
                self._update_total_toggled(self.grid[adj_point.y][adj_point.x])

    def _update_total_toggled(self, cell):
        """Essential for knowing when the game is finished"""
        if cell:
            self.total_toggled += 1
        if not cell:
            self.total_toggled -= 1

    def finished(self):
        if self.total_toggled >= self.total_cells:
            return True
        else:
            return False

def test():
    """ Test some game fundementals"""
    print '\tEntered testing'
    print '\t-- Testing Input Things'
    assert clear_terminal() == 0
    smart_input('PROMPT: ', len, 'ERROR!', True)

    print '\t-- Testing Board Win Conditions and render'
    game_board = Board(GridPoint(3,3))
    renderer = Renderer(game_board)
    input_manager = InputManager()
    user_input = 'esseddewwease' # should always win a 3*3 game
    game_board.handle_input(user_input)
    assert game_board.finished() == True
    print 'Initial testing complete, do try more stuff though! :)'
    sys.exit(0)

if __name__ == "__main__":
    clear_terminal()
    if len(sys.argv) > 1:
        if '--test' in sys.argv:
            constants.debug = True
            constants.SelectedInput = constants.InputWASD
            test()
        if '--debug' in sys.argv:
            constants.debug = True
        if '--control-coord' in sys.argv:
            constants.SelectedInput = constants.InputCoord
        elif '--control-wasd' in sys.argv:
            constants.SelectedInput = constants.InputWASD 
    game = Game()
    game.run()
