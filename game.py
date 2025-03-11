######################
# installation steps
# in the terminal run: pip3 install pyxel
######################

import pyxel
from player import Player
from sprite import Sprite
from map import Map

class Game:
    def __init__(self):
        pyxel.init(128, 128) # sets width and height

        pyxel.load("assets.pyxres")  # loads sprites and map

        self.player = Player(
            img_bank=0, 
            x_cor=0, 
            y_cor=24, 
            width=8, 
            height=8)
        
        self.player.set_xy(20,50)
        self.player.set_velocity(2)

        self.map = Map(
            128,
            128,
            transparent_tile = (0,0),
            wall_tile = (1,0),
            coin_tile = (4,0)
        )

        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.map.check_collision(self.player.x - self.player.velocity, self.player.y) != "wall":
                self.player.move_left()
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.map.check_collision(self.player.x + self.player.velocity, self.player.y) != "wall":
                self.player.move_right()
        if pyxel.btn(pyxel.KEY_UP):
            if self.map.check_collision(self.player.x, self.player.y - self.player.velocity) != "wall":
                self.player.move_up()
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.map.check_collision(self.player.x, self.player.y  + self.player.velocity) != "wall":
                self.player.move_down()        
    
    def draw(self):
        pyxel.cls(0)        #clears screen

        self.map.draw()
        self.player.draw()
        pyxel.text(80,0,"hello",5)

Game()




