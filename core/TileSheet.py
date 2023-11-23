import pygame

# Tilesheet
class TileSheet:
    def __init__(self, filename, tile_size):
        self.tile_size = tile_size
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.tiles = []
        self.load_tiles()
        
    def load_tiles(self):
        for y in range(0, self.sheet.get_height(), self.tile_size):
            for x in range(0, self.sheet.get_width(), self.tile_size):
                self.tiles.append(self.sheet.subsurface(x, y, self.tile_size, self.tile_size))
                
    def get_tile(self, index):
        return self.tiles[index]
    
    def get_tile_size(self):
        return self.tile_size
    
    def get_tile_amount(self):
        return len(self.tiles)
    
    def get_tile_sheet(self):
        return self.sheet