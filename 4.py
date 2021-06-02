a=int(input("Введите первое число "))
b=int(input("Введите второе чилсо "))

def bez(a, b):
 a, b = b, a
 print(a,b)
def C(a, b):
 c = a
 a = b
 b = c
 print(a,b)

C(a, b)
bez(a, b)
