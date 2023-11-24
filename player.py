import pygame
from core.GameObject import *
from core.SpriteManager import SpriteManager
from core.SoundManager import SoundManager

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, "red")
        self.speed = 5
        self.health = 100
        self.gravity = 4
        self.jump_height = 5
        self.is_jumping = False
        self.can_jump = True 

    def move(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_a]:
            self.x -= self.speed

        # Move right
        if keys[pygame.K_d]:
            self.x += self.speed

        # Jump
        if self.can_jump and keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.can_jump = False 

        # Apply gravity
        if not self.is_jumping:
            self.y += self.gravity
            self.can_jump = False
            self.check_collision()
        else:
            # Jumping logic
            if self.jump_height > 0:
                self.y -= self.jump_height
                self.jump_height -= 1
            else:
                self.is_jumping = False
                self.jump_height = 15
                self.can_jump = False

    def check_collision(self):
        block_height = 510

        if self.y + self.height > block_height:
            self.y = block_height - self.height  
            self.jump_height = 15  
            self.can_jump = True  

    def draw(self, screen, sprite):
        # Draws the player
        screen.blit(sprite, (self.x, self.y))

        # Health bar that scales with the player's health
        #Rect(self.x, self.y - 10, self.width * (self.health / 100), 5, "green").draw(screen)

        # Draws the player's position onto the screen
        Text("(" + str(self.x) + ", " + str(self.y) + ")", self.x, self.y + self.height + 5, "white", 20).draw(screen)
        
        Text("Health: " + str(self.health), 0, 0, "white", 20).draw(screen)
        
        # draw a line to the players mouse position
        mouse_pos = pygame.mouse.get_pos()
        Line(self.x + self.width / 2, self.y + self.height / 2, mouse_pos[0], mouse_pos[1], "white").draw(screen)
