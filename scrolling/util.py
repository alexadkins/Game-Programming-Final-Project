import random
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



def create_screen (level,window,x,y):
    # WRITE ME: take a level description and a window
    # and initial tile coordingates (x,y) representing the tile in the 
    # level array to display smack in the middle of the
    # window, and fills in the window and presumably
    # returns something that you can use later on to
    # modify what's on the screen. (What that is is
    # up to you.)
    # 
    # You can use the create_screen function from
    # your Lode Runner game as inspiration
    pass


# A simple class to register a "checking input from the player" event

MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}
