import pyxel
from sprite import Sprite

class Player(Sprite): 

    def __init__(self, img_bank, x_cor, y_cor, width, height):
        super().__init__(img_bank, x_cor, y_cor, width, height)
  
        self.velocity = 1

    def set_velocity(self, velocity):
        self.velocity = velocity

    def move_left(self):
        self.x -= self.velocity
    
    def move_right(self):
        self.x += self.velocity

    def move_up(self):
        self.y -= self.velocity

    def move_down(self):
        self.y += self.velocity










        