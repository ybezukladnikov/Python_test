# Задача 1
# Введем понятие «подчисло». «Подчислом» числа N назовем число M,
# которое составлено из его цифр, путем отсекания одной или более цифр справа или слева.
# Например, «подчисла» числа 1234 – это:
#       1
#       2
#       3
#       4
#       12
#       23
#       34
#       234
#       123
#  С клавиатуры вводится натуральное число N (N>100).
#  Выяснить, сколько «подчисел» имеет число N, а также
#  сколько из них являются простыми.
# import random
# N = random.randint(1000,100000)
#
# str_N = str(N)
# size = len(str_N)
# temp = N
# array =[]
# array_1 = []
# Flag = False
#
# while temp>0:
#     dig = temp%10
#     if dig in array:
#         temp //= 10
#         continue
#     array.insert(0,dig)
#     temp//=10
#
# for i in range(size-2):
#     for j in range(size-1-i):
#         dig = int(str_N[j:j+i+2])
#         if dig in array: continue
#         array.append(dig)
#
# for el in array:
#     Flag = True
#     for i in range(2, el//2+1):
#         if el%i==0:
#             Flag = False
#             break
#     if el==1:Flag = False
#     if Flag:
#         array_1.append(el)
#
#
# print("number = ", N)
# print("Subnumbers = ", array)
# print("Prime numbers = ", array_1)



# from math import sqrt
#
#
# def IsPrime(number):
#     prime_nums = [num for num in range(
#         1, number+1) if all(num % val or val == num for val in range(2, int(sqrt(number)+1)))]
#     return number in prime_nums
#
#
# n = input('Введите натуральное число больше 100: ')
# subset = set()
# prime_subset = set()
# for i in range(0, pow(10, (len(n)-1))):
#     if str(i) in n:
#         subset.add(i)
# for i in subset:
#     if IsPrime(i) and i > 1:
#         prime_subset.add(i)
# print(f'Число {n} имеет {len(subset)} подчисел -> {subset}')
# print(f'Из них простых {len(prime_subset)} -> {prime_subset}')



N = int(input("Input number: "))

str_N = str(N)
size = len(str_N)
array =set()
array_1 = []

while N>0:
    array.add(N%10)
    N//=10

for i in range(size-2):
    for j in range(size-1-i):
        dig = int(str_N[j:j+i+2])
        array.add(dig)

for el in array:
    if el == 1 or el == 0: continue
    Flag = True
    for i in range(2, el//2+1):
        if el%i==0:
            Flag = False
            break
    if Flag:array_1.append(el)

print("Subnumbers = ", array)
print("Prime numbers = ", array_1)