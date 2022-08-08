a, b = input().split()

bull_sum = 0
cow_sum = 0
for i in range(4):
    for j in range(4):
        if(b[j]==a[i] and j==i): bull_sum+=1
        if(b[j] == a[i] and j != i): cow_sum += 1

print(bull_sum, cow_sum)