import pygame

class Mouse:
    def __init__(self):
        self.buttons = {}
        self.pos = (0, 0)
        self.rel = (0, 0)
        self.wheel = 0
        self.wheel_rel = 0

    def update(self):
        self.buttons = pygame.mouse.get_pressed()
        self.pos = pygame.mouse.get_pos()
        self.rel = pygame.mouse.get_rel()
        self.wheel = pygame.mouse.get_wheel()
        self.wheel_rel = pygame.mouse.get_rel()[1]

    def getButton(self, button):
        return self.buttons[button]

    def getPos(self):
        return self.pos

    def getX(self):
        return self.pos[0]
    
    def getY(self):
        return self.pos[1]

    def getRel(self):
        return self.rel

    def getWheel(self):
        return self.wheel

    def getWheelRel(self):
        return self.wheel_rel
