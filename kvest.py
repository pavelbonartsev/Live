import random
import time as t
b, c, e = int(input()), int(input()), int(input())
a = [[0 for i in range(b)] for j in range(c)]
def pr():
    for i in a:
        print(*i, sep="")
    print()
    print(returnNeighbours(1, 1))
    print()
def isInField(x, y):
    if x <= len(a[0]) - 1 and x >= 0 and y >= 0 and y <= len(a) - 1:
        return True
    return False
def returnNeighbours(x, y):
    counter = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if isInField(x + j, y + i) == True and a[y + i][x + j] == 1:
                counter += 1
    return counter - (1 * (a[y][x] == 1))

for i in range(c):
    d = input()
    #while len(d) != b and list(a).count(" ") != 0 and (set(list(a)) != {"0", "1"} or set(list(a)) != {"1", "0"}):
        #d = input("Введите еще раз.")
    for j in range(len(d)):
        a[i][j] = int(d[j])
for i in range(e):
    for j in range(c):
        for k in range(b):
            if a[j][k] == 0 and returnNeighbours(k, j) == 3:
                a[j][k] = 1
            elif a[j][k] == 1 and returnNeighbours(k, j) in [0, 1, 4, 5, 6, 7, 8]:
                a[j][k] = 0
    pr()
    t.sleep(0.4)
