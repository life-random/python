# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:36:57 2021

@author: Mac_1
"""
import turtle as t

def n_polygon(n, lenght):
    for i in range(n):
        t.forward(lenght)
        t.left(360//n)

for i in range(10):
    t.left(20)
    n_polygon(6, 100)
    
t.done()
t.bye()