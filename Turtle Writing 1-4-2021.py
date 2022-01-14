from turtle import *
from random import *
#Setup
Screen().setup(500,500)
bgcolor('gray')
title("How to write on screen")
speed(0)
speed(0)
speed(0)
speed(0)
speed(0)

###Write text
##color("Red")
##style=('Times New Roman', 20 ,'normal')
##penup()
##goto(-200,200)
##pendown()
##write('ZoneA',align='center',font = style)
##
##color("Blue")
##style=('Jokerman', 20 ,'normal')
##penup()
##goto(200,200)
##pendown()
##write('ZoneB',align='center',font = style)
##
##color("Lime")
##style=('Comic sans ms', 20 ,'normal')
##penup()
##goto(-200,-230)
##pendown()
##write('ZoneD',align='center',font = style)
##
##color("Deep Pink")
##style=('Impact', 20 ,'normal')
##penup()
##goto(200,-230)
##pendown()
##write('ZoneC',align='center',font = style)
##
##color("Magenta")
##style=('Arial', 20 ,'normal')
##penup()
##goto(0,0)
##pendown()
##write('ZoneX',align='center',font = style)

###Square written with loop
##for i in range(4):
##    forward(50)
##    left(90)

#Square in function
def square():
    for i in range(4):
        forward(50)
        left(90)
#Function to clean move and draw
def move_n_draw(x,y):
    penup()
    goto(x,y)
    pendown()
    square()
###List of locations
##place = [(randint(-100,100)),(randint(-100,100)),(randint(-100,100)),(randint(-100,100)),(randint(-100,100)),(randint(-100,100)),(randint(-100,100)),(randint(-100,100))]
###Using for loop to draw
##for x,y in place:
##    move_n_draw(x,y)

for i in range(100):
    x,y = randint(-200,200),randint(-200,200)
    move_n_draw(x,y)
