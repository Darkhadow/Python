from turtle import *

def housedrawing():
    # setup
    title("My first drawing") # title of window
    Screen().setup(800,800) # size of window in pixels
    bgcolor("green") # background color
    shape("turtle")
    width(5)
    speed(0)
    # Movement
    # sky
    penup()
    goto(-400,-100)
    pendown()
    color('deepskyblue')
    begin_fill()
    count = 1
    while count < 3:
        forward(800)
        left(90)
        forward(500)
        left(90)
        count = count + 1
    end_fill()

    #sunq
    penup()
    goto(-320, 240)
    pendown()
    color("yellow")
    begin_fill()
    circle(50)
    end_fill()

    #House
    penup()
    goto(-100,-100)
    pendown()
    color("chocolate","orange") #stroke, fill
    begin_fill()
    for i in range(4):
        forward(170)
        left(90)
    end_fill()
    #house roof
    penup()
    goto(-127,70)
    pendown()
    color("brown","firebrick")
    begin_fill()
    for i in range(3):
        forward(225)
        left(120)
    end_fill()
    #house freatures
    penup()
    goto(-50,-100)
    pendown()
    color("red")
    begin_fill()
    forward(70)
    left(90)
    forward(100)
    left(90)
    forward(70)
    left(90)
    forward(100)
    end_fill()
    #doorknob
    penup()
    goto(-50,-50)
    pendown()
    color("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()
    goto(0,0)
    pendown()
    #window 1
    penup()
    goto(-80,60)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    left(90)
    forward(25)
    right(90)
    forward(50)
    left(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(50)
    #window 2
    penup()
    goto(50,60)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    left(90)
    forward(25)
    right(90)
    forward(50)
    left(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(50)
    #ending
    penup()
    goto(-400,400)
    pendown()
