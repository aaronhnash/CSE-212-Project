from maze import maze
"""
A maze is defined as a list of lists.  The outer list
contains a representation of each row in the maze.  You can
assume that the maze will be square (same number of rows
and columns). The inner lists show what is in the maze:

0 = Wall (You can't go through this)
1 = Open Path (You can go through this)
2 = End (You want to get to this point to win)

See the Prove instructions for graphical representations of
the 2 test mazes defined below.

The 'is_end_maze' and the 'is_valid_move' functions are
already written for you.  These functions assume that the first
square in the maze is (0,0).  These functions also assume
that you can't leave the boundaries of the maze and that you 
can't visit the same square in the same path (no circles).

The 'curr_path' variable is a list of (x,y) tuples that 
represent the path we are currently on.  If you add a new position
to the path, make sure that you add the tuple to the list so that the
'is_valid_move' function works properly.

The goal is to implement the 'solve_maze' function to display
all paths to the end square using recursion.  When you find a path, 
then displaying will be as simple as 'print(curr_path)'.
"""

def is_end_maze(maze, x, y):
    """
    Helper function to determine if the (x,y) position is at 
    the end of the maze.
    """
    return maze[y][x] == 2

def is_valid_move(maze, curr_path, x, y):
    """
    Helper function to determine if the (x,y) position is a valid
    place to move given the size of the maze, the content of the maze,
    and the current path already traversed.
    """
    # Can't go outside of the maze boundary
    if x > len(maze[0])-1 or x < 0: # get the width
        return False
    if y > len(maze)-1 or y < 0: # get the height
        return False
    # Can't go through a wall
    if maze[y][x] == 0:
        return False
    # Can't go if we have already been there (don't go in circles)
    if (x,y) in curr_path:
        return False
    # Otherwise, we are good
    return True

def solve_maze(maze, x=0, y=0, curr_path=None):
    """
    Use recursion to print all paths that start at (0,0) and end at the
    'end' square.
    """
    # If this is the first time running the function, then we need
    # to initialize the curr_path list.
    #print("called")
    if curr_path is None:
        curr_path = []

    # Add your current move.
    curr_path.append((x,y))

    # Am I at the end?
    if is_end_maze(maze, x, y):
        print(curr_path)
        return
    

    if is_valid_move(maze,curr_path,x+1,y): # can I move positively to the right?

        solve_maze(maze, x+1, y, curr_path) # Take a step and test this move.
        curr_path.pop() # If this route didn't work out, then remove your most recent step from the current path!


    if is_valid_move(maze, curr_path, x-1, y): # can I love to the left?

        solve_maze(maze, x-1, y, curr_path)
        curr_path.pop() # Did I hit a dead end? Better take a step back


    if is_valid_move(maze, curr_path, x, y+1): # down?

        solve_maze(maze, x, y+1, curr_path)
        curr_path.pop() # Take a step back


    if is_valid_move(maze, curr_path, x, y-1): # up?

        solve_maze(maze, x, y-1, curr_path)
        curr_path.pop() # Take a step back

solve_maze(maze)

# Your terminal output should list coordinates like this:
"""
[(0, 0), (0, 1), (0, 2), (0, 3), 
(0, 4), (0, 5), (0, 6), (0, 7), 
(0, 8), (1, 8), (2, 8), (2, 9), 
(2, 10), (3, 10), (4, 10), (5, 10), 
(6, 10), (7, 10), (7, 9), (7, 8), 
(7, 7), (7, 6), (6, 6), (5, 6), 
(4, 6), (4, 5), (4, 4), (5, 4), 
(5, 3), (5, 2), (6, 2), (7, 2), 
(7, 3), (7, 4), (8, 4), (9, 4), 
(10, 4), (11, 4), (12, 4), (13, 4)]
"""




# Searching through a BST
"""
CSE 212 Lesson 9A

Implementation of a basic Binary Search Tree data structure.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
          self.root = BST.Node(data)
        else:
          self._insert(data, self.root)

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
          if node.left is None:
            node.left = BST.Node(data)
          else:
            self._insert(data, node.left)
            
        else:
          if node.right is None:
            node.right = BST.Node(data)
          else:
            self._insert(data, node.right)
         
    def __iter__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.           
        """
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
          yield from self._traverse_forward(node.left)
          yield node.data
          yield from self._traverse_forward(node.right)


    def contains(self, value):
        current_node = self.root
        found = self._search_bst(value, current_node)
        return found



    def _search_bst(self, value, curr):
        if curr == None:
            return False
        elif curr.data == value:
            return True
        elif curr.data > value:
            return self._search_bst(value, curr.left)
        elif curr.data < value:
            return self._search_bst(value, curr.right)



sample_bst = BST()
sample_bst.insert(50)
sample_bst.insert(20)
sample_bst.insert(65)
sample_bst.insert(13)
sample_bst.insert(35)
sample_bst.insert(60)
sample_bst.insert(70)
sample_bst.insert(11)
sample_bst.insert(17)
sample_bst.insert(45)
sample_bst.insert(57)
sample_bst.insert(64)
sample_bst.insert(72)


print(sample_bst.contains(35)) # Will be true
print(sample_bst.contains(72)) # Will be true
print(sample_bst.contains(83)) # will be false
print()