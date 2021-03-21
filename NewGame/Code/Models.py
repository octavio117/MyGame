import pygame

class model():
    def __init__(self, Name, Picture, Hitbox):
        self.name = Name
        self.picture = Picture
        self.hitbox = Hitbox
    def Scale(self, scale):
        self.picture = pygame.transform.scale(self.picture, scale)
    def movement(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            return 'Left'
        if keys_pressed[pygame.K_RIGHT]:
            return 'Right'      
        if keys_pressed[pygame.K_SPACE]:
            return 'Jump'
        if keys_pressed[pygame.K_DOWN]:
            return 'Down'
class Block():
    def __init__(self, name, Picture, Hitbox):
        self.name = name
        self.picture = Picture
        self.hitbox = Hitbox
    def Scale(self, scale):
        self.picture = pygame.transform.scale(self.picture, scale)
    