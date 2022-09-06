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

N = 456
str_N = str(N)
temp = N
array =[]
array_1 = []
count = 0
while temp>0:
    dig = temp%10
    array.append(dig)
    for i in range(1,dig+1):
        if dig%i==0 : count+=1
    if count==2 : array_1.append(dig)
    count=0
    temp//=10

array.reverse()

size = len(array)
for i in range(size-2):
    for j in range(size-1-i):
        dig = int(str_N[j:j+i+2])
        array.append(dig)
        for k in range(1, dig + 1):
            if dig % k == 0: count += 1
        if count == 2: array_1.append(dig)
        count = 0




print(array)
print(array_1)



