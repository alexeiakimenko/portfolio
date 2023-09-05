print("Введите элементы списка: ")
list1 = [int(input("->")) for i in range(int(input("n=")))]
for i in range(len(list1)):
    if i % 2 == 0:
        print(list1[i], end=" ")
