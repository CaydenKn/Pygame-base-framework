import pygame
import os

class SpriteManager:
    def __init__(self):
        self.sprites = {}

    def load_sprites_from_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                name = os.path.splitext(filename)[0]
                image_path = os.path.join(folder_path, filename)
                image = pygame.image.load(image_path).convert_alpha()
                self.sprites[name] = image
                return print(f"Sprite loaded: {name}")
        return print("Not a valid path.")

    def get_sprite(self, name):
        return self.sprites.get(name, None)
    
    def resize_sprite(self, name, new_size):
        sprite = self.get_sprite(name)
        if sprite:
            self.sprites[name] = pygame.transform.scale(sprite, new_size)
            return self.sprites[name]
        return "Error"