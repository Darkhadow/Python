from house import *
from triangle import *
from square import *
print("-----MENU-----")

ask=input('''
a) House Drawing
b) 4 Squares
c) A Gaint Triangle
d) Exit

Option: ''').lower()
if ask == 'a':
    housedrawing()
elif ask == 'b':
    squaredrawing()
elif ask == 'c':
    triangledrawing()
elif ask == 'd':
    bye()
exit()
