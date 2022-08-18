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

coman, *integer = input().split()

print(coman)
print(len(integer))











