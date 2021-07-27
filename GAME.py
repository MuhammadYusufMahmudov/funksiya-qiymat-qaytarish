# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:02:58 2021

@author: GAME
"""

import turtle
my_wn=turtle.Screen()
turtle.speed(2)
for i in range(30):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()
    