# import turtle
#
# import random
#
#
#
# finish = 200
#
# t1 = turtle.Turtle()   # Создаем объект класса Turtle
#
# t1.shape('turtle')
# t1.color('blue')
# t1.penup()
# t1.goto(-200,20)
# t1.pendown()
#
# t2 = turtle.Turtle()   # Создаем объект класса Turtle
#
# t2.shape('turtle')
# t2.color('red')
# t2.penup()
# t2.goto(-200,-20)
# t2.pendown()
#
# def razmetkf():
#     temp = turtle.Turtle()
#     temp.speed(0)
#     for i in range(1,21):
#         temp.penup()
#         temp.goto(-200+i*20, 50)
#         temp.pendown()
#         temp.goto(-200 + i * 20, -100)
#     temp.hideturtle()
#
# razmetkf()
#
# x1,y1= t1.position()
# x2,y1= t2.position()
#
# while(x1<finish and x2<finish):
#
#     t1.speed(random.randint(0,10))
#     t1.forward(random.randint(1,30))
#     x1, y1 = t1.position()
#     if(x1>finish):break
#
#     t2.speed(random.randint(0,10))
#     t2.forward(random.randint(1,30))
#     x2, y1 = t2.position()
#
# turtle.exitonclick()





# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def fahrenheit2celsius(temp):
#     """
#     Returns temperature in Celsius.
#     """
#     return (5. / 9.) * (temp - 32)
#
#
# def convert_ax_c_to_celsius(ax_f):
#     """
#     Update second axis according with first axis.
#     """
#     y1, y2 = ax_f.get_ylim()
#     ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
#     ax_c.figure.canvas.draw()
#
# fig, ax_f = plt.subplots()
# ax_c = ax_f.twinx()
#
# # automatically update ylim of ax2 when ylim of ax1 changes.
# ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
# ax_f.plot(np.linspace(-40, 120, 100))
# ax_f.set_xlim(0, 100)
#
# ax_f.set_title('Two scales: Fahrenheit and Celsius')
# ax_f.set_ylabel('Fahrenheit')
# ax_c.set_ylabel('Celsius')
#
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# x = ['А', 'Б', 'В','C']
# y = [10, 50, 30, 35]
#
# sns.barplot(x=x, y=y);
# plt.show()


import seaborn
import matplotlib.pyplot as plt
w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
data = [[1, 2, 1, 1],
        [2, 3, 1, 3],
        [3, 1, 3, 2],
        [5, 4, 2, 1]]
seaborn.heatmap(data)
plt.savefig("out.png")

plt.show()
