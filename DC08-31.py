from turtle import *
import turtle
import random
color('red', 'yellow')
turtle.speed(20)
begin_fill()
while True:
    forward(300)
    left(91)
    if abs(pos()) < 1:
        break
while True:
    forward(300)
    left(179)
    if abs(pos()) < 1:
        break
done()