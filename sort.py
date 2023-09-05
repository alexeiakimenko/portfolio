from random import randint


def sort(a):
    if a == 1:
        return False
    j = 1
    s = 0
    while j <= a:
        if a % j == 0:
            s = s + 1
            if s > 2:
                return False
        j += 1

    return True


lst = [randint(1, 20) for i in range(11)]
print("Список:", lst)
lstp = []
lstn = []
for i in range(len(lst)):
    if sort(lst[i]):
        lstp.append(lst[i])
    else:
        lstn.append(lst[i])
print("Простые числа:", lstp)
print("Составные числа:", lstn)
print("min:", min(lstp))
print("max:", max(lstn))
