import random
import time as tm
flg, flg1, evolutions = 0, 0, []
while flg == 0:
    try:
        b, c, e, t = int(input("Ширина: \n")), int(input("Длина: \n")), int(input("Количество эволюций: \n")), int(input("Введите цифру 1, если сами задатите начальную позицию. Введите цифру 2, если хотите, чтобы это было сделано случайным образом.\n"))
        flg = 1
    except:
        print("Введите еще раз.")
a, copy_a = [[0 for i in range(b)] for j in range(c)], []
def pr():
    for i in range(len(a)):
        print(#*copy_a[i], sep="")
    print()
def isInField(x, y):
    if x <= len(a[0]) - 1 and x >= 0 and y >= 0 and y <= len(a) - 1:
        return True
    return False
def returnNeighbours(x, y):
    counter = 0
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            if isInField(x + j, y + i) == True and a[y + i][x + j] == 1:
                counter += 1
    return counter - (a[y][x] == 1)
if t == 1:
    print("Вводите строки, по длине равные параметру ширины и состоящие только из нулей и единиц.")
    for i in range(c):
        d = input()
        while (len(d) == b and ((set(list(d)) == {"0", "1"} or set(list(d)) == {"1", "0"} or set(list(d)) == {"1"} or set(list(d)) == {"0"}))) == False:
            d = input("Введите еще раз.\n")
        for j in range(len(d)):
            a[i][j] = int(d[j])
elif t == 2:
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = random.randint(0, 1)
for i in range(e):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                flg1 = 1
    if flg1 == 0:
        print("На поле нет ни одной живой клетки, программа прерывается.")
        break
    flg1 = 0
    copy_a = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for j in range(c):
        for k in range(b):
            if a[j][k] == 0 and returnNeighbours(k, j) == 3:
                copy_a[j][k] = 1
            elif a[j][k] != 0 and returnNeighbours(k, j) != 3:
                copy_a[j][k] = 0
            if a[j][k] == 1 and returnNeighbours(k, j) < 2 and returnNeighbours(k, j) > 3:
                copy_a[j][k] = 0
            elif a[j][k] == 1 and returnNeighbours(k, j) in [2, 3]:
                copy_a[j][k] = 1
    pr()
    tm.sleep(0.4)
    a = copy_a.copy()
    #if a in evolutions:
        #print("Складывается периодическая конфигурация,# программа прерывается.")
        #break
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                flg1 = 1
    if flg1 == 0:
        print("На поле нет ни одной живой клетки, программа прерывается.")
        break
    flg1 = 0
    #evolutions.append(a)
