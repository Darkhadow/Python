from turtle import *
import os
from math import *
import random
 
# Setup 
Screen().setup(0.5,0.85) 
bgcolor('black')
title("Turtle invaders ")


# Set up score system
score_value = 0
score_text = Turtle()
score_text.penup()
score_text.color('white')
score_text.speed(0)
score_text.penup()
score_text.goto(-310,320)
score_text.hideturtle()
style = ("Times new roman", 18)
score_text.write(f'Score:{score_value}',align='center',font=style)


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

# Add more enemies
enemy_total = 3
enemy_list = []
for i in range(enemy_total):
    enemy_list.append(Turtle())
    
# Setting up each enemy
for enemy in enemy_list:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.shapesize(0.5,0.5)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.goto(x,y)

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
        # Bullet state
        # Ready - ready to fire
        # Fire - bullet is firing
bullet_state = 'ready'


# This will increace score when trigger
def score_update():
    global score_value
    score_value += 100
    score_text.clear()
    score_text.write(f'Score:{score_value}',font = style)


# Collision func
def isCollision(t1, t2):
    distance = sqrt(pow(t1.xcor()-t2.xcor(),2)+pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False


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
 
def move_stop():
    global player_speed
    player_speed = 0
 
# Fire bullet func   
def fire_bullet():
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        # Spawn bullet on top of player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x,y)
        bullet.showturtle()        
 
 
# Create keyboard keybinding
listen()
onkeypress(move_left,'a')
onkeypress(move_right,'d')
onkeypress(move_reset,'x')
onkeyrelease(move_stop, "a")
onkeyrelease(move_stop, "d")
onkeypress(fire_bullet,'space') # Fire button  

#Main game loop
while True:
    # Scan thru each enemy within list
    for enemy in enemy_list:
        # Move player 
        player.setx(player.xcor()+player_speed)
             # Check borders 
        if player.xcor() > 285:
            player.setx(285)
            player_speed = 0
        elif player.xcor() < -285:
            player.setx(-285)
            playerspeed = 0
     
        # Move enemy 
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
     
    ##    # Enemy checks right border, if hit, move left 
    ##    if enemy.xcor() > 280:
    ##        enemy_speed *= -1
    ##    # Enemy checks left border, if hit, move right   
    ##    if enemy.xcor() < -280:
    ##        enemy_speed *= -1
     
        # Enemy checks right border, if hit, move left & down 40 pixels 
        if enemy.xcor() > 280:
            enemy_speed *= -1
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
     
        if enemy.xcor() < -280:
            enemy_speed *= -1
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
     
        # Enemy L&R and down 1 step (compressed) #BONUS 1   
    ##    if enemy.xcor() > 280 or enemy.xcor() < -280:
    ##        enemy_speed *= -1
    ##        enemy.sety(enemy.ycor() - 40)
    ##        print(enemy_speed)
        # Bullet hit enemy
        if isCollision(bullet, enemy):
            print('hit')
            # Reset the bullet
            bullet.hideturtle()
            # Remove enemy
            enemy.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0,-400)
            score_update() # Increace score upon hit

        # Enemt hit player
        if isCollision(player, enemy):
            # Removes the player
            player.hideturtle()
            enemy,hideturtle()
            print("!Game Over!")
            break
     
        # Move bullet upwards  
        if bullet_state == 'fire':
            bullet.showturtle()
            y = bullet.ycor()
            y += bullet_speed
            bullet.sety(y)
            
        # Bullet reset when hit top boundary  
        if bullet.ycor() > 280:
            bullet.hideturtle()
            bullet_state = 'ready'
