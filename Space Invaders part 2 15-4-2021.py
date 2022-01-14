#Imports
from turtle import *

# Setup
Screen().setup(0.5,0.85)
bgcolor('black')
title("Turtle invaders ")

# Draw border
border = Turtle()
border.color('white')
border.speed(0)
border.penup()
border.goto(-300,-300)
border.pensize(3)
border.pendown()
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()


# Create player
player = Turtle()
player.color('blue')
player.shape('turtle')
player.penup()
player.speed(0)
player.goto(0,-250)
player.lt(90)

# Move player speed
player_speed = 0

# Create player speed
enemy = Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.goto(-200,250)

# Move enemy speed
enemy_speed = 2

# Create bullet
bullet = Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.lt(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet_speed = 20
# Bullet state
        # Ready - ready to fire
        # Fire - bullet is firing
bullet_state = 'ready'


# Move funcs
def move_left():
    global player_speed
    player_speed = -3

def move_right():
    global player_speed
    player_speed = 3

def move_reset():
    global player_speed
    player_speed = 0
    player.setx(0)

# func to stop sliding
def move_stop():
    global player_speed
    player_speed = 0

# Fire bullet func
def fire_bullet():
    global bullet_state
    if bullet_state == 'ready':
        bullete_state = 'fire'
        # Spawn bullet on top of player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x,y)
        bullet.showturtle()

# Keyboard keybinding
listen()
onkeypress(move_left,'a')
onkeypress(move_right,'d')
onkeypress(move_reset,'x')
# Stop sliding
onkeyrelease(move_stop,"a")
onkeyrelease(move_stop,"d")
onkeypress(fire_bullet,'space') # Fire bullet

# Main game loop
while True:
    #move player
    player.setx(player.xcor()+player_speed)# Move left and right
      # Check borders limits
    if player.xcor() > 285:
        player.setx(285)
        player_speed = 0
    elif player.xcor() < -285:
        player.setx(-285)
        player_speed = 0

    # Move enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Enemy checks right border, if hit, move left & down 40 pixels
    if enemy.xcor() > 280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
    # Enemy checks left border, if hit, move right & down 40 pixels
    if enemy.xcor() < -280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    # Move bullet upwards
    if bullet_state == 'fire':
        bullet.showturtle()
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
