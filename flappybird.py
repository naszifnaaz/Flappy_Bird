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
#importing sound
flap_sound = pygame.mixer.Sound('assets/sounds/sound_effects/Flap.ogg')
hit_sound = pygame.mixer.Sound('assets/sounds/sound_effects/Hit.ogg')
score_sound = pygame.mixer.Sound('assets/sounds/sound_effects/Point.ogg')

#import font
game_font = pygame.font.Font('assets/font/04B_19.ttf',40)

#loading background
bg_surface = pygame.image.load('assets/images/sprites/Background.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(WIDTH,HEIGHT))

#loading floor
floor_surface = pygame.image.load('assets/images/sprites/Floor.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

#loading bird animations
bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/images/sprites/Bird_down.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/images/sprites/Bird_mid.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/images/sprites/Bird_up.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 400))
BIRD_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRD_FLAP, 200)

#loading pipes
pipe_surface = pygame.image.load('assets/images/sprites/Pipe.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
pipe_height = [200,400,550]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)

#loading game-over 
gameover_surface = pygame.image.load('assets/images/sprites/Game_Over.png').convert_alpha()
gameover_surface = pygame.transform.scale2x(gameover_surface)
gameover_rect = gameover_surface.get_rect(center = (262, 400))

#drawing dynamic floor
def draw_floor():
    win.blit(floor_surface,(dynamic_floor,700))
    win.blit(floor_surface,(dynamic_floor + 500 ,700))

#creating pipes
def create_pipe():
    random_pipe = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe - 250))
    return bottom_pipe, top_pipe

#moving pipes
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes

#drawing pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            win.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            win.blit(flip_pipe,pipe)

#collision detection
def check_collision(pipes):
    global can_score
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            pygame.time.delay(300)
            can_score = True
            return False
    if bird_rect.top <= -150 or bird_rect.bottom >= 700:
        hit_sound.play()
        pygame.time.delay(300)
        can_score = True
        return False
    return True

#rotating bird on hit
def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3,1)
    return new_bird

#bird flap animation
def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

#scoring system
def score_display(game_active):
    if game_active == 'main_game':
        score_surface = game_font.render(str(int(SCORE)), True, WHITE)
        score_rect = score_surface.get_rect(center = (262, 100))
        win.blit(score_surface,score_rect)

    if game_active == 'game_over':
        score_surface = game_font.render(f'Score: {int(SCORE)}', True, WHITE)
        score_rect = score_surface.get_rect(center = (262, 100))
        win.blit(score_surface,score_rect)
         
        HIGHSCORE_surface = game_font.render(f'High Score: {int(HIGH_SCORE)}', True, WHITE)
        HIGHSCORE_rect = score_surface.get_rect(center = (200, 685))
        win.blit(HIGHSCORE_surface,HIGHSCORE_rect)

#updating high-scores
def update_score(SCORE, HIGH_SCORE):
    if SCORE > HIGH_SCORE:
        HIGH_SCORE = SCORE
    return HIGH_SCORE

#scoring system updated
def pipe_score_check():
    global SCORE,can_score

    if pipe_list:
        for pipe in pipe_list:
            if 95 < pipe.centerx < 105 and can_score:
                SCORE+=1
                score_sound.play()
                can_score = False
            
            if pipe.centerx < 0:
                can_score = True

#game loop
while RUN:
    #setting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == True:
                bird_movement = 0
                bird_movement -= 8
                flap_sound.play() 
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,400)
                bird_movement = 0
                SCORE = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        
        if event.type == BIRD_FLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    win.blit(bg_surface,(0,0))

    if game_active:
        #Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        win.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)
        

        #Pipes
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        pipe_score_check()
        score_display('main_game')
    else :
        win.blit(gameover_surface,gameover_rect)
        HIGH_SCORE = update_score(SCORE, HIGH_SCORE)
        score_display('game_over')

    #Floor
    dynamic_floor -= 1
    draw_floor()
    if dynamic_floor <= -500:
        dynamic_floor = 0

    pygame.display.update()
    clock.tick(FPS)
    