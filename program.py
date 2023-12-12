# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

# comment and uncomment imports depending on algorithm implementation
from .astar import *
#from .bfs import *             
from .utils import render_board


"""
The input is a dictionary of board cell states, where the keys are tuples of (r, q) coordinates, 
and the values are tuples of (p, k) cell states. 
The output is a list of actions where each action is a tuple of (r, q, dr, dq) coordinates.
"""     
def search(input: dict[tuple, tuple]) -> list[tuple]:

    root = Node(input)               # root for search tree  
    solution = search_algo(root)     # solution for search algorithm implemented 

    # record moves made to reach solution state 
    moves = []                      
    while (solution.move != None):   # traverse tree backwards to root
        moves.append(solution.move)
        solution = solution.parent

    # OPT) for space complexity
    #print("Number of Nodes", NumNode.i)

    return moves[::-1]          
