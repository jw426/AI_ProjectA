from .node import *
from queue import PriorityQueue

QUEUE = PriorityQueue(0)  # priority queue for a* search with global access
          
"""
Function that expands a parent node to all possible child nodes.
"""
def gen_childNode(node: Node, focus: tuple, blueHex) -> None:

    for dir in range(len(DIRECTION)):

        # generate childnode
        child = Node(spread(node.board, focus, dir), node, focus + DIRECTION[dir])
        
        # calculate the heuristic h_n for child node on expansion
        child.h_n(heuristic(child, blueHex))

        # insert into priority queue
        QUEUE.put(child)



"""
The following code was taken and modified from: 
https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/solutions/2062141/java-c-python-compare-slopes-cross-product/
on March 24th, 2023.
Title: "Minimum Lines to Represent a Line Chart"
Application: 
- provide admissible heuristic function h(n) for A* search
- returns minimum number of straight lines that cross all blue tokens 
"""
def heuristic(node: Node, blue) -> int:
        
    n = len(blue)
    numLines = n - 1
    blueTokens = sorted(blue, key = lambda x: blue[COORDINATE])
    for i in range(1, n - 1):
        a, b, c = blueTokens[i-1][COORDINATE], blueTokens[i][COORDINATE], blueTokens[i+1][COORDINATE]
        if (b[R] - a[R]) * (c[Q] - b[Q]) == (c[R] - b[R]) * (b[Q] - a[Q]):
            numLines -= 1
    
    return numLines


"""
Initializes a specific infinite queue by inserting the root 
"""
def initialize_queue(root: Node) -> None:
    QUEUE.put(root)

"""
Expand the parent node into possible child nodes. 
If parent node itself is the goal state, return parent node. 
"""
def expand(node: Node) -> Node:
    
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
Implements search algorithm specified by import.
Returns the first found node with board configuration
- no blue tokens exist (part A implementation)
"""
def search_algo(node:Node) -> Node:

    assert node is not None
    initialize_queue(node)

    cur = expand(node)

    while (not QUEUE.empty()):
        temp = QUEUE.get()
        if cur < temp: break
        comp = expand(temp)
        if comp < cur: cur = comp

    return cur