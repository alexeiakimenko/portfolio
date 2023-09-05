vs = input("Введите по порядку,без пробелов элементы кортежа: ")
tl = tuple(vs)

lst = []
for i in range(len(tl)):
    if not tl[i] in lst:
        lst.append(tl[i])

for j in range(len(lst)):
    print("Количество", lst[j], "=", tl.count(lst[j]))
