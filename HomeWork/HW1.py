cifra = 56782
print("Моё число: ", cifra)
c1 = cifra % 10
cifra = cifra // 10
c2 = cifra % 10
cifra = cifra // 10
c3 = cifra % 10
cifra = cifra // 10
c4 = cifra % 10
cifra = cifra // 10
c5 = cifra % 10
print("Произведение цифр числа: ", c1 * c2 * c3 * c4 * c5)
print("Среднее арифметическое цифр числа: ", (c1 + c2 + c3 + c4 + c5) / 5)
