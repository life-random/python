# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle as t
t.shape("turtle")
t.clear()
n = int(input("몇 각형을 그리실것인가요? :"))

for i in range(n):
    t.forward(100)
    t.left(360//n)