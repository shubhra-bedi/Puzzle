""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\\nefgh\\nijkl\\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' if player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """

    if player_one_turn:
        return P1
    else:
        return P2
    
def get_winner(score_player_one: int, score_player_two: int) -> int:
    """Return the player1 as the winner if it has a higher score than player2,
    return player2 if it has a higher score than player 1,return tie if both 
    have the same scores.
    
    >>>get_winner(25,20)
    'player 1 wins'
    >>>get_winner(20.25)
    'player 2 wins'
    >>>get_winner(25,25)
    'Tie'
    """
    if score_player_one > score_player_two:
        return P1_WINS
    elif score_player_two > score_player_one:
        return P2_WINS
    else:
        return TIE

def reverse(rev: str) -> str:
    """Return the reverse copy of the string
    
    >>>reverse('Shubhra')
    'Arhbuhs'
    >>>reverse('Bedi')
    'Ideb'
    """
    revs = rev[::-1]
    return revs

def get_row(puzzle: str, row_no: int) -> str:
    """Return the number of letters in the row related to the row number.
    >>>get_row('abcd\nefgh\n', 1)
    efgh
    >>>get_row('abcd\nefgh\nijkl\n', 2)
    ijkl
    
    """
    grl = get_row_length(puzzle)
    return puzzle[row_no + (grl * row_no): grl * (row_no + 1) + row_no]

def get_factor(fact: str)-> int:
    """Return the multiplicative factor associated with this direction.
    
    >>>get_factor(forward)
    1
    >>>get_factor(backward)
    3
    """
    if fact == 'forward':
        return FORWARD_FACTOR
    elif fact == 'down':
        return DOWN_FACTOR
    elif fact == 'backward':
        return BACKWARD_FACTOR
    else:
        return UP_FACTOR
    
def get_points(direct: str, no_left: int)-> int:
    """Return the number of points for a correct guess.
    
    >>>get_points('forward', 3)
    3
    >>>get_points('backward', 5)
    15
    """
    if no_left >= THRESHOLD:
        return THRESHOLD * get_factor(direct)
    elif 1 < no_left < 5:
        return (2 * THRESHOLD - 2) * get_factor(direct)
    else:
        return (2 * THRESHOLD - 1) * get_factor(direct) + BONUS
    
def check_guess(puzz: str, direc: str, gu: str, row_col_no: int, no: int)->int:
    """Return the number of points earned after guessing.
    
    >>>check_guess('abcd\nefgh\nijkl\n','DOWN','aei',0,5)
    20
    >>>check_guess('abcd\nefgh\nijkl\n','up','aei',0,5)
    0
    """
    if direc == 'FORWARD' or direc == 'forward':
        if contains(get_row(puzz, row_col_no), gu):
            result = get_points(direc, no)
            return result
        else:
            return 0
        
    elif direc == 'BACKWARD' or direc == 'backward':
        if contains(get_row(puzz, row_col_no), reverse(gu)):
            result = get_points(direc, no)
            return result
        else:
            return 0
        
    elif  direc == 'DOWN' or direc == 'down':
                if contains(get_column(puzz, row_col_no), gu):
                    result = get_points(direc, no)
                    return result
                else:
                    return 0
                
    elif direc == 'UP' or direc == 'up':
        if contains(get_column(puzz, row_col_no), reverse(gu)):
            result = get_points(direc, no)
            return result
        else:
            return 0
    
    else:
        return 0