
a = float(input("Введите взводимое в степень чилсо - "))
n = int(input("Введите степень - "))
result = 1.0

for i in range(abs(n)):
    result *= a

if n < 0:
    result = 1 / result

print(result)