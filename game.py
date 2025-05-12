######################
# a few helpful commands
#   - pyxel edit assets.pyxres (run in Terminal)
#   - press `esc` to quit game 
#   - pyxel.frame_count - returns current frame number 
######################

import pyxel
import helpers
from player import Player
from coin import Coin

class Game:
    def __init__(self):
        self.width = 128*2
        self.height = 128

        pyxel.init(self.width, self.height) 

        pyxel.load("assets.pyxres")  # loads sprites and map
        
        self.player = Player(
            img_bank=0, 
            u=24, 
            w=0, 
            width=8, 
            height=8)
        
        self.coin_list = []

        self.scene = "start"

        self.setup_map_sprites()

        pyxel.run(self.update, self.draw)

    def setup_map_sprites(self):
        '''Sets up Player and Coin Sprites based on the map'''

        for y in range(pyxel.tilemap(0).height):
            for x in range(pyxel.tilemap(0).width):
                tile = helpers.get_tile(x, y)

                if tile == helpers.PLAYER_TILE:
                    self.player.set_xy(x * 8, y * 8)   

                    for yi in range(y, y + (self.player.height // 8)):
                        for xi in range(x, x + (self.player.width // 8)):
                            pyxel.tilemap(0).pset(xi, yi, helpers.TRANSPARENT_TILE)
 
                if tile == helpers.COIN_TILE:
                    coin = Coin(
                        img_bank=0, 
                        u=32, 
                        w=0, 
                        width=8, 
                        height=8,
                        scale = .5
                    )

                    coin.set_xy(x * 8, y * 8)              
                    self.coin_list.append(coin)
                
                    pyxel.tilemap(0).pset(x, y, helpers.TRANSPARENT_TILE) 

    def draw(self):
        pyxel.cls(0)    # clears screen

        if self.scene == "start":
            self.draw_start_screen()

        elif self.scene == "play":
            self.draw_play()
    
    def draw_start_screen(self):
        '''Handles what is drawn on the start screen'''

        pyxel.rect(0, 0, self.width, self.height, helpers.NAVY)

        pyxel.text(
            x = helpers.center_text(f"SIMPLE MAZE GAME", self.width), 
            y = self.height//3, 
            s = f"SIMPLE MAZE GAME", 
            col = helpers.WHITE)  
        
        
        pyxel.text(
            x = helpers.center_text(f"SIMPLE MAZE GAME",self.width), 
            y = self.height//2, 
            s = f"--press enter--", 
            col = helpers.WHITE)

        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = "play"

    def draw_play(self):
        '''Handles what is drawn when the game is being played'''

        # draw background color
        pyxel.rect(x=0, y=0, w=self.width, h=self.height, col=helpers.NAVY)
    
        # draw map
        pyxel.bltm(
            x= 0, 
            y = 0, 
            tm = 0, 
            u = 0 , 
            v = 0, 
            w = self.width, 
            h = self.height, 
            colkey=helpers.COLKEY)

        self.player.draw()

        for coin in self.coin_list:
            if coin.is_active() == True:
                coin.draw()

    def update(self):
        '''Called every frame of the game'''
  
        self.player.update()

        for coin in self.coin_list:
            if self.player.collides_with(coin) and coin.is_active():
                coin.set_active(False)

Game()




