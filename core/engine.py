import pygame
import sys
import os, datetime
from core.GameObject import *
from core.SpriteManager import SpriteManager
from core.SoundManager import SoundManager
from core.logger import Logger

class Engine:
    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.blocks = [] # loads from .level file
        self._using_level = False
        
        # Creating System Objects
        self.sprite_manager = SpriteManager() # creates the sprite manager
        self.sound_manager = SoundManager() # creates the sound manager
        self.logger = Logger('log.txt') # creates the logger
        
        # Loading assets
        self.sprite_manager.load_sprites_from_folder("ASSETS") # loads all sprites from a folder
        self.sound_manager.load_sounds_from_folder("ASSETS") # loads all sounds from a folder
        
    def setTitle(self, title):
        pygame.display.set_caption(title)
        
    def fill(self, color):
        self.screen.fill(color)

    # Game loop functions
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                # log the current time
                self.logger.log(f"Game Closed at {str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
                pygame.quit()
                sys.exit()
            else:
                self.logger.log(str(event)) 
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # closes game
        if keys[pygame.K_ESCAPE]:
            self.running = False
    
    def update(self):
        print("update")
        
    def draw(self):
        # if the game is loading levels, draw the blocks
        if self._using_level:
            for block in self.blocks:
                block.draw(self.screen)
            
        pygame.display.flip()
        
    # loads the level from a file using a set of points
    def load_level(self, filename):
        if self._using_level:
            self.logger.log("Loading level from " + filename)
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    data = line.split(",")
                    x = int(data[0])
                    y = int(data[1])
                    width = int(data[2])
                    height = int(data[3])
                    color = (int(data[4]), int(data[5]), int(data[6]))
                    self.blocks.append(Rect(x, y, width, height, color))
        
    def run(self):
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update()
            self.draw()
            
            # count fps in game window title
            fps = int(self.clock.get_fps())
            self.setTitle("Game | fps: " + str(fps))

            self.clock.tick(60)