from util import *
# Player is created by Player(x,y,window,level,scr)
#   where (x,y) is the initial position of the player
#   in the level, window is the window created by
#   GraphWin, level is the level array, and scr
#   is a data structure that holds whatever interesting elements
#   you've displayed on the screen in create_screen(), presumably.

class Player (object):
    def __init__ (self,x,y,window,level,scr):
        self._pic = "t_android.gif"    # this might be useful
        self._window = window  # you may not need all of these, but they're here anyway
        self._level = level
        self._screen = scr
        self._x = x
        self._y = y

    def move (self,dx,dy):
        # MOVE THE PLAYER BY (dx,dy)
        # calculate new position:
        tx = self._x + dx
        ty = self._y + dy
        # make sure you call this when there is movement so that the
        # window can refresh
        self._window.update()



