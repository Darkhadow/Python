"--MODULES--"

import pygame as pg
import sys, random

"--CONSTANT/KEY VARIABLES--"

# Setup
pg.init()
screen = pg.display.set_mode((288,512))
clock = pg.time.Clock()
game_font = pg.font.Font("04B_19.ttf",20)
color = pg.color.THECOLORS

# Game Var
gravity = 0.5 
p1_movement = 0 
game_active = True
 
# Scoring 
score = 0
high_score = 0
can_score = True

"--ASSETS--"

# Image, Background
bg_surface = pg.image.load('assets/background-day.png').convert()
# Image, Floor
floor_surface = pg.image.load('assets/base.png').convert()
floor_x_pos = 0
# Images, p1 animation
p1_downflap = pg.image.load('assets/downflap.png').convert_alpha()
p1_midflap = pg.image.load('assets/upflap.png').convert_alpha()
p1_upflap = pg.image.load('assets/upflap.png').convert_alpha()
p1_frames = [p1_downflap,p1_midflap,p1_upflap]
p1_index = 0
# p1 Rect 
p1_surface = p1_frames[p1_index]
p1_rect = p1_surface.get_rect(center = (50,257))
p1flap = pg.USEREVENT
pg.time.set_timer(p1flap,200)
# Images, pipe                                        
pipe_surface = pg.image.load('assets/pipe-red.png')
pipe_list = []
spawnpipe = pg.USEREVENT + 1
pg.time.set_timer(spawnpipe,1200)
pipe_height = [200,300,400]

# Sound, Birb FX
flap_sound = pg.mixer.Sound('sound/sfx_wing.wav')
death_sound = pg.mixer.Sound('sound/sfx_hit.wav')

# Sound, Scoring 
score_sound = pg.mixer.Sound('sound/sfx_point.wav')

# Images, Gameover 
game_over_surface = pg.image.load('assets/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center = (144,257))

"--FUNCTIONS--"

def score_display(game_state): 
    if game_state == 'main_game':
        score_surface = game_font.render((f'Score: {int(score)}'),True,color['white'])
        score_rect = score_surface.get_rect(center = (144,50))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render((f'Score: {int(score)}'),True,color['gray'])
        score_rect = score_surface.get_rect(center = (144,50))
        screen.blit(score_surface,score_rect)
        high_score_surface = game_font.render((f'High score: {int(high_score)}'),True,color['royalblue1'])
        high_score_rect = high_score_surface.get_rect(center = (144,425))
        screen.blit(high_score_surface,high_score_rect)
  
def update_score(score,high_score): 
    if score > high_score:
        high_score = score
    return high_score
                
# Exercise Answer                
def pipe_score_check():
    global score, can_score
    if pipe_list:
        for pipe in pipe_list:
            if 65 < pipe.centerx < 85 and can_score:
                score += 1
                score_sound.play()
                can_score = False
            if pipe.centerx < 0:
                can_score = True

def check_collision(pipes):
    for pipe in pipes:
        if p1_rect.colliderect(pipe):
            death_sound.play()
            return False  
    if p1_rect.top <= -50 or p1_rect.bottom >= 450:
        death_sound.play()
        return False

    return True

                                                                                          
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (350,random_pipe_pos - 150))
    return bottom_pipe,top_pipe

                                                                                    
def move_pipes(pipes): 
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes

                                                                                        
def draw_pipes(pipes): 
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pg.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)


def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos+288,450))
    
def p1_animation(): 
    new_p1 = p1_frames[p1_index]
    new_p1_rect = new_p1.get_rect(center = (50,p1_rect.centery))
    return new_p1,new_p1_rect

def rotate_p1(p1): 
    new_p1 = pg.transform.rotozoom(p1,-p1_movement*3,1)
    return new_p1

def main():
    global floor_x_pos,p1_movement,p1_surface,p1_rect
    global p1_index,pipe_list,game_active,score,high_score                               
    
    while True:
        #Handle closing
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # P1 jumps when space is pressed
            if event.type == pg.KEYDOWN:  
                keys = pg.key.get_pressed()
                if keys[pg.K_SPACE] and game_active:
                    p1_movement = 0
                    p1_movement -= 10
                    flap_sound.play()
                #Resets game after death by pressing space bar
                if keys[pg.K_SPACE] and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    p1_rect.center = (50,257)
                    p1_movement = 0
                    score = 0
            # P1 cycles thru different animation        
            if event.type == p1flap:
                if p1_index < 2:
                    p1_index += 1
                else:
                    p1_index = 0

                p1_surface,p1_rect = p1_animation()

            # Adds new pipe to pipe_list
            if event.type == spawnpipe:
                pipe_list.extend(create_pipe())                 
                
        # Draw background
        screen.blit(bg_surface,(0,0))

        # Only runs when game is active
        if game_active:
            #p1
            p1_movement += gravity
            rotated_p1 = rotate_p1(p1_surface)
            p1_rect.centery += p1_movement
            screen.blit(rotated_p1,p1_rect)
            game_active = check_collision(pipe_list)
            
            # Pipes 
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)
            
            # Current score
            pipe_score_check()
            score_display('main_game')
        else:
            # Game over score
            screen.blit(game_over_surface,game_over_rect) #display restart graphic
            high_score = update_score(score,high_score)
            score_display("game_over")
            
        # Draw floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -288:
            floor_x_pos = 0
        
        pg.display.update()
        clock.tick(60)

"--EXECUTE--"
if __name__ == '__main__':
    main()

