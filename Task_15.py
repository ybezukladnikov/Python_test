N = int(input())
mas = []

sum = 0
for i in range(N):
    mas.append(list(map(int, input(" ").split())))

for i in range(N):
    for j in range(i, N):
        if(mas[i][j]==1): sum+=1



print(sum)
