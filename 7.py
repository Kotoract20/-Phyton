  
import math

def length(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


method = int(input("1 - координаты вершин; 2 - длины сторон треугольника: "))
if method == 1:
   x1, y1 = map(float, input("Введите x1, y1:").split())
   x2, y2 = map(float, input("Введите x2, y2:").split())
   x3, y3 = map(float, input("Введите x3, y3:").split())

   a = length(x1,y1, x2,y2)
   b = length(x2,y2, x3,y3)
   c = length(x3,y3, x1,y1)

   if a + b < c or b + c < a or c + a < b:
        print("Такого треугольника не существует.")
   else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S треугольника = {0}".format(s))

elif method == 2:
        a = float(input("Введите а:"))
        b = float(input("Введите b:"))
        c = float(input("Введите c:"))

        if a + b < c or b + c < a or c + a < b:
            print("Такого треугольника не существует.")
        else:
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("S треугольника = {0}".format(s))

else:
    print("Incorrect input")
    pass