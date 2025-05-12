import pyxel

# pyxel color palette 
BLACK = 0
NAVY = 1
PURPLE = 2
GREEN = 3
BROWN = 4
GRAY_DARK = 5
GRAY_LIGHT = 6
WHITE = 7
RED = 8
ORANGE = 9
YELLOW = 10
LIME = 11
CYAN = 12
STEEL_BLUE = 13
PINK = 14
PEACH = 15

# map setup
COLKEY = BLACK
TRANSPARENT_TILE = (0,0)
WALL_TILE = (1,0)
COIN_TILE = (4,0)
PLAYER_TILE = (3,0)


def get_tile(tile_x, tile_y):
    return pyxel.tilemaps[0].pget(tile_x, tile_y)