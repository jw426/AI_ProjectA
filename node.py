DIRECTION = [(0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0)]    # hex direction of the action

BOARD_SIZE = 7                                                      # size of hexagonally tiled board 
MAX_POWER = BOARD_SIZE - 1                                          # max power for a token stack 
COLOR = 0                                                           # index indicating color of token
POWER = 1                                                           # index indicating power of token
RED = 'r'
BLUE = 'b'
COORDINATE = 0
TOKEN = 1
R = 0
Q = 1

"""
Class to contain static variable: # nodes generated for search 
"""
class NumNode:
    i = 0
    def __init__(self):
        NumNode.i = NumNode.i + 1

"""
Node class that contains information on possibilities of game play 
"""
class Node:

    def __init__(self, board: dict[tuple, tuple], parent=None, move=None):
        
        self.board = board
        self.parent = parent
        self.move = move # action tuple of (r, q, dr, dq) coordinates
        self.h = 0 # default 0 until calculation

        # numMove: g(n) - # moves taken so far
        if parent is not None:
            self.numMove = parent.numMove + 1
        else: 
            self.numMove = 0

        # to count number of nodes generated
        # can be commented (optional)
        NumNode()

    # h: h(n) - admissible heuristic value 
    def h_n(self, h) -> None:
        self.h = h

    def __eq__(self, other) -> int:
        return (self.h + self.numMove == other.h + other.numMove)    

    # comparison function for pq
    def __lt__(self, other) -> int:
        return (self.h + self.numMove < other.h + other.numMove)

"""
Accepts coordinate (r, q) and moves it in the direction specified.
Returns a valid coordinate (r', q')
"""
def move_step(orig: tuple, dir: int) -> tuple:
    
    x, y = orig
    delta_x, delta_y = DIRECTION[dir]
    return ((x + delta_x) % BOARD_SIZE, (y + delta_y) % BOARD_SIZE)

"""
Function that implements SPREAD starting from position 'orig' in direction 'dir'.
Returns the board configuration after the SPREAD movement. 
"""
def spread(board: dict[tuple, tuple], orig: tuple, dir: int) -> dict[tuple, tuple]:

    assert orig in board

    new_board = board.copy()

    control = orig # currently controlling cell
    control_color = board[orig][COLOR] 
    # optional: part A implementation
    assert (control_color == 'r')

    for n in range(new_board[orig][POWER]):

        control = move_step(control, dir)

        # CASE 1: cell not empty 
        if control in new_board:
            # CASE 1-1: token has value above max power and disappears
            if new_board[control][POWER] == MAX_POWER:
                del new_board[control]    
            # CASE 1-1: token stack       
            else: new_board[control] = (control_color, int(new_board[control][POWER]) + 1)
        # CASE 2: cell empty 
        else: 
            new_board[control] = (control_color, 1)

    # empty original token
    del new_board[orig]

    return new_board

"""
Function that splits the dictionary of tokens by color. 
Returns two lists that contain dictionary key, value pair 
of board composition with same color.  
"""
def sep_red_blue(board: dict[tuple, tuple]):

    red = []
    blue = []
    for pos, token in board.items():
        if token[COLOR] == RED:
            red.append((pos, token))
        elif token[COLOR] == BLUE:
            blue.append((pos, token))

    return red, blue