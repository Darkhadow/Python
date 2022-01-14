# Imports
from turtle import *
import os
# Setup (LESSON 2.1 setup screen and talk about the size)
Screen().setup(0.5,0.85)   #measure int=pixels, float=fraction
bgcolor('black')
title("Turtle invaders ")
 
# Draw border (LESSON 2.2 setting up a border to limit movement)
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
 
 
# Create player (LESSON 2.3 making player & facing right way)
player = Turtle()
player.color('blue')
player.shape('turtle')
player.penup()
player.speed(0)
player.goto(0,-250)
player.lt(90)
 
# Move player speed (LESSON 2.4 begins with 0 so that it wont move at first)
player_speed = 0
 
# Move funcs (explain that this is constantly adding when we press key later)
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
 
# func to stop sliding(LESSON 2.8)
def move_stop():
    global player_speed
    player_speed = 0
 
 
# Keyboard keybinding (LESSON 2.5 funcs to get key press)
listen()
onkeypress(move_left,'a')
onkeypress(move_right,'d')
onkeypress(move_reset,'x')
# Stop sliding (LESSON 2.9)
onkeyrelease(move_stop, "a")
onkeyrelease(move_stop, "d")
 
# Main game loop (LESSON 2.6 main loop that will constantly run)
while True:
    # Move player (this is constantly being added)
    player.setx(player.xcor()+player_speed)
      # Check borders limits (LESSON 2.7 checks if player has reach boarder limits)
    if player.xcor() > 285:
        player.setx(285)
        player_speed = 0
 
    elif player.xcor() < -285:
        player.setx(-285)
        playerspeed = 0
 
