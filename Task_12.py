# N = int(input(" "))

array = list(map(int, input("df ").split()))
array1 = list(map(int, input("df ").split()))

mas = [array, array1]

print(mas)


# x = 3
# y = 2
# x1 = 2
# y1 = 1
# x2 = 2
# y2 = 3
# x3 = 6
# y3 = 3
# x4 = 6
# y4 = 1
#
# def gipotinuzaPraym(x1, y1, x2,y2):
#
#     return (((abs(y1-y2))**2) + ((abs(x1-x2))**2))**(0.5)
#
# a = gipotinuzaPraym(x1,y1,x2,y2)
# b = gipotinuzaPraym(x2,y2,x3,y3)
# c = gipotinuzaPraym(x3,y3,x4,y4)
# d = gipotinuzaPraym(x4,y4,x1,y1)
#
# plosh = a*b
#
#
#
# def PloshadTreug(x1, y1, x2,y2,x,y):
#
#     a = (((abs(y1-y2))**2) + ((abs(x1-x2))**2))**(0.5)
#     b = (((abs(y-y1))**2) + ((abs(x-x1))**2))**(0.5)
#     c = (((abs(y - y2)) ** 2) + ((abs(x - x2)) ** 2)) ** (0.5)
#
#     p = (a+b+c)/2
#
#     res = (p*(p-a)*(p-b)*(p-c))**(0.5)
#
#     return res
#
#
# ploshVseshTreug = PloshadTreug(x1,y1,x2,y2, x,y)+PloshadTreug(x2,y2,x3,y3,x,y)+PloshadTreug(x3,y3,x4,y4,x,y)+PloshadTreug(x4,y4,x1,y1,x,y)
#
# sum = 0
#
# print(round(plosh),  round(ploshVseshTreug))
#
