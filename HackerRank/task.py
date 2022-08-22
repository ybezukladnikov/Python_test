# n = int(input())
#
# res = ''
# for i in range(1,n+1):
#     res+=str(i)
#
#
# print(res)


# list = [4, 5, 1, 8, 8]
# list1 = list.copy()
#
# a = max(list)
#
# for i in range(len(list)):
#     if list[i] == a: list1.remove(a)
#
# print(max(list1))
#

# n = int(input(" "))
# arr_name =[]
# arr_score =[]
# for i in range(n):
#     arr_name.append(input(" "))
#     arr_score.append(float(input(" ")))

# n = 5
# arr_name =["Tom", "Werry", "Carry", "Kate", "Lucy"]
# arr_score =[23.5, 45.3, 23.5, 45.3, 56.3]
#
# first_min = min(arr_score)
#
# arr_copy = arr_score.copy()
#
# for i in range(n):
#     if arr_score[i]==first_min:arr_copy.remove(first_min)
#
# second_min = min(arr_copy)
#
# arr_res_name = []
#
# for i in range(n):
#     if arr_score[i]==second_min:
#         arr_res_name.append(arr_name[i])
#
# arr_res_name.sort()
#
# for i in range(len(arr_res_name)):
#     print(arr_res_name[i])

# n = int(input(" "))
#
# my_dict = {}
# for i in range(n):
#     name, *line = input(" ").split()
#     val = list(map(float, line))
#     my_dict[name] = val
#
# val_key = input(" ")
# list = my_dict[val_key]
#
# sum = 0
#
# for i in range(len(list)):
#     sum+=list[i]
#
# aver = sum/3
#
# print("%.2f" % aver)

# dict={}
# array =[]
#
# n = int(input(" "))
# for i in range(n):
#     name_temp, *temp = input(" ").split()
#     val = list(map(int, temp))
#     name = str(i)+"-"+name_temp
#     dict[name]=val
#
# print(dict)
#
# for key in dict:
#     a, b = key.split("-")
#     if b == "append": array.append(dict[key][0])
#     elif b == "insert": array.insert(dict[key][0],dict[key][1])
#     elif b == "print" : print(array)
#     elif b == "pop" : array.pop()
#     elif b == "sort" : array.sort()
#     elif b == "reverse": array.reverse()
#     elif b == "remove" : array.remove(dict[key][0])
#


# x=2
# y=2
# z=2
# n=2
#
#
# mas=[]
# res = []
#
# for k in range(x+1):
#     for j in range(y + 1):
#         for i in range(z + 1):
#             mas.append([k, j, i])
#
# for i in mas:
#     if sum(i) != n: res.append(i)
#
#
# print(res)
#

# Бинарный поиск.

# from random import randint
# import math
# a=98
# b=200
# x = randint(a, b)
#
# print(x)
# i=2
# y = abs(b-a)//i
# count = 1
# while y!=x:
#
#     if x>y:
#         y = y + math.ceil((100-50)/i)
#     else:
#         y = y - math.ceil((100-50)/i)
#     i=i*2
#     count+=1
#
# print(y)
# print("счетчик =",count)

thickness=5
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+ (c * i).ljust(thickness - 1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6))

























