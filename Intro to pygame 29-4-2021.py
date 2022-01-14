"--MODULES--"
import pygame as pg
import random

"--CONSTANT/KEY VARIABLES--"
WIDTH,HEIGHT = 500,500
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Dhira's first pygame")
color = pg.color.THECOLORS

"--IMAGES--"
logo = pg.image.load('ASSETS\logo.png').convert_alpha()
x_pos = (WIDTH/2)-(274/2)
y_pos = (HEIGHT/2)-(217/2)
vel = 1

pick = 'steelblue'

"--FUNTIONS--"
def player_control():
    global x_pos,y_pos
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        if not x_pos <= 0:
            x_pos -= vel
    if keys[pg.K_d]:
        if not x_pos >= 500-274:
            x_pos += vel
    if keys[pg.K_w]:
        if not y_pos <= 0:
            y_pos -= vel
    if keys[pg.K_s]:
        if not y_pos >= 500-217:
            y_pos += vel
    if keys[pg.K_SPACE]:
        x_pos = (WIDTH/2)-(274/2)
        y_pos = (HEIGHT/2)-(217/2)
    if keys[pg.K_q]:
        pick = random.choice([i for i in color.keys()])
    return x_pos,y_pos

def draw_screen(x_pos,y_pos):
    screen.fill(color[pick])
    screen.blit(logo,(x_pos,y_pos))
    pg.display.update()

def main():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        player_control()
        draw_screen(x_pos,y_pos)

    pg.quit()

"--EXECUTE--"
if __name__ == "__main__":
    main()
