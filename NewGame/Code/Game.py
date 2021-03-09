from Models import model 
from Models import Block
import pygame
pygame.init()
pygame.mixer.init()

FPS = 60
clock = pygame.time.Clock()
mario_pos = (0 ,200)
mario_size = (50, 50)
floor_size = (60, 60)
floor_pos = (0, 600)
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
mario = model("Mario", pygame.image.load('/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/SMB_Smallmario.png'), pygame.Rect(mario_pos, mario_size))
mario.Scale(mario_size)
floor = Block('floor', pygame.image.load('/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Floor_Block.png'), pygame.Rect(floor_pos, floor_size))
floor.Scale(floor_size)
gravity = 5

def draw(M, B):
    WIN.fill((255, 255, 255))
    WIN.blit(M.picture, (M.hitbox.x, M.hitbox.y))
    WIN.blit(B.picture, (B.hitbox.x, B.hitbox.y))
    pygame.display.flip()
def Fall(M):
    M.hitbox.y += gravity
running = True
while running:    
    clock.tick(FPS)
    if mario.hitbox.y != floor.hitbox.y - 50:
        Fall(mario)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
    keys = pygame.key.get_pressed()
    mario.input_move(keys)
    draw(mario, floor)

    