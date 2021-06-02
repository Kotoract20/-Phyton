import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        print("Корней нет")
    else:
        print("x = {0}".format(-c/b))
else:

    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print("Корней нет")
    else:

        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)

        print('Корни уравнения x1 = {0} и x2 = {1}'.format(x1, x2))