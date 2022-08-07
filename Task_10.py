a, b, c, d = map(int, input().split())

for el in range(-100, 101):
    if(a*(el**3) + b*(el**2) + c*el + d ==0): print(el, end=" ")


