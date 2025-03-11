import pyxel

class Map:
    def __init__(self, height, width, transparent_tile, wall_tile, coin_tile):
        self.height = height
        self.width = width        
        self.transparent_tile = transparent_tile
        self.wall_tile = wall_tile
        self.coin_tile = coin_tile

    def check_collision(self, x, y):
        x1 = pyxel.floor(x) // 8
        y1 = pyxel.floor(y) // 8
        x2 = (pyxel.ceil(x) + 7) // 8
        y2 = (pyxel.ceil(y) + 7) // 8
    

        for yi in range(y1, y2 + 1):
            for xi in range(x1, x2 + 1):
                tile = pyxel.tilemaps[0].pget(xi, yi)
                if tile == self.coin_tile:
                    # change tile to background color, 'hide' tile
                    pyxel.tilemap(0).pset(xi, yi, self.transparent_tile)
                    return "coin"
                
                elif tile == self.wall_tile:
                    return "wall"
                
        return False
    
    def draw(self):
        # draw level  (x, y, tm, u, v, w, h)
        pyxel.bltm(0, 0, 0, 0, 0, self.height, self.width)

        


      