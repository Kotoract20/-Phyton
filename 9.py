minsInHour = 60

h1, m1 = map(int, input("Введите назначенное время встречи: (Пример - ЧЧ:ММ) - ").split(sep=':'))
h2, m2 = map(int, input("Введите время прибытия - ").split(sep=':'))

m1 = minsInHour * h1 + m1
m2 = minsInHour * h1 + m2

if abs(m1 - m2) > 15:
    print('Встреча не состоится')
else:
    print('Встреча состоится')