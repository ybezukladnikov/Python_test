# a = input(" ")
# a = a.split()
# a = "-".join(a)
# print(a)


# def print_full_name(first, last):
#
#     print('Hello {0} {1}! You just delved into python.'.format(first,last))
#
#
# # Write your code here
#
# if __name__ == '__main__':
#     first_name = input(" ")
#     last_name = input(" ")
#     print_full_name(first_name, last_name)


# def mutate_string(string, position, character):
#     res_binar = string[:position]+character+string[position+1:]
#
#     return res_binar
#
# if __name__ == '__main__':
#     s = input(" ")
#     i, c = input(" ").split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# Поиск подстроки.
# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string)):
#         if string.find(sub_string,i,len(sub_string)+i)!= -1:
#             count+=1
#
#
#     return count
#
#
# if __name__ == '__main__':
#     string = input(" ").strip()
#     sub_string = input(" ").strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
#

# Task 3
# s = input("")
#
# a = False
# b = False
# c = False
# d = False
# e = False
#
#
# for i in s:
#     if i.isalnum()==True:a=True
#     if i.isalpha() == True: b = True
#     if i.isdigit() == True: c = True
#     if i.islower() == True: d = True
#     if i.isupper() == True: e = True
#
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# Task 4

# import textwrap
#
# def wrap(string, max_width):
#
#
#     return textwrap.fill(string,max_width)
#
# if __name__ == '__main__':
#     string, max_width = input(" "), int(input(" "))
#     result = wrap(string, max_width)
#     print(result)

# Task 5
# N, M = map(int,input(" ").split())
# c=".|."
# a = "WELCOME"
#
# for i in range(1,N,2):
#     print((c*i).center(M,"-"))
#
# print(a.center(M,"-"))
#
# for i in range(N-2,0,-2):
#     print((c*i).center(M,"-"))
#

# Task 6

# N = int(input())

N =46

res_binar = ''
res_octal= ''
res_hex = ''
for i in range(1, N+1):
    a=i
    while a >= 2:
        c = str(a % 2)
        res_binar = c + res_binar
        a = a // 2

    binar = '1' + res_binar
    res_binar =''

    b = i
    while b >= 8:
        c = str(b % 8)
        res_octal = c + res_octal
        b = b // 8

    octal = str(b) + res_octal
    res_octal = ''

    if i < 10: d=i
    if i==10: d='A'
    if i == 11: d = 'B'
    if i == 12: d = 'C'
    if i == 13: d = 'D'
    if i == 14: d = 'E'
    if i == 15: d = 'F'
    if i>15:
        d = i
        while d >= 16:
            c = str(d % 16)
            if c == 10: c = 'A'
            if c == 11: c = 'B'
            if c == 12: c = 'C'
            if c == 13: c = 'D'
            if c == 14: c = 'E'
            if c == 15: c = 'F'
            res_hex = c + res_hex
            d = d // 16



    hexad = str(d) + res_hex
    res_hex = ''



    print(str(i).rjust(2) + octal.rjust(10)+hexad.rjust(30)  + binar.rjust(40))









