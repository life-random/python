# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:53:09 2021

@author: Mac_1
"""
import turtle as t
import random as r

for i in range(30):
    lenght = r.randint(1, 100)
    t.forward(lenght)
    angle = r.randint(-180, 180)
    t.left(angle)

t.exitonclick()