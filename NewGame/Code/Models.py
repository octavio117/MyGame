import pygame

class model():
    def __init__(self, Name, Picture, Hitbox):
        self.name = Name
        self.picture = Picture
        self.hitbox = Hitbox
    def Scale(self, scale):
        self.picture = pygame.transform.scale(self.picture, scale)
    def Flip(self):
        self.picture = pygame.transform.flip(self.picture, True, False)
    def input_move(self, keys_pressed):
        if keys_pressed[pygame.K_SPACE]:
            self.hitbox.y -= 25
        if keys_pressed[pygame.K_LEFT]:
            self.hitbox.x -= 10
        if keys_pressed[pygame.K_RIGHT]:
            self.hitbox.x += 10
        if keys_pressed[pygame.K_DOWN]:
            self.hitbox.y += 10
class Block():
    def __init__(self, name, Picture, Hitbox):
        self.name = name
        self.picture = Picture
        self.hitbox = Hitbox
    def Scale(self, scale):
        self.picture = pygame.transform.scale(self.picture, scale)
    