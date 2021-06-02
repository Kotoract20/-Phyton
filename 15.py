import random

while True:
    RN = int(random.random() * 101)
    win = False

    for i in range(5):
        guess = int(input())
        if guess > RN:
            print("Число < загаданного")
        elif guess < RN:
            print("Число > загаданного")
        else:
            print("Победа")
            win = True
            break

    if not win:
        print("Поражение. Загаданное число:", RN)

    if not 1 == int(input("Ещё попытка? (1 - да)\n")):
        break