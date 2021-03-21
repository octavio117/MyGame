from Models import model 
from Models import Block
import pygame
import time
pygame.init()
pygame.mixer.init()

FPS = 120
framespersec = pygame.time.Clock()
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#A list for the background paths
BCpaths = [
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_001.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_002.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_003.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_004.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_005.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_006.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_007.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_008.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_009.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_010.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_011.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_012.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_013.jpg',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/cut_images_5jiiDj64wMiEcdbG/image_part_014.jpg',
]
#list of mario paths and his size
mario_size = (80, 50)
Mario = [
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet.png',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet (4).png',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet (5).png',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet (6).png',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet (10).png',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet (8).png',
    '/Users/octaviodelgado/Desktop/VS_Code/Python/NewGame/Images/Mario/smb_mario_sheet (7).png'
]
walking = [pygame.transform.scale(pygame.image.load(Mario[1]), mario_size), pygame.transform.scale(pygame.image.load(Mario[2]), mario_size), pygame.transform.scale(pygame.image.load(Mario[3]), mario_size)]
mario = model('Mario', pygame.image.load(Mario[0]), pygame.Rect((0,580), mario_size))
mario.Scale(mario_size)
rmove_count = 0
lmove_count = 0
isjumping = False
def move(Mario, keys_pressed, x): #this will only move mario left and right
    if keys_pressed == 'Right' and Mario.hitbox.x < 420:
        Mario.hitbox.x += 10
    if keys_pressed == 'Left' and Mario.hitbox.x - 5 > 0:
        Mario.hitbox.x -= 10
    if keys_pressed == 'Jump':
        isjumping = True
def draw(mario, x, y, keys_pressed):
    #displays all BCs on the screen
    for backgrounds in BCpaths:
        WIN.blit(pygame.transform.scale(pygame.image.load(backgrounds), (WIDTH, HEIGHT)), (x, y))
        x += 900
    #displays mario
    global rmove_count
    global lmove_count
    if mario.movement(keys_pressed) == 'Right':
        WIN.blit(walking[rmove_count], (mario.hitbox.x, mario.hitbox.y))
        rmove_count += 1
        if rmove_count == 3:
            rmove_count = 0
    elif mario.movement(keys_pressed) == 'Left':
        WIN.blit(pygame.transform.flip(walking[lmove_count], True, False), (mario.hitbox.x, mario.hitbox.y))
        lmove_count += 1
        if lmove_count == 3:
            lmove_count = 0
    else:
        WIN.blit(mario.picture, (mario.hitbox.x, mario.hitbox.y))

x, y = 0, 0 # the BC location
running = True
while running:
    framespersec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # if x > -11700: #to see if the images are rendered
    #     x -= 10
    key = pygame.key.get_pressed()
    move(mario, mario.movement(key), x)
    if mario.hitbox.x == 420 and mario.movement(key) == 'Right':
        x -= 10
    print(mario.hitbox.x, mario.hitbox.y)    
    draw(mario, x, y, key)
    pygame.display.update()