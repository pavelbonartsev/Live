import time as t
import random
d = ""
while d.lower() != "стоп":
    a, b, d, c, e = "", "", " ", "", ""
    while c not in ["1", "2"] or (a.isdigit() == False or (a.isdigit() == True and int(a) <= 0)) or (b.isdigit() == False or (b.isdigit() == True and int(b) <= 0)):
        if c not in ["1", "2"]:
            c = input("1 - Автоматическая генерация, 2 - ручной ввод.\n")
        if a.isdigit() == False or (a.isdigit() == True and int(a) <= 0):
            a = input("Введите длину мира.\n")
        if b.isdigit() == False or (b.isdigit() == True and int(b) <= 0):
            b = input("Введите количество генераций.\n")
    a, b = int(a), int(b)
    if c == "1":
        e = []
        for i in range(a):
            e.append(random.randint(0, 1))
    else:
        while len(e) != a and (sorted(list(set(e)))) != [0, 1]:
            e = input("Введите мир, состоящий только из нулей и единиц, и такой, чтобы количество элементов в мире было равно введенной Вами ранее длине мира.\n")
    e = [int(i) for i in e]
    print("Стартовая генерация:", end=" ")
    for i in e:
        if i == 0:
            print(" ", end="")
        elif i == 1:
            print("*", end="")
    print()
    for _ in range(b):
        for i in range(len(e)):
            if i == len(e) - 1:
                if e[i] == 1 and ((e[i - 1] + e[0]) in [0, 2]):
                    e[i] = 0
                elif e[i] == 0 and ((e[i - 1] + e[0]) == 1):
                    e[i] = 1
            else:
                if e[i] == 1 and ((e[i - 1] + e[i + 1]) in [0, 2]):
                    e[i] = 0
                elif e[i] == 0 and ((e[i - 1] + e[i + 1]) == 1):
                    e[i] = 1
        for i in e:
            if i == 0:
                print(" ", end="")
            elif i == 1:
                print("*", end="")
        print()
        t.sleep(0.5)
    d = input("Начать генерацию заново? Нет - стоп (без учета регистра), все остальное - да.\n")
