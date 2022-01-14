from turtle import *

def triangledrawing():
    bgcolor("black")
    penup()
    goto(-127,70)
    pendown()
    color("cyan")
    begin_fill()
    for i in range(3):
        forward(230)
        left(120)
    end_fill()
