# Introducing recursion!

def recursive_message_1(message):
    print(message)
    recursive_message_1(message)

#recursive_message_1("hello") # uncomment if you dare!


def recursive_message_2(message, count):
    count -=1
    if count >= 0:
        print(f"{message} {count}")
        recursive_message_2(message, count)

recursive_message_2("hello", 5)

print()

def recursive_message_3(message, count):
    count -=1
    if count >= 0:
        recursive_message_3(message, count)
        print(f"{message} {count}")

recursive_message_3("hello", 5)







# EXAMPLE 1: Recursion
from examples import maze

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
    if curr_path is None:
        curr_path = []
        #curr_path.append((x,y))


    # ADD CODE HERE   


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