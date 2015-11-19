"""
- Author:  Aaron Delaney
- Email:   aaron.delaney29@mail.dcu.ie
- Developed for CPSSD1 @ DCU
- Last Worked on the file: 19/11/2015
"""
import sys
import traceback


def cli():
    """Capture command line input from the user"""
    verbose = "--verbose" in sys.argv
    prompt = "How many pegs does your board have on each side?: "
    while True:
        try:
            print "\nPress CTRL+C to exit"
            amount_of_pegs = abs(int(raw_input(prompt)))
            pegboard = Pegboard(amount_of_pegs)
            moves = pegboard.solve()
            write_output(moves)
        except KeyboardInterrupt:
            print "\nBye bye!\n"
            sys.exit(0)
        except:
            if verbose:
                print "\n", traceback.format_exc()
            print 'Error with your input, make sure it is of type int'


def write_output(moves):
    """Write the output of Pegboard.solve() to the user"""
    # Note -1 is here to remove the starting position
    total_moves = "\nOverall Moves: " + str(len(moves) - 1)
    if len(moves[0]) > 79:
        print "Very large data, so saving to a file instead"
        print "Find the file in results.txt"
        with open("results.txt", "w") as f:
            f.writelines(moves)
            f.write(total_moves)
    else:
        for move in moves:
            print move,  # comma is here because \n are in return values
        print total_moves

class Peg(object):
    """ Represents a Peg in the pegboard, of a certain type.

    Pegs are defined by sign, so black pegs are +1 and white pegs are -1.
    Or rather, pegs on the left are positive and pegs on the right are negative.

    This was chosen because it is the goal of pegs on the left to move right,
    or positivly through the pegboard, and conversly, it is the goal if the
    pegs on the right to move left.

    Sign is either +1 or -1

    ### Methods:
    - obj.move()
        Iterates the times_moved property

    ### Properties:
    - obj.times_moved

       The amount of times the peg was moved.
       since optimizations are in place to select pegs that were moved the
       least, the times_moved variable is neccessary.
    """
    def __init__(self, numerical_sign):
        self.direction = numerical_sign  # pegs should never go backwards
        self.times_moved = 1

    def move(self):
        """Iterates the times_moved property"""
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
    """Represents a space in the pegboard"""
    def __init__(self):
        # this is done so the peg is always the *last* peg that is moved
        # float("inf") always equals true for greater than tests
        self.times_moved = float("inf")
        self.direction = None

    def __repr__(self):
        return " "


class Pegboard(object):
    """ Represents the pegboard

    ### Properties:
    - size
       represents the amount of pegs of one type of the pegboard

    ### Methods:
    - obj.generate_pegboard()

       Used internally to generate the initial pegboard
    - obj.solve()

       Returns the moves needed to transpose the pegboard with min time
    - obj.move_peg(n)

       Used internally to to move the peg at position n
    - obj.check_move(pegboard_copy, peg, moved_from, moved_to)
    -
       Used to make sure a move is optimal. See the method for more details.
    - obj.solved() -

       Returns True if the pegboard is transposed
    """
    def __init__(self, n):
        self.size = n
        self.generate_pegboard()

    def generate_pegboard(self):
        """Used to generate the initial pegboard"""
        self.pegboard = []

        for i in range((self.size * 2) + 1):
            if self.size - i == 0:
                self.pegboard.append(PegSpace())
            elif self.size - i > 0:
                self.pegboard.append(Peg(1))
            else:
                self.pegboard.append(Peg(-1))

    def solve(self):
        """ Returns the moves needed to transpose the pegboard with min time

        Return value is a list where each item a string of each move in order.

        **Algorithm in English**

        Sort the pegs by how often they were moved. If we don't do this step,
        the pegs may organize themselves such that they end up in a situation
        where they are forced to move backwards. Since this is the opposite of
        what we want, we make sure to do this.

        sFrom right to left, try to move the peg.

        If the peg jumped over the peg of the same type, and reject the move.
        If the peg is adjacent to a peg of the same type, and the pegs are not
        touching an edge as a unit, reject the move.

        These moves are rejected because we never want to have to move the pegs
        backwards.

        **Note on representation of pegs**

        Pegs have their own Peg objects, which rely on signs. See the Peg
        object documentation for more details.
        """
        pegboard_moves = []
        while self.solved() == False:
            pegboard_moves.append(str(self) + "\n")
            # Sorting by least moved, so we don't move something at an incorrect time
            possible_pegs = sorted(self.pegboard, key=lambda x: x.times_moved)
            for peg in possible_pegs:
                move = self.move_peg(peg)
                if move is not None:
                    self.pegboard = move
                    peg.move()
                    break
        pegboard_moves.append(str(self) + "\n")
        return pegboard_moves

    def move_peg(self, peg):
        """Attempt to move a Peg object

        Returns None if move does not match move criteria or is invalid
        Returns with a copy of the new pegboard if the move is valid
        """
        # this copys the list, so we don't move the pegboard in place
        pos = self.pegboard.index(peg)
        pegboard_copy = self.pegboard[:]
        direction = peg.direction

        if peg.direction is None:
            return None  # trying to move a space, which doesn't make sense

        move_position = pos + direction
        jump_position = pos + (2 * direction)

        if move_position < 0 or move_position > len(pegboard_copy):
            return None
        if pegboard_copy[move_position].direction == None:
            pegboard_copy[pos] = self.pegboard[move_position]
            pegboard_copy[move_position] = peg
            return self.check_move(pegboard_copy, peg, pos, move_position)

        if jump_position < 0 or jump_position > len(pegboard_copy):
            return None
        if pegboard_copy[jump_position].direction == None:
            pegboard_copy[pos] = self.pegboard[jump_position]
            pegboard_copy[jump_position] = peg
            return self.check_move(pegboard_copy, peg, pos, jump_position)

        return None  # Peg can't move anywhere, so None

    def check_move(self, pegboard_copy, peg, moved_from, moved_to):
        """ This method makes sure a move is optimal.

        If the peg jumped over the peg of the same type, and reject the move.
        If the peg is adjacent to a peg of the same type, and the pegs are not
        touching an edge as a unit, reject the move.
        """
        if moved_to <= 0 or moved_to >= len(pegboard_copy) - 1:  # hit an edge
            return pegboard_copy
        elif moved_from + peg.direction == moved_to:  # moved straight forward
            if pegboard_copy[moved_to + peg.direction].direction != peg.direction:
                return pegboard_copy
        else:  # jumped
            if pegboard_copy[moved_from + peg.direction].direction == peg.direction:
                return None  # can't jump over a peg of the same type
            elif pegboard_copy[moved_to + peg.direction].direction != peg.direction:
                return pegboard_copy

        if peg.direction == 1:
            for i in range(moved_to, len(pegboard_copy)):
                if pegboard_copy[i].direction != 1:
                    return None
        elif peg.direction == -1:
            for i in range(moved_to - 1, 0, -1):
                if pegboard_copy[i].direction != -1:
                    return None

        return pegboard_copy

    def solved(self):
        """Returns True if the pegboard is transposed"""
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
