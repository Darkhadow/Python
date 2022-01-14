from turtle import *

def squaredrawing():
    bgcolor("white")
    count = 1
    while count < 5:
        forward(100)
        right(90)
        count = count + 1
    penup()
    backward(200)
    pendown()
    count = 1
    while count < 5:
        forward(100)
        right(90)
        count = count + 1
    penup()
    forward(400)
    pendown()
    count = 1
    while count < 5:
        forward(100)
        right(90)
        count = count + 1
    penup()
    goto(-100,100)
    pendown()
    count = 1
    while count < 5:
        forward(100)
        right(90)
        count = count + 1
