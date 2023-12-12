from .node import *
from queue import Queue

QUEUE = Queue(0)  # queue for a* search with global access

"""
Initializes a specific infinite queue by inserting the root 
"""
def initialize_queue(root: Node) -> None:
    QUEUE.put(root)

"""
Implements search algorithm specified by import.
Returns the first found node with board configuration
- no blue tokens exist (part A implementation)
"""
def search_algo(node:Node) -> Node:

    assert node is not None
    initialize_queue(node)

    while not QUEUE.empty():

        cur = QUEUE.get()

        # seprates the dictionary of token positions by color 
        red, blue = sep_red_blue(cur.board)
         
        # win condition 
        if len(blue) == 0:
            return cur

        # expand node
        for redToken in red:
            gen_childNode(cur, redToken[COORDINATE], blue)  

"""
Function that expands a parent node to all possible child nodes.
parameter 'blueHex' is unused, exists for other implementations.
"""        
def gen_childNode(node: Node, focus: tuple, blueHex):

    for dir in range(len(DIRECTION)):
        child = Node(spread(node.board, focus, dir), node, focus + DIRECTION[dir])
        QUEUE.put(child)
     
