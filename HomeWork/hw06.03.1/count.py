names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
lst = names
kol = 0
p = 1


def count(lst1):
    global p
    global kol
    p = 0
    l = []
    for i in lst1:

        if isinstance(i, list):
            p = 1
            for j in i:
                l.append(j)
        else:
            kol += 1

    return l


while True:
    if p == 1:
        lst = count(lst)
        print(lst)

    else:
        break
print(f'Количество элементов в списке {names} : {kol}.')
