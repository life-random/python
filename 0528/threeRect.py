# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:24:23 2021

@author: Mac_1
"""
import turtle as t

def drawRect(lenght):
    for i in range(4):
        t.forward(100)
        t.left(360/4)

for i in range(-200, 400, 200):
    t.up()
    t.goto(i, 0)
    t.down()
    drawRect(100)

t.done()
t.bye()
