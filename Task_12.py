N = int(input())
mas = []

for i in range(N):
    mas.append(list(map(int, input().split())))

sum = 0

for i in range(N):
    x = mas[i][0]
    y = mas[i][1]
    x1 = mas[i][2]
    y1 = mas[i][3]
    x2 = mas[i][4]
    y2 = mas[i][5]
    x3 = mas[i][6]
    y3 = mas[i][7]
    x4 = mas[i][8]
    y4 = mas[i][9]


    def gipotinuzaPraym(x1, y1, x2, y2):
        return (((abs(y1 - y2)) ** 2) + ((abs(x1 - x2)) ** 2)) ** (0.5)


    a = gipotinuzaPraym(x1, y1, x2, y2)
    b = gipotinuzaPraym(x2, y2, x3, y3)
    c = gipotinuzaPraym(x3, y3, x4, y4)
    d = gipotinuzaPraym(x4, y4, x1, y1)

    plosh = a * b


    def PloshadTreug(x1, y1, x2, y2, x, y):
        a = (((abs(y1 - y2)) ** 2) + ((abs(x1 - x2)) ** 2)) ** (0.5)
        b = (((abs(y - y1)) ** 2) + ((abs(x - x1)) ** 2)) ** (0.5)
        c = (((abs(y - y2)) ** 2) + ((abs(x - x2)) ** 2)) ** (0.5)

        p = (a + b + c) / 2

        res = (p * (p - a) * (p - b) * (p - c)) ** (0.5)

        return res


    ploshVseshTreug = PloshadTreug(x1, y1, x2, y2, x, y) + PloshadTreug(x2, y2, x3, y3, x, y) + PloshadTreug(x3, y3, x4,
                                                                                                             y4, x,
                                                                                                             y) + PloshadTreug(
        x4, y4, x1, y1, x, y)

    if round(plosh)>=round(ploshVseshTreug):
        sum+=1




print(sum)




