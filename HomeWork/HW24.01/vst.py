print("Введите элементы списка: ")
li = [int(input("->")) for i in range(int(input("n=")))]

k = input("Введите индекс:")
print("k=", k)
c = input("Введите значение:")
print("c=", c)
print("Первоначальный список:", li)
li.insert(int(k), int(c))

print("Изменённый список:", li)