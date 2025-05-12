import pyxel
import helpers
from sprite import Sprite

class Player(Sprite):
    def __init__(self, img_bank, u, w, width, height, scale = 1):
        super().__init__(img_bank, u, w, width, height), scale

        self.x = 0
        self.y = 0

        self.speed = 2

    def update(self):
        original_x = self.x
        original_y = self.y

        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed

        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed
        
        elif pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed

        if self.is_colliding(self.x, self.y, helpers.WALL_TILE):
            self.set_xy(original_x,original_y)




