class Maze:
    """
    Defines a maze using a dictionary.  The dictionary is provided by the
    user when the Maze object is created.  The dictionary will contain the
    following mapping:

    (x,y) : (left, right, up, down)

    'x' and 'y' are integers and represents locations in the maze.
    'left', 'right', 'up', and 'down' are boolean are represent valid directions

    If a direction is False, then we can assume there is a wall in that direction.
    If a direction is True, then we can proceed.  

    If there is a wall, then display "Can't go that way!".  If there is no wall,
    then the 'curr_x' and 'curr_y' values should be changed.
    """

    def __init__(self, maze_map : dict):
        """
        Initialize the map.  We assume that (1,1) is a valid location in
        the maze.
        """
        self.maze_map : dict = maze_map
        self.curr_x : int = 1
        self.curr_y : int = 1

    def move_left(self):
        """
        Check to see if you can move left.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        pos : tuple = (self.curr_x, self.curr_y)
        print(self.curr_x - 1, self.curr_y) if self.maze_map[pos][0] else print('Error')
        if self.maze_map[pos][0]:
            self.curr_x -= 1

    def move_right(self):
        """
        Check to see if you can move right.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """     
        pos : tuple = (self.curr_x, self.curr_y)
        print(self.curr_x + 1, self.curr_y) if self.maze_map[pos][1] else print('Error')
        if self.maze_map[pos][1]:
            self.curr_x += 1

    def move_up(self):
        """
        Check to see if you can move up.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        
        pos : tuple = (self.curr_x, self.curr_y)
        print(self.curr_x, self.curr_y + 1) if self.maze_map[pos][2] else print('Error')
        if self.maze_map[pos][2]:
            self.curr_y -= 1

    def move_down(self):
        """
        Check to see if you can move down.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        pos : tuple = (self.curr_x, self.curr_y)
        print(self.curr_x, self.curr_y - 1) if self.maze_map[pos][3] else print('Error')
        if self.maze_map[pos][3]:
            self.curr_y += 1
    
    def show_status(self):
        print("Current location (x={} , y={})".format(self.curr_x, self.curr_y))

# Sample Test Cases (may not be comprehensive) 
map =  {(1,1) : (False, True, False, True),
        (1,2) : (False, True, True, False),
        (1,3) : (False, False, False, False),
        (1,4) : (False, True, False, True),
        (1,5) : (False, False, True, True),
        (1,6) : (False, False, True, False),
        (2,1) : (True, False, False, True),
        (2,2) : (True, False, True, True),
        (2,3) : (False, False, True, True),
        (2,4) : (True, True, True, False),
        (2,5) : (False, False, False, False),
        (2,6) : (False, False, False, False),
        (3,1) : (False, False, False, False),
        (3,2) : (False, False, False, False),
        (3,3) : (False, False, False, False),
        (3,4) : (True, True, False, True), 
        (3,5) : (False, False, True, True),
        (3,6) : (False, False, True, False),
        (4,1) : (False, True, False, False),
        (4,2) : (False, False, False, False),
        (4,3) : (False, True, False, True),
        (4,4) : (True, True, True, False),
        (4,5) : (False, False, False, False),
        (4,6) : (False, False, False, False),
        (5,1) : (True, True, False, True),
        (5,2) : (False, False, True, True),
        (5,3) : (True, True, True, True),
        (5,4) : (True, False, True, True),
        (5,5) : (False, False, True, True),
        (5,6) : (False, True, True, False),
        (6,1) : (True, False, False, False),
        (6,2) : (False, False, False, False),
        (6,3) : (True, False, False, False),
        (6,4) : (False, False, False, False),
        (6,5) : (False, False, False, False),
        (6,6) : (True, False, False, False)}

print("\n=========== PROBLEM 4 TESTS ===========")
maze = Maze(map)
maze.show_status() # Should be at (1,1)
maze.move_up() # Error
maze.move_left() # Error
maze.move_right() 
maze.move_right() # Error
maze.move_down()
maze.move_down()
maze.move_down()
maze.move_right()
maze.move_right()
maze.move_up()
maze.move_right()
maze.move_down()
maze.move_left()
maze.move_down() # Error
maze.move_right()
maze.move_down()
maze.move_down()
maze.move_right()
maze.show_status() # Should be at (6,6)