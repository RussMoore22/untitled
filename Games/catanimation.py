import pygame, sys
import random
from pygame.locals import *



pygame.init()

FPS = 60 #frames per second setting
fpsClock = pygame.time.Clock()

#Set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (100, 100, 100)
col_array = [(0, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 255), (128, 128, 128), (0, 128, 0),
             (0, 255, 0), (128, 0, 0), (0, 0, 128), (128, 128, 0), (128, 0, 128), (255, 0, 0), (0, 128, 128)]


count = random.randint(0, 12)
randcol = col_array[count]
coltest = col_array[5]


CatImgleft = pygame.image.load('catleft.png')
CatImgup = pygame.image.load('catup.png')
CatImgdown = pygame.image.load('catdown.png')
CatImgright = pygame.image.load('catright.png')



Catx = 10
Caty = 10
direction = 'right'

while True: #The main game loop
    DISPLAYSURF.fill(randcol)

    if direction == 'right':
        Catx += 5
        if Catx == 280:
            direction = 'down'
            count = random.randint(0, 12)
            randcol = col_array[count]
            pygame.draw.rect(DISPLAYSURF, randcol, (0, 0, 400, 300))
    elif direction == 'down':
        Caty += 5
        if Caty ==  200:
            direction = 'left'
            count = random.randint(0, 12)
            randcol = col_array[count]
            pygame.draw.rect(DISPLAYSURF, randcol, (0, 0, 400, 300))
    elif direction == 'left':
        Catx -= 5
        if Catx == 10:
            direction = 'up'
            count = random.randint(0, 12)
            randcol = col_array[count]
            pygame.draw.rect(DISPLAYSURF, randcol, (0, 0, 400, 300))
    elif direction == 'up':
        Caty -= 5
        if Caty == 10:
            direction = 'right'
            count = random.randint(0, 12)
            randcol = col_array[count]
            pygame.draw.rect(DISPLAYSURF, randcol, (0, 0, 400, 300))
    if direction == 'right':


        DISPLAYSURF.blit(CatImgright, (Catx, Caty))
    elif direction == 'left':

        DISPLAYSURF.blit(CatImgleft, (Catx, Caty))
    elif direction == 'up':

        DISPLAYSURF.blit(CatImgup, (Catx, Caty))
    elif direction == 'down':

        DISPLAYSURF.blit(CatImgdown, (Catx, Caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)




