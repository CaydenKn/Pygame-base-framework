import pygame
from core.GameObject import *

class Enemy(Sprite):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, 50, 50, "red", sprite)
        self.health = 100
        self.speed = 5
        self.direction = 1

    def move(self):
        self.x += self.speed * self.direction

    def check_collision(self, other):
        if self.collides_with(other):
            self.health -= 1
            if self.health <= 0:
                print('Dead')
                self.y += 10

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))