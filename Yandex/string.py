a = input(" ")
b = input(" ")
c = ''.join(set(a))


count =0

for i in c:
    for j in b:
        if i ==j:
            count += 1



print(count)




