import turtle
# from turtle import *
from random import randint



finish = 200

t1 = turtle.Turtle()   # Создаем объект класса Turtle

t1.shape('turtle')
t1.color('green')
t1.penup()
t1.goto(-500,500)
t1.pendown()

t2 = turtle.Turtle()   # Создаем объект класса Turtle

t2.shape('turtle')
t2.color('red')
t2.penup()
t2.goto(-500,400)
t2.pendown()

def razmetkf():
    temp = turtle.Turtle()
    temp.speed(0)
    for i in range(21):
        temp.penup()
        temp.goto(-200+i*20, 50)
        temp.pendown()
        temp.goto(-200 + i * 20, -100)
    temp.hideturtle()




turtle.exitonclick()







