a = int(input(" "))


count =0

while (abs(a)>1):
    if(a%2==1): count+=1
    a//=2

if a==1:
    count+=1

print(count)
