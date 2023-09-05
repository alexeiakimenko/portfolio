from random import randint

matrix = [[randint(0, 10) for i in range(6)] for j in range(6)]
zam = [randint(0, 10) for k in range(6)]
print("Начальная матрица:")
for i in matrix:
    for j in i:
        print(j, end="\t")
    print()
print()
print(zam)
s = 0
while s < len(matrix):
    matrix[s] = zam
    s = s + 2
print("Изменённая матрица:")
for i in matrix:
    for j in i:
        print(j, end="\t")
    print()
