import pygame

class InputHandler:
    def __init__(self):
        self.keys = {}

    def update(self):
        self.keys = pygame.key.get_pressed()

    def getKeys(self):
        return self.keys

    def getKey(self, key):
        return self.keys[key]