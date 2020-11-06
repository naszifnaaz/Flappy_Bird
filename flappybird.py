#FlappyBird using pygame

import pygame
import sys

#game constants
WIDTH = 500
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
bg_surface = pygame.transform.scale(bg_surface,(WIDTH,HEIGHT))
floor_surface = pygame.image.load('assets/images/sprites/Floor.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

#game loop
while run:
    
    #setting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.blit(bg_surface,(0,0))
    win.blit(floor_surface,(0,670))
    pygame.display.update()
    clock.tick(FPS)