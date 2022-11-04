import numpy as np
ACTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
class Maze(object):
    def __init__(self):
        self.maze = np.zeroes((6, 6))
        self.maze[0, 0] = 2
        self.maze[5, :5] = 1
        self.maze[:4, 5] = 1
        self.maze[2, 2:] = 1
        self.maze[3, 2] = 1
        self.robot_position = (0, 0) # current robot position
        self.steps = 0 # contains num steps robot took
        self.allowed_states = None # for now, this is none
        self.construct_allowed_states() # not implemented yet

def is_allowed_move(self, state, action):
    y, x = state
    y += ACTIONS[action][0]
    x += ACTIONS[action][1]
    # moving off the board
    if y < 0 or x < 0 or y > 5 or x > 5:
         return False
    # moving into start position or empty space
    if self.maze[y, x] == 0 or self.maze[y, x] == 2:
        return True
    else:
        return False
def construct_allowed_states(self):
    allowed_states = {}
    for y, row in enumerate(self.maze):
        for x, col in enumerate(row):
            # iterate through all valid spaces
            if self.maze[(y,x)] != 1:
                allowed_states[(y,x)] = []
                for action in ACTIONS:
                    if self.is_allowed_move((y, x), action):
                        allowed_states[(y,x)].append(action)
    self.allowed_states = allowed_states

def update_maze(self, action):
    y, x = self.robot_position
    self.maze[y, x] = 0 # set the current position to empty
    y += ACTIONS[action][0]
    x += ACTIONS[action][1]
    self.robot_position = (y, x)
    self.maze[y, x] = 2
    self.steps += 1
    
def is_game_over(self):
    if self.robot_position == (5, 5):
        return True
    return False