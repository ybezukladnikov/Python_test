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
#     res = string[:position]+character+string[position+1:]
#
#     return res
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
s = input("")

a = False
b = False
c = False
d = False
e = False


for i in s:
    if i.isalnum()==True:a=True
    if i.isalpha() == True: b = True
    if i.isdigit() == True: c = True
    if i.islower() == True: d = True
    if i.isupper() == True: e = True


print(a)
print(b)
print(c)
print(d)
print(e)
