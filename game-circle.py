# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:09:13 2021

@author: gaME
"""
import turtle
my_wn=turtle.Screen()
turtle.bgcolor("yellow")
turtle.pencolor("red")
turtle.speed(9.5)
for i in range(30):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()




