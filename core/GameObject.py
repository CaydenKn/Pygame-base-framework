import pygame

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

class Circle(GameObject):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius * 2, radius * 2, color)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.radius, self.y + self.radius), self.radius)

class Rect(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Line(GameObject):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__(x1, y1, x2 - x1, y2 - y1, color)
        self.x2 = x2
        self.y2 = y2

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x2, self.y2))

class Polygon(GameObject):
    def __init__(self, points, color):
        super().__init__(points[0][0], points[0][1], points[1][0] - points[0][0], points[1][1] - points[0][1], color)
        self.points = points

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)
        
class Sprite(GameObject):
    def __init__(self, x, y, width, height, color, sprite):
        super().__init__(x, y, width, height, color)
        self.sprite = sprite

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

class AnimatedSprite(GameObject):
    def __init__(self, x, y, width, height, color, sprites):
        super().__init__(x, y, width, height, color)
        self.sprites = sprites
        self.current_sprite = 0
        self.frame = 0

    def draw(self, screen):
        screen.blit(self.sprites[self.current_sprite], (self.x, self.y))
        self.frame += 1
        if self.frame >= 10:
            self.frame = 0
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

class Text(GameObject):
    def __init__(self, text, x, y, color, font_size):
        super().__init__(x, y, 0, 0, color)
        self.text = text
        self.font_size = font_size

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", self.font_size)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))
