from core.engine import Engine
from core.GameObject import GameObject, Circle, Rect, Line, Polygon, Text
from core.SpriteManager import SpriteManager
from player import Player

class Game(Engine):
    def __init__(self):
        super().__init__(800, 600, 'game') # Creates Game Window
        self.start() # Calls on game start
        self.player = Player(100,100)
            
    def start(self):
        self.logger.log('Game Started')
     
    def update(self):
        print("update") # remove this line
        self.player.move()
        
    def draw(self):
        self.fill("black") # fills the screen with a solid color to get rid of the previous frame
        
        # put code here
        self.player.draw(self.screen, self.sprite_manager.resize_sprite("player", (60,50)))
        
        super().draw() # Engine draws over everything else


game = Game()
game._using_level = False
game.load_level("levels/level.level")
game.run()