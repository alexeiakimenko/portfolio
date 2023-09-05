from random import randint

lst = [randint(0, 100) for i in range(20)]
print(lst)
print("Сумма элементов списка равна:", sum(lst))
