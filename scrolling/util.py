import random
from graphics import *
# The size of the level (in tiles)
LEVEL_WIDTH = 50
LEVEL_HEIGHT = 50

# The size of the viewport (in tiles)
VIEWPORT_WIDTH = 21
VIEWPORT_HEIGHT = 21   

# The size of the window (in pixels)
TILE_SIZE = 24
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

def screen_pos_index (x,px,y, py):
    (wx, wy) = level_to_window(x,px,y,py)
    sx = wx*TILE_SIZE
    sy = wy*TILE_SIZE
    return sx,sy

def level_to_window(x,px,y, py):
    wx = x-px+10
    wy = y-py+10
    return wx,wy

def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a

# The representation of data in the level array
# 0 empty   (player can be on this)
# 1 grass   (player can be on this)
# 2 tree    (player cannot be on this)


def create_random_level ():
    level = make2dList(50,50)
    # level = [0] * 2500
    for i in range(100):
        level[random.randint(0,49)][random.randint(0,49)] = 1
    for i in range(50):
        level[random.randint(0,49)][random.randint(0,49)] = 2
    return level



def create_screen (level,window,px,py):
    colors = {1:"green", 2:"brown", 0: "white"}
    for rows in range(py-10,py+11):
        if rows > 0 and rows < 50:
            for col in range(px-10, px+11):
                (sx,sy) = screen_pos_index(col,px,rows,py)
                if col > 0 and col < 50:
                    elt = Rectangle(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE))
                    elt.setFill(colors[level[rows][col]])
                    elt.setOutline(colors[level[rows][col]])
                else:
                    print sx, col
                    elt = Rectangle(Point(sx,0), Point(sx+TILE_SIZE, 20*TILE_SIZE))  
                    elt.setFill("black")
                elt.draw(window)                      
        else: 
            (sx,sy) = screen_pos_index(0,px,rows, py)
            elt = Rectangle(Point(0,sy), Point(20*TILE_SIZE+TILE_SIZE,sy+TILE_SIZE))
            elt.setFill("black")
            elt.draw(window)


# A simple class to register a "checking input from the player" event

MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}
