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