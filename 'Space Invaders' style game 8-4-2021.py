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

# Keyboard keybinding
listen()
onkeypress(move_left,'a')
onkeypress(move_right,'d')
onkeypress(move_reset,'x')
# Stop sliding
onkeyrelease(move_stop,"a")
onkeyrelease(move_stop,"d")

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
