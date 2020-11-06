#FlappyBird using pygame

import pygame
import sys

#game constants
WIDTH = 576
HEIGHT = 700
FPS = 120
run = True

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

while run:
    
    #setting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)