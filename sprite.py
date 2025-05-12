import pyxel
import helpers

class Sprite:
    def __init__(self, img_bank, u, w, width, height, scale = 1):
        self.img_bank = img_bank
        self.width = width
        self.height = height
        self.u = u
        self.w = w
        self.scale = scale
        self.x = 0
        self.y = 0

    
    def set_xy(self, x, y):
        '''Set x,y position'''

        self.x = x
        self.y = y

    def draw(self):
        '''Draw Sprite at current location'''

        pyxel.blt(
            self.x, 
            self.y, 
            self.img_bank, 
            self.u, 
            self.w, 
            self.width, 
            self.height, 
            colkey=helpers.COLKEY,
            scale = self.scale)

    def is_colliding(self, x, y, tile):
        '''Checks if Sprite is colliding with a specific tile'''

        # Calculate the tile range based on the sprite's width and height
        x1 = pyxel.floor(x) // 8
        y1 = pyxel.floor(y) // 8
        x2 = pyxel.floor(x + self.width - 1) // 8
        y2 = pyxel.floor(y + self.height - 1) // 8

        # Check for collisions within the tile range
        for yi in range(y1, y2 + 1):
            for xi in range(x1, x2 + 1):
                if helpers.get_tile(xi, yi) == tile:
                    return True

        return False

    def collides_with(self, other_sprite):
        '''Check is self Sprite collides with another Sprite'''

        return (
            self.x < other_sprite.x + other_sprite.width and
            self.x + self.width > other_sprite.x and
            self.y < other_sprite.y + other_sprite.height and
            self.y + self.height > other_sprite.y
        )
    





