print("Введите х, v, и t для расчёта расстояния падения:")
x0,v0,t = (map(float,input().split()))
print("Расстояние падения: ",x0 + v0*t - (9.8*t**2/2))