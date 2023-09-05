li = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
pol = []
print("Список:", li)
for i in range(len(li)):
    if li[i] > 0:
        pol.append(li[i])

print("Новый список,состоящий из положительных элементов:", pol)
sb = pol[1]
for i in range(len(pol)):
    if pol[i] > sb:
        sb = pol[i]
print("Наибольший элемент списка:", sb)
