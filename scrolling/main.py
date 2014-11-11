#
# Scrolling Demo
#
#

import time
from util import *
from graphics import *
from player import *
from queue import *
from checkinput import *


def main ():

    window = GraphWin("Scrolling Demo", 
                      WINDOW_WIDTH, WINDOW_HEIGHT,
                      autoflush=False)

    level = create_random_level()

    # initial "center" of the screen is (25,25) in the level array
    scr = create_screen(level,window,49,49)

    # player starts at (25,25) as well...
    p = Player(49,49,window,level,scr)

    q = EventQueue()

    q.enqueue(1,CheckInput(window,p))

    while True:
        q.dequeue_if_ready()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
