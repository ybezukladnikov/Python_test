a, b = map(int, input().split())
temp_a = abs(a)
temp_b = abs(b)
while (temp_a * temp_b >0):
    if (temp_a > temp_b):
        temp_a = temp_a % temp_b
    else:
        temp_b = temp_b % temp_a

    nod = temp_a+temp_b

nok = int((a * b) / nod)

print(nok)
