#FlappyBird using pygame

import pygame
import sys
from constants import *



#pygame initialisation
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

#loading assets
bg_surface = pygame.image.load('assets/images/sprites/Background.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(WIDTH,HEIGHT))

floor_surface = pygame.image.load('assets/images/sprites/Floor.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

bird_surface = pygame.image.load('assets/images/sprites/Bird_mid.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 400))


#drawing floor
def draw_floor():
    win.blit(floor_surface,(dynamic_floor,670))
    win.blit(floor_surface,(dynamic_floor + 500 ,670))

#game loop
while run:
    
    #setting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.blit(bg_surface,(0,0))
    win.blit(bird_surface,bird_rect)
    dynamic_floor -= 1
    draw_floor()
    if dynamic_floor <= -500:
        dynamic_floor = 0

    pygame.display.update()
    clock.tick(FPS)