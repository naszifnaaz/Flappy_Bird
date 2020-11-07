#FlappyBird using pygame

import pygame
import sys
import random
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

pipe_surface = pygame.image.load('assets/images/sprites/Pipe.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
pipe_height = [200,400,600]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)

#drawing dynamic floor
def draw_floor():
    win.blit(floor_surface,(dynamic_floor,700))
    win.blit(floor_surface,(dynamic_floor + 500 ,700))

#create pipe
def create_pipe():
    random_pipe = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe - 220))
    return bottom_pipe, top_pipe

#moving pipes
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

#drawing pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            win.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            win.blit(flip_pipe,pipe)

#game loop
while run:
    
    #setting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    win.blit(bg_surface,(0,0))

    #Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    win.blit(bird_surface,bird_rect)
    

    #Pipes
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)


    #Floor
    dynamic_floor -= 1
    draw_floor()
    if dynamic_floor <= -500:
        dynamic_floor = 0

    pygame.display.update()
    clock.tick(FPS)