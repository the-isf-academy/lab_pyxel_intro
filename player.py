import pyxel
from sprite import Sprite

class Player(Sprite): 

    def __init__(self, img_bank, x_cor, y_cor, width, height):
        super().__init__(img_bank, x_cor, y_cor, width, height)
  
        self.x_vel = 1
        self.y_vel= 1

        self.gravity = 0.5
        self.jump_strength = -10 
        self.on_ground = False

    def set_velocity(self, xVel, yVel):
        self.x_vel = xVel
        self.y_vel = yVel

    def move_left(self):
        self.x -= self.x_vel
    
    def move_right(self):
        self.x += self.x_vel

    def move_up(self):
        self.y -= self.y_vel

    def move_down(self):
        self.y += self.y_vel








        