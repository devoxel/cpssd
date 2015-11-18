"""
- Written by Aaron Delaney, 2015
- Built with https://www.python.org/
- Developed for CPSSD1 @ DCU
- Last Worked on the file: 06/11/2015
_=
"""
import sys
import traceback

def cli():
    verbose = "--verbose" in sys.argv
    while True:
        try:
            print "\nPress CTRL+C to exit"
            amount_of_pegs = int(raw_input("How many pegs does your board have: "))
            pegboard = Pegboard(amount_of_pegs)
            pegboard.solve()
        except KeyboardInterrupt:
            print "\nBye bye!\n"
            sys.exit(0)
        except:
            if verbose: print "\n",traceback.format_exc()
            print 'Error with your input, make sure it is of type int'


def numerical_sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return None

class Peg(object):
    def __init__(self, numerical_sign):
        self.direction = numerical_sign # pegs should never go backwards
        self.times_moved = 1

    def move(self):
        self.times_moved += 1

    def __repr__(self):
        if self.direction == 1:
            return "+" + str(self.times_moved)
        else:
            return "-" + str(self.times_moved)

    def __str__(self):
        if self.direction == 1:
            return "+"
        else:
            return "-"

class PegSpace(object):
    def __init__(self):
        # this is done so the peg is always the *last* peg that is moved
        self.times_moved = float("inf")
        self.direction = None
    def __repr__(self):
        return " "

class Pegboard(object):
    def __init__(self, n):
        self.size = n
        self.generate_pegboard()

    def generate_pegboard(self):
        self.pegboard = []

        for i in range((self.size*2)+1):
            if self.size - i == 0:  self.pegboard.append( PegSpace() )
            elif self.size - i > 0: self.pegboard.append( Peg(1) )
            else: self.pegboard.append( Peg(-1) )

    def solve(self):
        while self.solved() == False:
            print self
            raw_input()
            possible_pegs = sorted(self.pegboard, key=lambda x: x.times_moved)
            for peg in possible_pegs:
                move = self.move_peg(peg)
                if move is not None:
                    print ".. moved @", self.pegboard.index(peg)
                    self.pegboard = move
                    peg.move()
                    break

    def move_peg(self, peg):
        # this copys the list, so we don't move the pegboard in place
        pos = self.pegboard.index(peg)
        pegboard_copy = self.pegboard[:]
        direction = peg.direction

        if peg.direction is None:
            return None # trying to move a space, which doesn't make sense

        move_position = pos + direction
        jump_position = pos + (2*direction)

        if pegboard_copy[move_position].direction == None:
            pegboard_copy[pos] = self.pegboard[move_position]
            pegboard_copy[move_position] = peg
            print pegboard_copy
            return self.check_move(pegboard_copy, peg, pos, move_position)

        elif pegboard_copy[jump_position].direction == None:
            pegboard_copy[pos] = self.pegboard[jump_position]
            pegboard_copy[jump_position] = peg
            return self.check_move(pegboard_copy, peg, pos, jump_position)

        return None # Peg can't move anywhere, so None

    def check_move(self, pegboard_copy, peg, moved_from, moved_to):
        """This method makes sure a move is optimal

        Optimal moves will never move the peg to a position in which it touches
        another peg of the same type, unless it's touching an edge.
        """
        if moved_to == 0 or moved_to == len(pegboard_copy):
            return pegboard_copy
        if pegboard_copy[moved_to - (moved_to-moved_from)].direction == peg.direction:
            return None
        if pegboard_copy[moved_to + (moved_from-moved_to)].direction != peg.direction:
            return pegboard_copy
        else:
            print "checking ", moved_from
            for i in range(2, moved_from+move):
                if pegboard_copy[moved_from + move + (i*peg.direction)].direction != peg.direction:
                    return None
            return pegboard_copy

    def solved(self):
        for i in range(self.size):
            if self.pegboard[i].direction != -1:
                return False
            if self.pegboard[self.size + i + 1].direction != 1:
                return False
        return True

    def __str__(self):
        s = "|"
        for peg in self.pegboard:
            s += str(peg)
            s += "|"
        return s

    def __repr__(self):
        s = "|"
        for peg in self.pegboard:
            s += repr(peg)
            s += "|"
        return s

if __name__ == "__main__":
    cli()
