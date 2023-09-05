import random

d = 1
z = random.randint(1, 100)
while True:
    ch = int(input("Введите число от 1 до 100: "))
    if ch > z:
        print("Заданное число меньше")
        d += 1
    elif ch < z:
        print("Заданное число больше")
        d += 1
    else:
        break
print("Вы угадали число c", d, "раза.")
