from Models import model 
from Models import Block
import pygame
pygame.init()
pygame.mixer.init()

FPS = 120
framespersec = pygame.time.Clock()
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Establish Mario elements
mario_size = (50, 70)
mario_path = '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/SMB_Smallmario.png'
mario_jumping_path = '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/SMB_Small_Mario_Jumping_Sprite.png'
BC_path = [
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_gfLmypHW1EzFqyU6/image_part_001.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_gfLmypHW1EzFqyU6/image_part_002.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_gfLmypHW1EzFqyU6/image_part_003.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_gfLmypHW1EzFqyU6/image_part_004.jpg',
]
BC = pygame.transform.scale(pygame.image.load(BC_path[0]), (900, 700))
mario = model('Mario', pygame.image.load(mario_path), pygame.Rect((0,0), (50, 70)))
mario.Scale(mario_size)

jumping = False
jumpcount = 10
x = 0
y = 0
running = True
while running:
    framespersec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    WIN.blit(BC, (x,y))
    WIN.blit(pygame.transform.scale(pygame.image.load(BC_path[1]), (900, 700)), (x+900, y))
    WIN.blit(mario.picture, (mario.hitbox.x, mario.hitbox.y))
    playermove = mario.movement(keys_pressed)
    #establish movement as well as jump
    if playermove == 'Right':
        mario.hitbox.x += 5
        if mario.hitbox.x > 450:
            x -= 10
    if playermove == 'Left' and mario.hitbox.x > 5:
        mario.hitbox.x -= 5
        x += 5
    if not jumping:
        if playermove == 'Down':
            mario.hitbox.y += 5
        if playermove == 'Jump':
            jumping = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            mario.hitbox.y -= (jumpcount ** 2) / 2 * neg
            jumpcount -= 1
        else:
            jumping = False
            jumpcount = 10
    pygame.display.update()

    
