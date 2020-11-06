#FlappyBird using pygame

import pygame
import sys

#game constants
WIDTH = 576
HEIGHT = 800
FPS = 120
run = True

#pygame initialisation
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

#drawing background
bg_surface = pygame.image.load('assets/images/sprites/Background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
win.blit(bg_surface,(0,0))

#game loop
while run:
    
    #setting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)