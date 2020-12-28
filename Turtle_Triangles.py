# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:50:29 2020

@author: anwno
"""

import turtle
from random import randint

# ------------ Makes instant
turtle.tracer(0, 0)

# ----------- Setup ----------- #
color_list = ['red','orange','yellow','green','blue','indigo','violet']
length = 100  #triangle side length

tur = turtle.Turtle()
tur.speed(0)  #Speed of turtle. 0 = slow, 10 = fast

def tri(arg1, arg2):  #arg1: 'right' or 'left'   arg2: length
    random_color = color_list[randint(0,6)]
    tur.fillcolor(random_color)
    tur.begin_fill()
    for x in range(3):
        tur.forward(arg2)
        if arg1 == "right":
            tur.right(120)
        else:
            tur.left(120)
    tur.end_fill()
    
def hexagon(arg1):
    # ----------- Center ----------- #
    for x in range(6):
        
        tri('right',length)
        tur.right(60)
        
    tur.forward(length)
    tur.left(60)
    # ----------- 2nd Ring 1 ----------- #
    
    for x in range(6):
    
        tri('left',length)
        
        tur.up()
        tur.left(60)
        tur.forward(length)
        tur.down()
        
    # ----------- 2nd Ring Small Triangles1 ----------- #
    
    def little_tri():
        for x in range(2):
            tri('right',length/2)
            tur.right(60)
            tri('right',length/2)
            tur.left(60)
            tur.forward(length/2)
        
        tur.backward(length)
        tur.right(120)
        tur.forward(length/2)
        tur.left(120)
        
        for x in range(2):
            tri('right',length/2)
            tur.right(60)
            tri('right',length/2)
            tur.left(60)
            tur.forward(length/2)
        
        tur.up()    
        tur.left(60)
        tur.forward(length/2)
        tur.left(60)
        tur.forward(length)
        tur.right(60)
        tur.down()
    
    for x in range(6):
        little_tri()
    
    tur.right(60)
    tur.backward(length)
    
    if arg1 == 0:
        tur.up()
        tur.left(120)
        tur.forward(length*4)
        tur.right(120)
        tur.forward(length*2)
        tur.down()

    if arg1 in range(1,7):
        tur.up()
        tur.forward(length*2)
        tur.right(60)
        tur.forward(length*2)
        tur.down()
        

for x in range(7):
    hexagon(x)  
    
# ------------ Makes instant
turtle.update()

turtle.done()
turtle.bye()


try:
    turtle.bye()   
except turtle.Terminator:
    pass
