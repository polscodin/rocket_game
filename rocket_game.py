import pygame
from pygame.locals import *
import time


pygame.init()

WIDTH = 800
HEIGHT = 600

imgstart = (0,0)
space = pygame.image.load("spacebg.png")
rocket = pygame.image.load("rocket.png")

rocket_x = (WIDTH/2)
rocket_y = (HEIGHT/2)
rocket_pos = (rocket_x,rocket_y)
screen = pygame.display.set_mode((WIDTH,HEIGHT))

keys = [False,False,False,False]


rocket_x = (WIDTH/2.4)
rocket_y = (HEIGHT/2.5)


while rocket_y < HEIGHT:
    rocket_pos = (rocket_x,rocket_y)

    screen.blit(space,imgstart)
    screen.blit(rocket,rocket_pos)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.type == K_UP:
                keys[0] = True
            if event.type == K_LEFT:
                keys[1] = True        
            if event.type == K_DOWN:
                keys[2] = True  
            if event.type == K_RIGHT:
                keys[3] = True      


    if keys[0]:
        if rocket_y > 0:
            rocket_y -= 7
    elif keys[1]:
        if rocket_x > 0:
            rocket_y -= 2
    elif keys[2]:
        if rocket_y < 570:
            rocket_y += 4
    elif keys[3]:
        if rocket_x <770:
            rocket_x += 2

    if event.type == pygame.KEYUP:
        if event.type == K_UP:
            keys[0] = False
        if event.type == K_LEFT:
            keys[1] = False        
        if event.type == K_DOWN:
            keys[2] = False  
        if event.type == K_RIGHT:
            keys[3] = False
    rocket_y += 1
    time.sleep(0.15)
    
    

    
    

        
