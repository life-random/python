# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:31:16 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
t.clear()
scr = t.s

while True:
    s = t.textinput("도형", "삼각형, 사각형, 원, 종료 중 하나 고르세!")
    t.reset()
    if s == "사각형":
        s = t.textinput("가로", "가로 :")
        w = int(s)
        s = t.textinput("높이", "높이 :")
        h = int(s)
        for i in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)
    elif s == "원":
        s = t.textinput("반지름", "반지름 :")
        r = int(s)
        t.circle(r)
    elif s == "삼각형":
        s = t.textinput("한 변의 길이", "길이 :")
        l = int(s)
        for i in range(3):
            t.forward(l)
            t.left(120)
    elif s == "종료":
        break
    else:
        t.write("잘못된 입력입니다. 다시 입력해주세요!")
            
   src.bye()
t.exitonclick
    
    