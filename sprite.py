import pyxel

class Sprite:
    def __init__(self, img_bank, y_cor, x_cor, width, height):
        self.img_bank = img_bank
        self.y_cor = x_cor
        self.x_cor = y_cor
        self.width = width
        self.height = height
        
        self.x = 0
        self.y = 0

        self.active = True
    
    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def set_active(self, bool):
        self.active = bool

    def draw(self):
        pyxel.blt(
            self.x, 
            self.y, 
            self.img_bank, 
            self.y_cor, 
            self.x_cor, 
            self.width, 
            self.height, 
            )
        
    def collide_sprite(self, other_sprite): 
        return abs(self.x - other_sprite.x) < 8 and abs(self.y - other_sprite.y) < 8
    
