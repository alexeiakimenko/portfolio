print("Введите элементы списка: ")
li = [int(input("->")) for i in range(int(input("n=")))]
print("Список:", li)
ch = int(input("Введите число:"))
print("ch=", ch)
sov = 0
for i in range(len(li)):
    if li[i] == ch:
        sov = sov + 1

if sov > 0:
    print("Число присутствует в элементах списка.")
else:
    print("Число отсутствует в элементах списка.")
