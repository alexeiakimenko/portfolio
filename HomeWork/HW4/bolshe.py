print("Введите элементы списка: ")
li = [(int(input("->"))) for i in range(int(input("n=")))]
for i in range(len(li) - 1):
    if li[i + 1] > li[i]:
        print(li[i + 1], end=" ")
