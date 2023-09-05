# name = "Alexei"
#
# print("Hello,", name)
#
# age = 20
# print(age)

# a = 5
# print(a)
# print(type(a))
# b= "6"
# print(b)
# print(type(b))

# a = 4
# b = 5
# print(a)
# print(id(a))
# a = b
# print(a)
# print(id(a))

# a, b, c = 2, "Hello", 4.5
# print(a, b, c)
# print(id(a), id(b), id(c))
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# print("строка символов")
# print('строка символов')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + "," + s2 + "! \t \t"
#
# print(s3 * 3)
# print(757348993040506099696)
# print(7.57348993040506099696)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(6 / 4)
# print(6 // 4)
# print(6 % 4)
# print(6 // 4)

# nom = 10
# nom += 5
# print(nom)
# nom -= 3
# print(nom)
# nom *= 4
# print(nom)

# num = 7492
# print(num)
# a1 = num % 10
# print(a1)
# num = num // 10
# a2 = num % 10
# print(a2)
# num = num // 10
# a3 = num % 10
# print(a3)
# num = num // 10
# a4 = num % 10
# print(a4)
# num = 1000 * a1 + 100 * a2 + 10 * a3 + a4
# print(num)
# num = 4728
# print(num)
# res = num % 10 * 1000
# num = num // 10
# res += num % 10 * 100
# num = num // 10
# res += num % 10 * 10
# num = num // 10
# res += num % 10
# print(res)
# a = 1
# b = 2
# print("a: ", a)
# print("b: ", b)
# a,b =  b,a
# # c = a
# # a = b
# # b = c
# print("a: ", a)
# print("b: ", b)
# Функции явного преобразования типов:
# int()-приводит строку к целочисленному значению
# str()-приводит число к строковому значению
# float()-приводит строку к вещественному числу

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
# a = 3.891
#
# a = round(a, 1)
# # print(a)
# num1 = "5.2"
# nim2 = 10
# c = float(num1) + nim2
# print(c)

# name = "Alex"
# age = 44
# print("Меня зовут " + name + ".Мне", age, "года.")
# print("Меня зовут " + name + ".Мне ", age, " года.", sep="", end=" ")
# print("Я учу Python.")
# name=input("Введите имя: ")
# print("Вас зовут",name)
# num = float(input("Введите число: "))
# power = float(input("Введите степень: "))
#
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)
# num1 = int(input("1: "))
# num2 = int(input("2: "))
# num3 = int(input("3: "))
# num4 = int(input("4: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = round(sum1 / sum2, 2)
# print("Result:", round((sum1 / sum2), 2))
# b1 =  True
# b2 = False
# print(b2 + 5)


# test=5
# print(test)
# test =None
# print(test)
# print(2 + 5 == 7)
# print(2 + 5 != 7)
# print("hEllo" > "hellO")

# print(2 < 4 > 9)
# print(3*3 <= 7 >= 2)
# print(2*5 > 7 >=4 +3)
# a = 10
# b = 5
# c = a==b
# print(a,b,c)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён.")
# else:
#     print("Доступ запрещён.")

# = 5
# if a > b:
#     print("a>b")
# if b > a:
#     print("b>a")
# else:
#     print("a=b")
# a = 15
# b
# a = int(input())
# b = int(input())
# if a > b:
#     print("a>b")
# elif a < b:
#     print("a<b")
# else:
#     print("a=b")
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(N, "ВОРОНА")(N, "ВОРОНА")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if n == 0 or n > 4:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# day = "вторник"
# match day:
#     case "понедельник"|"вторник":
#         print("Рабочий день")
# case _:действие по умолчанию

# a, b = 40, 20
# print("a=b" if a == b else "a>b" if a > b else "b>a")

# try  ... except
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
#
# print("код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так")
# else:
#     print("Всё нормально.")
# finally:
#     print("Конец программы.")
# print("код далее")

# Циклы

# i = 10
# while i <=100:
#     print("i=", i)
#     i = i + 10
# i = 1
# while i <= 20:
#     print(i)
#     i = i + 2
# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапозона: "))
# res = 0
# while a <= b:
#
#     if a % 2:
#         res += a
#         print(a, "+")
#     a += 1
# print("=", res)
# n = input("Введите целое число:")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Чётное число.")
# else:
#     print("Нечяётное число.")
# i = 0
# while i < 10:
#
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён")
# res = 1
#
# while True:
#     n = int(input("Введите число:"))
#     if n == 0:
#         break
#     res = res * n
# print("Результат: ", res)
# i = 0
# while i < 4:
#     print(i)
#     i += 1
# else:
#     print("end ,i=", i)
# i = 1
# while i < 5:
#     print("Внешний цикл:i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл j=", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end='')
#         else:
#             print("-", end="")
#
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for element in collection:
#   тело цикла
# for i in "Hello":
#     print(i)
# for color in "red", "yellow", "green", "orange":
#     print(color)
# range(start,stop,step)
# for i in range(9, -1, -2):
#     print(i, end=" ")
# print()
# o = 2
# while o < 9:
#     print(o, end=" ")
#     o += 3

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0 and a != i:
#         print(i, end=" ")

# i = 0
# for i in range(1, 101):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("done!")
# w = int(input("shirina": "))
# h = int(input("vysota: "))
# s = "*"
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print(s, end="")
#
#         else:
#             print(" ", end="")
#     print()

# w = [letter * 2 for letter in "Hello"]
# print(w)
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки
# nums = [8, 3, 9, [2, 5, 7], 4, 1]
# print(nums)
# print(type(nums))

# nums = [8, 3, 9, 4, 1]
#
# print(nums)
# print(nums[1])
# print(nums[-1])
# nums[1] = 256
# print(nums[1])
# nums[3] += 100
# print(len(nums))

# s = [5, 1] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
# print(len(b))
# c = s + b
# print(c)

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(n2)

#  генератор списков
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)
# a = [0] * int(input("kolichestvo elementov: "))
#
# for i in range(len(a)):
#     a[i] = int(input("vvedite znachenie: "))
# print(a)
# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, ":", a[i])
# for i in a:
#     print(i)

# n = list(range(21, 41))
# s1 = 0
# s2 = 0
# for i in range(len(n)):
#     if i % 2 == 0:
#         s1 = s1 + 1
#     if i % 2 == 1:
#         s2 = s2 + n[i]
# print("kol=", s1, ",summa=", s2)

# a = [6, 3, 0, 8, 2]
# a[0], a[-1] = a[-1], a[0] перемена местами элементов

# срез
# список[start:stop:step]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[0:-1:2])
# print(a[::-1])
# print(a[2:20])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[3:5])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# a = "Hello"
# print(a[1:3])
# print(a[::-1])

# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a[:])
#
# del a[1:4]
# print(a)
# del-удаляет элементы

# Методы списка

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.append(99)
# # добавляет один элемент в конец списка
# print(a)
# a.extend([5, 3, 7, 9])
# # добавляет несколько элементов в конец списка
# print(a)
# a.extend("add")
# print(a)

# b = []
# for i in range(1, 11):
#     b.extend([i ** 2])
# print(b)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2,100)
# print(a)      #добавляет элемент списка(второй параметр),в определённое место(первый параметр)

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33,44,55]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a),len(b)):
#     c.append(b[i])
# print(c)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.remove(3)  # удаляет первый совпадающий элемент из списка
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаляемый элемент
# print(a)
# print(last)
# second = a.pop(0)  # удаляет элемент по индексу
# print(a)
# print(second)
# a.clear()  # очищает список
# print(a)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.pop(2)
# print(a)

# a = [5, 2, 9, 1, 2, 4, 3, 2, 4]
# num = a.count(2)  # считает количество заданных значений в списке
# print(num)
#
# ind = a.index(9)  # возвращает положение первого индекса по заданому значению
# print(ind)
# b= 2
# if b in a:
#     ind=a.index(b,4 -1)     #возвращает положение индекса первого по заданному значению

# c = [1, 2, 3]
# d = c.copy()  # создаёт копию списка в другую ячейку памяти
# print("c=", c)
# print("d=", d)
# c.append(4)
# d.insert(0, 100)
# print("c=", c)
# print("d=", d)

# a = [5, 2, 9, 1, 2, 4, 3, 2, 4]
# print(a)
# a.reverse()  # перевернули элементы в обратном порядке
# print(a)
# a.sort()  # сортирует список по возрастанию
# print(a)
# a.sort(reverse=True)  # сортирует по убыванию
# print(a)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort()
# print(s)
# s.sort(key=len)
# print(s)
# s.sort(key=len, reverse=True)
# print(s)

# b = sorted(a, reverse=True)
# print("b=", b)
# print("a=", a)

# Генерация случайных данных

# import random as r #задание нового имени модуля
#
# print(r.randint(0, 5))
# print(r.randrange(6, 16, 2))

# from random import *  # подключение отдельной функции из модуля.import.* всех функций

# print(randint(0, 5))
# print(randrange(6, 12, 2))
# print(round(uniform(10.5, 20.6), 0))
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург", "Томск"]
# print(choice(city_list))
# print(choices(city_list, k=3))
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=3))
# shuffle(s)
# print(s)


# nas = [randint(0,20) for i in range(5)]
# print(nas)

# Функции агрегирование

# lst = [19, 17, 2, 7, 17]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
# from random import randint


# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# mx = max(lst)
# print(mx)
# lst.remove(mx)
# lst.insert(0, mx)
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
#
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# mn = min(lst)
# print(mn)
# ind = lst.index(mn)
# del lst[:ind]
# print(lst)

# lst = [4]
# # if len(lst)==0:
# #     print("Clear list")
# print(bool(lst))

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("First list:", a)
# print("Second list:", b)
# c = a + b
# print("All list", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы без повторений:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Общие элементы для двух списков:", c)
#
# c = []
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальные и максимальные элементы из списков:",c)

# k = int(input("Введите длину списка:"))
# s = []
# while len(s) < k:
#     w = randint(1, k)
#     if w not in s:
#         s.append(w)
# print(s)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(m)
# # m[1] = [21, 22, 23, 24]
# # print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col]**2, end="\t\t")
#     print()


# matrix = [[x * y for x in range(1, 10)] for y in range(1, 10)]

# matrix = []
# for y in range(3):
#     new_row = []
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)

# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)


# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# s = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#         print(x, end="\t")
#     print()
# print(s)
# n = int(input("Size list:"))
# m = [[randint(0, 100) for i in range(n)] for j in range(n)]
# mn = m[1][1]
# for i in m:
#     for j in i:
#         print(j, end="\t")
#     print()
# for k in range(n):
#     if mn > m[k][k]:
#         mn = m[k][k]
# print(mn)
# print("Hello")

# import math

# num1 = math.e
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.sqrt(4)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# print(dir(math))
# from math import sqrt
#
# num1 = sqrt(9)
# print(num1)

# import math as m
# num1 = m.pi
# print(num1)

# from math import pi
#
# r = float(input("Введите радиус окружности: "))
# print("Длина окружности:", round((2 * r * pi), 2))

# import time

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# t = time.time()
# print(t)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Сегодня: %B %d(%A). %Y."))
# pause = 5
# print("Begin")
# time.sleep(pause)
# print("End")

# text = input("Название напоминания: ")
# t = float(input("Через сколько минут: "))
# t = t * 60
# time.sleep(t)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print("Hello,", name)
#
#
# hello("Boris")
# def get_sum(a, b):
#     print("Sum")
#     return a + b
#
#
# x = 3
# y = 6
# res = get_sum(x, y)
# print(res)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")
# def mat(a, b):
#     if a > b:
#         return a - b
#     if a <= b:
#         return a + b
#
#
# n1 = float(input("n1:"))
# n2 = float(input("n2:"))
# print(mat(n1, n2))

# def cub(a):
#     return a * a * a
#
#
# for i in range(1,11):
#     print(i ,"=", cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.append(b)
#     lst.insert(0, a)
#     return lst


# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))
# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 7))

# def check_password(password):
#     has_upper = False
#     has_number = False
#     has_lower = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_number = True
#     if len(password) >= 8 and has_upper and has_lower and has_number:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# print(check_password(p))
# if check_password(p):
#     print("Это надёжный пароль.")
# else:
#     print("Это не надёжный пароль!")

# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# print("result", get_sum(d=1, a=5), sep="&&")

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

# def summa(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg
#
#
# a1 = summa(2, 5, 8)
# print(a1 ** 2)

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s = s + cur_digit
#     elif not even and cur_digit % 2:
#     s = s + cur_digit
#
#
# n = (n - cur_digit) / 10
# return s
#
# print("Сумма чётных:")
# print(digits_sum(9874023))
# print(digits_sum(382271))
# print(digits_sum(123456789))
# print("Сумма нечётных:")
# print(digits_sum(9874023, False)
# print(digits_sum(382271, False)
# print(digits_sum(123456789, False)


# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
# a = 2
# b = 2
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(id(lt1))
# lt1.pop(1)
# print(id(lt1))
# lt1[1] = "Hello"

# s = "Hello"
# print(id(s))
# s += "World"
# print(id(s))

# a = 5
# print(id(a))
# a = a + 1
# print(id(a))

# def add_number(n):
#     print(n, "=", id(n))
#     n1 = n + [4]
#     print(n1, "=", id(n1))
#
#
# x = [1, 2, 3]
# print("x:", x, id(x))
# add_number(x)
# print("x:", x, id(x))

# кортеж (tuple)
# lst = [1, 2, 3]
#
# # print(lst.__sizeof__())
# # print(tpl.__sizeof__())
# print(type(tpl))
# a = ()
#
# b = tuple()
# print(type(b))
# a = (1,)
# print(a)
# print(type(a))
# b = tuple(("Hello"))
# print(b)
# print(type(b))
# c = c + 4,
# print(c)
# tpl = (1, 2, 3, 5, 6, 7, 8, 9)
# print(tpl)
# print(tpl[2])
# print(tpl[1:3])
# from random import randint

# s = tuple(2 ** i for i in range(1, 13))
# print(s)
# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(len(t3))
# print(t3.count("l"))
# print(t3.index("l", 4))

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tpl(n1, n2):
#     return tuple(randint(n1, n2) for _ in range(10))
#
#
# tl1 = tpl(0, 5)
# tl2 = tpl(-5, 0)
#
# print(tl1)
# print(tl2)
# tl3 = tl1 + tl2
# print(tl3)

# t = (10, 11, [1, 2, 3], ["hello", "world"])
# print(t, id(t))
# t[3][0] = "new"
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)
# t = (1, 2, 3)
# del t
# print(t)


# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst2 = list(tpl)
# print(type(lst2))
# print(lst2)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country


# Множество(set)

# s = {}
# print(s)
# print(type(s))
# lst=list(s)
# print(lst)

# a = set(["banana", "apple", "orange"])
# print(type(a))
# print(a)

# s = {i * i * i for i in range(10)}
# print(s)

# str1 = "я обычная строка"
# str2 = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
#
#
# def to_set(a):
#     return set(a)
#
#
# print(to_set(str1), len(to_set(str1)))
# print(to_set(str2), len(to_set(str2)))

# t = {"red", "green", "blue"}
# for i in t:
#     print(i)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = {i for i in lst if "a" not in i}
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"}
# print(a)

# users = {"Tom", "Alice", "Bob"}
# users.add("Ann")
# print(users)
# # user = "Rob"
# # if user in users:
# #     users.remove(user)
# #
# # print(users)
# # users.discard("Rob")
# # print(users)
# # users.pop()
# # print(users)
# users.clear()
# print(users)

# a = {1, 2, 3, 4, 5}
# b = {0, 4, 5, 6, 3}
# # c = a | b
# # c = a<b
# print(c)
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 |s6 | s7
#
# print(s)
# print(min(s))
# print(max(s))


# str1 = "Hello"
# str2 = "How are you"
# s1 = set(str1)
# s2 = set(str2)
# # # s = s1 | s2
# s3 = s1 & s2
# # print(s3)
# for i in s3:
#     print(i, end=" ")
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one = drawing ^ music
# print(one)
# both = drawing & music
# print(both)
# s1= one-both

# frozenset(замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello","world"})
# print(a)


# Словарь(dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(d)

# d = {"one": 1, "two": 2}
#
# print(d)
# print(type(d))
#
# d1 = dict(one=1, t=2)
# print(d1)
# d = {"one": 1, "two": 2, "three": 3}
# print(list(d))
# # lst = ["one", "two", "three"]
# # print(dict(lst))
#
# a = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
# print(a)
# print(dict(a))

# d = {"one": 45, 0: "text", (1, 2, 3): "Кортеж", 43: [1, 2, 3, 4]}
# print(d[0][1])

# d = {input("key"): randint(1, 10) for i in range(3)}
# print(d)

#
# # print(d)
# # d["two"] = 200
# # d["one"] += 100
# print(d)
# del d["two"]
# print(d)
# for key in d:
#     print(key, ":", d[key])

# d = {i: input("Введите элемент словаря: ") for i in range(1, 5)}
# print(d)
# de = int(input("Введите ключ удаляемого элемента: "))
# try:
#     del d[de]
# except KeyError:
#     print("Такого ключа нет!")
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")
# while True:
#     n = input("№: ")
#     if n != "0":
#         qty = int(input("Количество:"))
#         goods[n][1] += qty
#     else:
#         break
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")

# d = {"a": 1, "b": 2, "c": 3}
# d2 = d.copy()
# print("D=", d)
# print("D2=", d2)
# d["b"] = 5
# print("D=", d)
# print("D2=", d2)
# d2["e"] = 7
# print("D=", d)
# print("D2=", d2)

# # print(d["b"])
# # value = d.get("b","nokey")
# # print(value)
# print(d.keys())  # ключи
# print(d.values())  # значения
# print(d.items())  # ключи + значения
# for k, v in d.items():
#     print(k, v)

#
# print(d)
# # item = d.pop("b")
# # # item = d.popitem()
# #
# # print(item)
# # d.clear()
# # item = d.setdefault("e", 100)  #устанавливает значение по умолчанию
# d.update([("r", 7), ("c1", 6)])  # преобразует словарь
# d.update({"y": 65, "n": 64})
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = {}
# # z.update(x)
# # z.update(y)
# z = x | y
# print(z)

#
# d2 = dict()
# d2['name'] = d1.pop('name')
# d2['salary'] = d1.pop('salary')
#
# print(d1)
# print(d2)

# d1 = {"name": "Kelly", 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d1['location'] = d1.pop('city')
# print(d1)
# a = {
#
#     "first": {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: "four",
#         5: "five"
#     }
#
# }
# print(a)
#
# sales = {
#     "Jhon": {"N": 3056, "S": 8463, "E": 8441, "W": 2594},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 4578, "E": 8441, "W": 2594}
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep="")
# person = input("Name: ")
# region = input("Region: ")
# print(sales[person][region])
# new_data = int(input("New money: "))
# sales[person][region] = new_data
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep="")

#
# print({key: value for key, value in d.items()})

# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# k = ''
# for i in lst:
#     if type(i) == str:
#         k = i
#         d[k] = []
#     else:
#         d[k].append(i)
# print(lst)
# print(d)

# zip() объединяет структуры данных

# a = [12, 1, 2, 3]
# b = ['Dec', 'Jan', 'Feb', 'March']
# c = [4.0, 8.5, 4.9, 7.3]
# d = dict(zip(a, b))
# print(d)
# f = {k: v for k, v in zip(b, a)}
# print(f)
# f = list(zip(a, b,c))
# print(f)
#
# dic2 = {'name': 'Irina', 'email': 'irina@mail.com', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(dic1.items(), dic2.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# d = {"b": 2, "a": 4, "d": 1, 'c': 3}
# e = list(d.items())
# print(e)
# n, m = zip(*e)
# print(n)
# print(m)
# c = list(zip(m, n))
# print(c)
# c.sort()
# print(c)
# c = {v: k for k, v in c}
# print(c)

# month = ['January', 'February', 'March']
# total_sales = [52000, 51000, 48000]
# prod_cost = [46800, 45900, 43200]
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)

# one = {'a': 1, 'b': 2, 'c': 55}
# two = {'c': 3, 'd': 4}
# print({**one, **two})

# data = ['red', 'green', 'blue']
# ind = 1
# for i in data:
#     print(ind, i)
#     ind += 1
# print("")
# for n, i in enumerate(data, 1):
#     print(n, i)

# dic1 = {'name': 'Igor', 'email': 'igor@mail.com', 'job': 'Consultant'}
# for i, v in enumerate(dic1.values(), 1):
#     print(i, ')', ": ", v, sep='')

# def func(*args):
#     return (args)
#
#
# print(func(5))
# print(func(5, 3))
# print(func(5, 3, 2, 7))


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return (res)
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 4, 5))


# def to_dict(*args):
#     return {k: k for k in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))


# def func(*args):
#     res = 0
#     d = 0
#
#     for i in args:
#         res += i
#         d += 1
#     sra = res / d
#
#
#     return [x for x in args if x < sra]
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
#
#
# def func(a, *args):
#     return (a, args)
#
#
# print(func(3, 5, 6, 7, 2))

# def print_scores(student, *scores):
#     print('\nStudent name:', student)
#     for score in scores:
#         print(score, end=' ')
#
# print()
# print_scores("Jon", 10, 95, 88, 92, 99)
# print_scores("Mike", 96, 20, 33, 56)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# d = func(f=5, e=6, m=9)
# print(d)

# def intro(**data):
#     for k,v in data.items():
#         print(k,"is",v)
#     print()
#
#
#
# intro(name='Irina',surname='Sharma',age=22)
# intro(name='Igor',surname='Wood',email='igor@mail.com',age=22,phone=89523454437)

# dic = {'one': 'first'}


# def db(**kv):
#     # global dic
#     # dic = dic | kv
#     dic.update(kv)
#     return dic
#
#
# db(k1=22, k2=31)
# print(dic)
# def func(*args):
#     print(args[0])
#
#
# func(4, 6, 7, 5, 3)

# def func(first, *arg, c=100, **kv):
#     return first, arg, c, kv
#
#
# print(func(5, 4, 8, 9, 7, a=6, b=2))

# Области видимости(scope)

# name = 'Tom'
#
#
# def hi():
#     global name, surename
#     name = 'Sam'
#     surename = "Jhonson"
#     print("Hello", name, surename)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)
# print(surename)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# x = 20
#
#
# def ad(a):
#     # x = 2
#
#     def ad2():
#         # x = 8
#         return a + x
#
#     return ad2()
#
#
# print(ad(3))
# import builtins
# names = dir(builtins)
# for t in names:
#     print(t)

# min1 = 23
# a = [4, 5, 7, 8, 9]
#
# print(min1)
# print(a)
# print(min(a))
# print(max(a))
# print(sum(a) / len(a))

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func('World!')

# def func1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print("Summa:", a + b)
#
#     print('a=', a)
#
#     func2(c)
#
#
# func1()

x = 25

# t = 0


# def fn():
#     global t
#     a = 30
#
#     def inf():
#         nonlocal a
#         a = 35
#
#     inf()
#     t = a
#
#
# fn()
# z = x + t
# print(z)

# def f1():
#     x = 25
#
#     def f2():
#         # x = 33
#
#         def f3():
#             nonlocal x
#             x = 55
#
#         f3()
#         print('f3:', x)
#
#     f2()
#     print('f2:', x)
#
#
# f1()
# print('f1:', x)

# def outf(a1, a2, b1, b2):
#     a = 0
#     b = 0
#
#     def inf():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inf()
#     return [a, b]
#
#
# print(outf(2, 3, 5, 7))


# Замыкание
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(6))
# add2 = outer(5)
# print(add2(18))
# print(outer(5)(4))


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Fiona': 35,
#     'Grace': 69
#
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(80, 101)
# B = make(70, 80)
# C = make(50, 70)
# D = make(0, 50)
# print('A:',A(students))
# print('B:',B(students))
# print('C:',C(students))
# print('D:',D(students))

# Анонимные функции(lambda)

# print((lambda x, y: x + y)(6, 3))
# print((lambda a, b: a ** 2 + b ** 2)(int(input('a=')), int(input('b='))))

# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7))
# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
# for t in c:
#     print(t('abc_'))
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(6))
# add2 = outer(5)
# print(add2(18))
# print(outer(5)(4))
#
#
# def out1(n):
#     return lambda x: n + x
#
#
# add2 = out1(5)
# print(add2(10))
#
# out2 = lambda n: lambda x: x + n
# add3 = out2(5)(6)
# print(add3)

# print('sum=', (lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))
# d = {'d': 10, 'b': 15, 'c': 4}
# a = sorted(d)
# print(a)
# lst = list(d.items())
# print(lst)
# lst.sort()
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d = dict(lst)
# print(d)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Фёдор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семёнов', 'rating': 6},
#
# ]
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'],reverse=True)
# print(res)


# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[2](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x * (-1), 'three': lambda x: x ** 5}
# b = [-3, 10, 0, 4]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d= {
#     1:lambda:print('Monday'),
#     2:lambda:print('day2'),
#     3:lambda:print('day3')
# }
# d[2]()

# print((lambda a, b: a if a > b else b)(5, 3))
# print((lambda a, b, c: a if (a < b and a < c) else b if b < c else c)(5, 8, 2))

# map(func,iterables),filter(func,iterables)-ЦИКЛЫ

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, 6, -3]
# #
# # a = list(map(mult, lst))
# # print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a1)


# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(int, t))
# print(t2)
# areas = [3.76748, 45.5425263, 65.6345637, 4.626277, 7.736356436, 5.64733]
# print(list(map(round, areas, range(1, 7))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = list(map(lambda a, b: (a ** b), l1, l2))
# print(l3)

# t = ('abcd', 'abc', 'cdrfg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t)
# print(t2)
#
# b = [66, 34, 89, 23, 88, 35, 28, 46, 98]
# res = list(filter(lambda s: s > 75, b))
# print(b)
# print(res)

# from random import randint
#
# l = [randint(1, 40) for i in range(10)]
# print(l)
# l2 = list(filter(lambda a: 10 <= a <= 20,l))
# print(l2)

# print(list(map(lambda a: a ** 2, filter(lambda a: a % 2, range(10)))))

# Декораторы

# def h():
#
#
#
# def sfunc(f):
#     print('Hello I am super func!')
#     print(f())
#
#
# sfunc(h)


# def hello():
#     return 'Hello I am func "hello"'
#
#
# test = hello
# print(type(test))
# print(test())

# def my_decorator(func):
#     def funcwrap():
#         print('Код до функции')
#         func()
#         print('Код после функции')
#     return funcwrap
#
#
# @my_decorator
# def functest():
#     print('Тело функции "funct"')
# #
# # # test = my_decorator(funct)
# # # test()
# functest()
#
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
#
# def hello():
#     return 'text'


# print(hello())
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print('Меня зовут', name, surname)
#
#
# print_full_name('Ирина', 'Леонова')

# def args_decorator(fn):
#     def wrap(*arg1, **arg2):
#         print(arg1, arg2)
#         fn(*arg1, **arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study1='Python'):
#     print(a, b, c, 'изучают', study1, '\n')
#
#
# print_full_name('Ирина', 'Борис', 'Svetlana')
# print_full_name('Jhon', 'mike', 'Nick')
# def decor(arg1, arg2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма", '+')
# def sum(a, b):
#     print(a + b)
#
#
# @decor("Разность", '-')
# def sub(a, b):
#     print(a - b)
#
#
# sum(float(input('x=')), float(input('y=')))
# sub(float(input('x=')), float(input('y=')))

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 10))
# print(int('100', 16))
# print(0c01001)
# print(0x23)
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e*4)
# print("Py" in e)
# s = 'Hello'
# print(s[1])
# print(s[-3])
# print(s[1:4])
# print(s[::-1])

# str2
# print(s[3])
# s[3] = 't'
# print(s)
# s = s[:3] + 't' + s[4:]
# print(s)
# def change_to_str(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
#
# print('str1:', str1)
# str2 = change_to_str(str1, 'N', 'P')
# print('str2:', str2)

# print('Hello')
# print(u'Hello')
# print(r'Hello'+'\\')
# name = "Dmitry"
# age = 25
# print('My name is', name, "age", age)
# print(f'My name is {name}.Age: {age} old.')

# from math import pi
#
# print(f'Число PI:{round(pi, 3)}')
# print(f'Число PI:{pi:.3f}')
# x = 10
# y = 5
# print(f'{x =},{y =}')
# print(f'{x} x {y} / 2 ={x * y / 2}')
# a = 74
# print(f'{{{a}}}')
# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# s = ""
# s1 = ''
# s2 = """Много
# строк"""
# s3 = ''''''
# print(s2)

# def square(n):
#     '''Принимает число n,возвращает квадрат числа n'''
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# from math import pi
#
#
# def sc(r, h):
#     """
#     Вычисляет площадь цилиндра.
#     Вычисляет площадь цилиндра на основании высоты т радиуса основания.
#
#     :param r: Положительное число, радиус основания.
#     :param h: Положительное число, высота цилиндра.
#     :return: Площадь поверхности цилиндра.
#     """
#
#     return (2 * pi * r * h) + (2 * pi * r ** 2)
#
#
# print(sc(5, 8))
# print(sc.__doc__)


# print(ord('a'))
#
# while True:
# my_str = 'Test string for me '
# arr = [ord(i) for i in my_str]
# print('ASCII коды:', arr)
# arr1 = sum(arr) / len(arr)
# arr1 = [round(arr1)] + arr
# print('Среднее арифметическое:', arr1)
# arr1 += [ord(x) for x in input('->')[:3] if ord(x) not in arr]
# print(arr1)
# print(arr1.count(arr1[-1]) - 1)
# arr1.sort(reverse=True)
# print(arr1)
# print(chr(97))
# print(chr(1008))
# i = 97
# while i <= 122:
#     print(f'{chr(i)} {i}',end=' ')
#     i += 1

# print('apple' == 'Apple')
# print('apple' > 'Apple')


# from random import randint
#
# short = 7
# long = 10
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(min_ASCII, max_ASCII))
#         res += rand_char
#
#     return (res)
#
#
# print('Случайный пароль:', random_password())

# print(dir(str))

# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())

# print(s.lower().count('he'))  # подсчёт вхождений подстроки

# print(s.find('h'))  # возвращает первый индекс соответствующий началу подстроки -1 если нет
# print(s.rfind('h'))  # возвращает первый индекс соответствующий началу подстроки -1 если нет
# print(s.index('o'))  # возвращает первый индекс соответствующий началу подстроки ValueError если нет
# print(s.rindex('o'))  # возвращает первый индекс соответствующий началу подстроки ValueError если нет

# s = input('->')
# ind = s.find(' ')
# print(ind)
# s = s[ind + 1:] + ' ' + s[:ind]
# print(s)


# s1 = 'ab12c59p7dq'
# digits = []
# for symbol in s1:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))

# print(digits)


# st = "the original words and form a written or printed work"
# ch = 'o'
# if st.count(ch) == 1:
#     print(st.find(ch))
# elif st.count(ch) >= 2:
#     print(st.find(ch), st.rfind(ch))

# s = 'hello,WORLD!I am learning Python.'
# print(s.endswith('on.'))
# print(s.startswith('he'))

# print('abc123'.isalnum())  # определяет состоит ли строка из букв и цифр
# print('abcADF'.isalpha())  # только буквы
# print('123'.isdigit())  #только цифры
# print('abc'.islower())  # в нижнем регистре
# print('SDF'.isupper())  # в верхнем регистре
# print('py'.center(10, '*'))  # выравнивает по центру
# print('    py'.lstrip())
# print('py     '.rstrip())
# print('    py    '.strip())

# print('http://www.python.org'.lstrip('/:pths'))


# str1 = 'Я изучаю Nython.Мне нравится Nython.Nython очень интересный язык прогаммирования.'
# print(str1)
# print(str1.replace('Nython', 'Python', 2))
# str1 = str1.replace('Nython', 'Python')
# print(str1)

# s = 'Заменить в этой строке все буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(s)
# a = s[:s.find('о') + 1]
# b = s[s.rfind('о'):]
# c = s[s.find('о') + 1:s.rfind('о')]
# s = a + c.replace('о', 'О') + b
# print(s)


# s = '-'
# st = ('a', 'b', 'c')
# print(s.join(st))
# print('..'.join(st))
# print('**'.join(['1', '2', '3']))
# print('*'.join('Alex'))
# print('A*l*e*x'.split('*'))
# print('www.python.org.ru'.split('.', 2))
# print('alex akim'.split())
# a = input('->').split(',')
# print(a)

# s = input("->").split()
# print(f'{s[0].capitalize()} {s[1][0].upper()}.{s[2][0].upper()}.')


# Регулярные выражения
# import re

# # reg = '[12][0-9][0-9][0-9]'
# # reg = '[A-Za-z]'
# # reg = '[A-Z 0-9.\[\]-]'
# reg =r'[!]'
# print(re.findall(reg, s))
# print(ord('Я'))
# print(ord('а'))
# print(chr(96))

# s = 'Час в 24-формате от 00 до 23.2021-06-15Т21:45.Минуты,в диапазоне 00 до 59.2021-06-15Т01:09'
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

#
# reg = r'20+'
# print(re.findall(reg, s))
#
# d = 'Цифры : 7, +17, -42, 0012, 0.3'
# print(re.findall(r'[+-]?\d+[.\d]*', d))
# s = '06-03-1987 #Дата рождения'
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s)))

# s = 'author=Пушкин  А.С.; title = Евгений Онегин; price =200; year= 1831 '
#
# # reg = r'\w+\s*=\s*\w+[\s\w.]*'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))


# s = '12 сентября 2021 года 4567489495005'
# reg = r'\d{1,4}'
# print(re.findall(reg, s))
# s = '+7 499 456-46-78,+74994564578,+7 (499) 456 45 78,74994564578'
# reg=r'\+?7\d{10}'
# print(re.findall(reg, s))

# reg = r'\w+\.$'
# print(re.findall(reg, s))

# def validate_login(name):
#
#     return re.findall(r'^[A-Za-z0-9_-]{3,16}$',name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Pyt'))
# print(validate_login('Pyt5'))
# print(validate_login('Pyt5$$$'))


# print(re.findall(r'\w+', '10 +й'))
# print(re.findall(r'\w+', '10 +й', flags=re.ASCII))
# print(re.findall(r'\w+', '10 +й', flags=re.A))
# print(re.findall(r'\w+', '10 +й', re.A))
# text = "Hello world"
# print(re.findall(r'\w\+', text,re.DEBUG))

#
# reg = r'я'
# print(re.findall(reg,s,re.IGNORECASE))
# text = '''
# one
# two
# '''
# # print(re.findall(r'one.\w', text))
# # print(re.findall(r'one.\w+', text, re.DOTALL))
# # print(re.findall(r'one.\w+', text, re.S))
# print(re.findall('one$', text))
# print(re.findall('one$', text, re.MULTILINE))
# print(re.findall('one$', text, re.M))

# print(re.findall("""
# [a-z.-]+       #part1
# @              #@
# [a-z.-]+"""    #part2
#                  ,'test@mail.ru',re.VERBOSE))
# text = ''''
# Python
# python
# PYTHON
# '''
# reg = r'(?im)^python'
# print(re.findall(reg, text))


# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall("<.*?>", text))

# reg = r'\d{,}'
# print(re.findall(reg, s))

# s = '<p>Изображение <img src="bg.jpg">-фон страницы</p>'
# # reg = r'<img.*?>'
# # reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = "Пётр,Ольга и Виталий отлично учатся!"
# reg = "Пётр| Ольга |Виталий"
# print(re.findall(reg, s))

# s = "int = 4,float = 4.0,double = 8.0f"
# # reg = r'int\s*=\s*\d[.\w]*|double\s*=\s*\d[.\w]*'
# reg = r'((?:int|double)\s*=\s*(?:\d[.\w]*))'
# print(re.findall(reg, s))


# () -сохраняющие скобки
# (?:)-несохраняющие скобки


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d*)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))


# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))


# s = 'Я ищу совпадения в 2023 году.И я их найду в два счё_та.749357944.Hello.'
# reg = r'(\d+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s))
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


text = """
Самара
Москва
Тверь
Уфа
Казань
"""


# count = 0
#
#
# def repl_count(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print('<select name="city">')
# print(re.sub(r'\s*(\w+)\s*', repl_count, text))
# print('</select>')


# s = "Самолёт прилетает 10/23/2021.Будем рады вас видеть после 10/24/2021."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'yandex.ru and yandex.com'
# reg = r'(([a-z0-9]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# Рекурсия

# def elevator(n):
#     if n == -3:
#         print('Вы в подвале.')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n ** n, end=' ')
#
#
# n1 = int(input('На каком вы этаже?'))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res+=i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     print(lst[0])
#     if len(lst) == 1:
#
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(2546547,11))

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# # print(len(names))
# # print(names[0])
# # print(isinstance(names[0], list))
# # print(names[1][0])
# # print(isinstance(names[1][0], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0]+remove(text[1:])
#
#
#
# print(remove('       Hello\t,World !'))

# Файлы

# f = open(r'E:\учёба\python\text.txt')
# print(f)
# print(*f)
# d = open('text.txt', mode='r')
# print(d)
# print(*d)
# print(d.mode)
# print(d.encoding)
# print(d.name)
# print(d.closed)
# print(f.name)
# f.close()
# d.close()
# print(d.closed)

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test.txt')
#
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt')
#
# print(f.readlines())
#
# f.close()

# f = open('test.txt')
# kol = 0
# for line in f:
#     print(line)
#     kol += 1
# print(kol)
#
# f.close()


# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld!\n')
# f.close()
# f = open('xyz.txt', 'a')
# f.write('New text')
# line = ['This is line1', 'This is line 2']
# f.writelines(line)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [i ** 5 for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(str(index) + '\n')
# f.close()
# f = open('text2.txt', 'w')
# f.write('Заменить строку в текстовом файле;\n')
# f.write('Изменить строку в списке;\n')
# f.write('Записать список в файл;\n')
# f.close()
# f = open('text2.txt', 'r')
# lst = f.readlines()
# while True:
#     ind = int(input('->'))
#     if 1 <= ind <= 3:
#         break
#     else:
#         print("Заново")
#
# print(lst)
# f.close()
# f = open('text2.txt', 'w')
# lst[ind - 1] = 'pos = ' + str(ind)
# f.writelines(lst)
# f.close()

# f = open('text.txt','w')
# f.write('Hello!!!')
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())  # Возвращает позицию курсора в файле.
# print(f.seek(1))  # Переместил курсор в заданную позицию.
# print(f.read())
# f.close()

# f = open('text1.txt', 'a+')
# print(f.write('\nI am learning Python.'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()
# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line)
# def get_line(lt):
#     lt = list(map(str(lt)))
#     return " ".join(lt)


# file_name = 'res.txt'
# # lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# # with open(file_name, 'w') as f:
# #     for i in lst:
# #         f.write(str(i)+' ')
# # print('Done!')
#
# with open(file_name, 'r') as f:
#     rf = f.read().split(' ')
#     print(rf, len(rf))
#     print(sum(map(float, rf[:-1])))
# def longest_word(file):
#     with open(file, encoding='UTF-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#
#         return res
#
#
# print(longest_word('test.txt'))

# text = "Строка№1\nСтрока№2\nСтрока№3\nСтрока№4\nСтрока№5\nСтрока№6\nСтрока№7\nСтрока№8\nСтрока№9\nСтрока№10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = "two.txt"
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)
# with open('one.txt', 'r') as f1, open('two.txt', 'r') as f2, open('three.txt', 'w') as f3:
#     for ln1, ln2 in zip(f1, f2):
#         f3.write(ln1)
#         f3.write(ln2)

# Модули OS и OS.PATH

# import os
# import os.path


# print("Текущая директория:", os.getcwd()) # возвращает путь к текущей директории
# print(os.listdir()) # возвращает файлы и папки из текущей директории
# print(os.listdir('..'))
# os.mkdir("folder")  # создание папки
# os.makedirs('nested1/nested2/nested3') # создание папок
# os.rmdir('folder') # удаление пустой папки
# os.remove('xyz.txt') # удаляет файл
# os.rename('two.txt','new.txt') # переименование файлов и папок
# os.rename('new.txt', 'directory/two.txt') # пермещает файл по заданному пути который уже существует
# os.rename('three.txt', 'directory/three.txt')
# os.renames('text2.txt', 'test/text2/txt') # перемещает файл в создаваемые папки


# for root, dirs, files in os.walk('\учёба'):
#     print('Root:', root)
#     print('Sub dirs:', dirs)
#     print('Files:', files)

# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветке {root_tree}.')
#     print('-' * 50)
#     for root, dirs, file in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#     print('-' * 50)
#
#
# remove_empty_dirs('nested1')

# print(os.path.split(r'E:\учёба\python\test\text2\txt2.txt'))  # разбивает путь на кортеж
#
# print(os.path.dirname(r'E:\учёба\python\test\text2\txt2.txt'))
# print(os.path.basename(r'E:\учёба\python\test\text2\txt2.txt'))


# print(os.path.join('E:\учёба', 'pyton', 'test', 'text2', 'txt2.txt'))


# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
# files = {
#     'Work': ["w.txt"],
#     r"Work\F1": ["f11.txt", 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         print(file_path)
#         open(file_path, 'w').close()
# files_width_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_width_text:
#     with open(file, 'w') as f:
#         f.write(f'Некоторый текст для документа:{file}.')

# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху вниз." if topdown else "снизу вверх."}')
#     for r, d, f in os.walk(root, topdown):
#         print(r)
#         print(d)
#         print(f)
#     print('*' * 50)
#
#
# print_tree('Work', False)
# print_tree('Work', True)

# print(os.path.exists(r'E:\учёба\python\test\text2\text2.txt')) # возвращает True если файл существует
# import time
#
# p = r'E:\учёба\python\test\text2\txt2.txt'
# # print(os.path.getsize(p))  # возвращает размер файла
# # print(os.path.getmtime(p))  # возвращает время последнего изменения файла
# # print(os.path.getatime(p))  # возвращает время последнего доступа к файлу
# # print(os.path.getctime(p))  # возвращает время создания файла
# #
# # atime = os.path.getctime(p)
# # print(time.strftime('%d.%m.%Y, %H:%M:%S',time.localtime(atime)))
#
# print(os.path.isdir(p))  # возвращает True,если путь является директорией
# print(os.path.isfile(p)) # возвращает True,если путь является файлом


# print(type(p1))
# print(p1.x)
# print(Point.__doc__)
# print(dir(Point))
# class Point:
#     """Координаты точки"""
#     x = 1
#     y = 2


# p1 = Point()
# Point.x = 100
# p1.x = 30
# p1.y = 87
# p1.z = 13
# print(p1.x)
# print(p1.y)
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p1.__dict__)

# class Point:
#     x = 4
#     y = 6
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(x + y)
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# p2 = Point()
# p2.set_coord(20, 40)
# Point.set_coord(p1, 70, 90)
class Human:
    name = 'name'
    birthday = '00.00.0000'
    phone = '00-00-00'
    country = 'country'
    city = 'city'
    adress = 'street, house'

    #     def print_info(self):
    #         print('Персональные данные'.center(40, '*'))
    #         print(f'Имя: {self.name}')
    #         print(f'Дата рождения: {self.birthday}')
    #         print(f'Номер телефона: {self.phone}')
    #         print(f'Страна: {self.country}')
    #         print(f'Город: {self.city}')
    #         print(f'Домашний адрес: {self.adress}')
    #         print('=' * 40)
    #
    #     def input_info(self, firstname, birthday, phone, country, city, address):
    #         self.name = firstname
    #         self.birthday = birthday
    #         self.phone = phone
    #         self.country = country
    #         self.city = city
    #         self.adress = address
    #     def get_city(self):
    #         return self.city
    #
    # h1 = Human()
    # h1.print_info()
    # h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный 2-97')
    # h1.print_info()
    # h1.city='Саратов'
    # h1.print_info()
    # print(h1. get_city())
    # class Person:
    #     skill = 10  # статическое свойство
    #
    #     def __init__(self, name, surname):
    #         self.name = name  # динамическое свойство
    #         self.surname = surname
    #
    #     def print_info(self):
    #         print("Данные сотрудника:", self.name, self.surname)
    #
    #     def add_skill(self, k):
    #         self.skill += k
    #         print('Квалификаация сотрудника:', self.skill)
    #         print('=' * 50)
    #
    #
    # p1 = Person(input('name'), input('surname'))
    # p1.print_info()
    # p1.add_skill(3)
    #
    # p2 = Person('Anna', 'Dolgih')
    # p2.print_info()
    # p2.add_skill(2)

    #     def __del__(self):
    #         print('Удаление экземпляра.')
    #
    #
    #
    # print(p1.__dict__)

    # class Point:
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y

    #     def set_coord(self, x, y):
    #         if isinstance(x, int) and isinstance(y, int):
    #             self.x = x
    #             self.y = y
    #
    #         print(self.x,self.y)
    #
    #
    # p1 = Point(5, 10)
    # p1.set_coord(45, 64)

    # class Point:
    #     count = 0

    #     def __init__(self, x=1, y=1):
    #         self.x = x
    #         self.y = y
    #         Point.count += 1
    #
    #
    # p1 = Point()
    # print('p1', p1.count)
    # print('Point', Point.count)
    # p2 = Point()
    # print('p2', p2.count)
    # print('Point', Point.count)
    # p3 = Point()
    # print('p3', p3.count)
    # print('Point', Point.count)

    # class Robot:
    #     k = 0
    #
    #     def __init__(self, name):
    #         self.name = name
    #         print("Инициализация робота:", self.name)
    #
    #     def __del__(self):
    #         print(self.name, 'выключается.')
    #         Robot.k -= 1
    #         print('Численность роботов', Robot.k)
    #
    #     def say_hi(self):
    #         print('Приветствую!Меня зовут', self.name)
    #         Robot.k += 1
    #
    #
    # droid1 = Robot('R2-D2')
    # droid1.say_hi()
    # print('Численность роботов', Robot.k)
    # print('*' * 50)
    # droid2 = Robot('C-3PO')
    # droid2.say_hi()
    # print('Численность роботов', Robot.k)

    # class Point:
    #     def __init__(self, x, y):
    #         self.__x = x
    #         self.__y = y
    #
    #     def __cvalue(z):
    #         if isinstance(z, int) or isinstance(z, float):
    #             return True
    #         return False
    #
    #     def set_coord(self, x, y):
    #         if Point.__cvalue(x) and Point.__cvalue(y):
    #             self.__x = x
    #             self.__y = y
    #
    #     def get_coord(self):
    #         return self.__x, self.__y
    #
    #
    # p1 = Point(5, 10)
    # print(p1.get_coord())
    # print(p1.x, p1.y)
    # p1.x = 100
    # p1.y = 'abc'
    # print(p1.x, p1.y)
    # import math
    #
    #
    # class Rectangle:
    #     def __init__(self, lenght=1, width=1):
    #         self.__lenght = lenght
    #         self.__width = width
    #
    #     def __cvalue(z):
    #         if isinstance(z, int) or isinstance(z, float):
    #             return True
    #         return False
    #
    #     def set_width(self, w):
    #         if Rectangle.__cvalue(w):
    #             self.__width = w
    #
    #     def set_lenght(self, lg):
    #         if Rectangle.__cvalue(lg):
    #             self.__lenght = lg
    #
    #     def get_width(self):
    #         return self.__width
    #
    #     def get_lenght(self):
    #         return self.__lenght
    #
    #     def get_area(self):
    #         return self.__width * self.__lenght
    #
    #     def get_perimetr(self):
    #         return 2 * (self.__width + self.__lenght)
    #
    #     def get_diag(self):
    #         return math.sqrt(self.__width ** 2 + self.__lenght ** 2)
    #
    #     def get_draw(self):
    #         print(('*' * int(self.__width) + '\n') * int(self.__lenght))
    #
    #
    # a = Rectangle()
    # a.set_lenght(float(input()))
    # a.set_width(float(input()))
    # print("Длина прямоугольника:", a.get_lenght())
    # print("Ширина прямоугольника:", a.get_width())
    # print("Площадь прямоугольника:", a.get_area())
    # print("Периметр прямоугольника:", a.get_perimetr())
    # print("Диагональ прямоугольника:", a.get_diag())
    # a.get_draw()

    # class Point:
    #     __slots__ = ['__x', '__y', 'z']
    #
    #     def __init__(self, x, y):
    #         self.__x = x
    #         self.__y = y
    #
    #
    # p1 = Point(5, 10)
    # p1.z = 1
    # print(p1.z)
    # print(p1.__dict__)
    # class Point:
    #
    #     def __init__(self, x, y):
    #         self.__x = x
    #         self.__y = y
    #
    #     def __set_x(self, x):
    #         print('__set_x')
    #         self.__x = x
    #
    #     def __get_x(self):
    #         print('__get_x')
    #         return self.__x
    #
    #     def __del_x(self):
    #         print("Удаление свойства")
    #         del self.__x
    #
    #     x = property(__get_x, __set_x, __del_x)
    #
    #
    # p1 = Point(5, 10)
    # p1.x = 45
    # print(p1.__dict__)
    # del p1.x
    # print(p1.__dict__)

    # class Point:
    #
    #     def __init__(self, x, y):
    #         self.__x = x
    #         self.__y = y
    #
    #     @property
    #     def x(self):
    #         print('__get_x')
    #         return self.__x
    #
    #     @x.setter
    #     def x(self, x):
    #         print('__set_x')
    #         self.__x = x
    #
    #     @x.deleter
    #     def x(self):
    #         print("Удаление свойства")
    #         del self.__x
    #
    #     # x = property(__get_x, __set_x, __del_x)
    #
    #
    # p1 = Point(5, 10)
    # p1.x = 45
    # print(p1.__dict__)
    # del p1.x
    # print(p1.__dict__)

    # class KgToPounds:
    #     def __init__(self, kg):
    #         self.__kg = kg
    #
    #     @property
    #     def kg(self):
    #         return self.__kg
    #
    #     @kg.setter
    #     def kg(self, new_kg):
    #         if isinstance(new_kg, (int, float)):
    #             self.__kg = new_kg
    #         else:
    #             print('Килограммы задаются только числами')
    #
    #     def to_pounds(self):
    #         return self.__kg * 2.205
    #
    #
    # weight = KgToPounds(12)
    # print(weight.kg, 'кг =>', end=' ')
    # print(weight.to_pounds(), 'фунтов.')
    # weight.kg = float(input())
    # print(weight.kg, 'кг =>', end=' ')
    # print(weight.to_pounds(), 'фунтов.')

    # class Person:
    #     def __init__(self, name='Irina', old=26):
    #         self.__name = name
    #         self.__old = old
    #
    #     @property
    #     def name(self):
    #         return self.__name
    #
    #     @property
    #     def old(self):
    #         return self.__old
    #
    #     @name.setter
    #     def name(self, name):
    #         self.__name = name
    #
    #     @old.setter
    #     def old(self, old):
    #         self.__old = old
    #
    #     @name.deleter
    #     def name(self, name):
    #         del self.__name
    #
    #     @old.deleter
    #     def old(self, old):
    #         del self.__old
    #
    #     def print_person(self):
    #         print(f'{self.__name} - {self.__old} лет.')
    #
    #
    # p1 = Person('Alexei', 45)
    # p1.print_person()
    # p1.name = 'Nastya'
    # p1.old = 14
    # p1.print_person()

    # class Point:
    #     __count = 0
    #
    #     def __init__(self, x=0, y=0):
    #         self.__x = x
    #         self.__y = y
    #         Point.__count += 1
    #
    #     @staticmethod
    #     def get_count():
    #         return Point.__count

    # p1 = Point()
    # p2 = Point()
    # p3 = Point()
    # print(p1.get_count())

    # class Change:
    #     @staticmethod
    #     def inc(x):
    #         return x + 1
    #
    #     @staticmethod
    #     def dec(x):
    #         return x - 1
    #
    #
    # print(Change.inc(10), Change.dec(10))
    # import math
    #
    #
    # class Area:
    #     __count = 0
    #
    #     @staticmethod
    #     def triangle_area1(a, b, c):
    #         Area.__count += 1
    #         p = (a + b + c) / 2
    #         return math.sqrt(p * (p - a) * (p - b) * (p - c))
    #
    #     @staticmethod
    #     def triangle_area2(a, h):
    #         Area.__count += 1
    #         return .5 * a * h
    #
    #     @staticmethod
    #     def squre_area(a):
    #         Area.__count += 1
    #         return a ** 2
    #
    #     @staticmethod
    #     def rectangle_area(a, b):
    #         Area.__count += 1
    #         return a * b
    #
    #     @staticmethod
    #     def get_count():
    #         return Area.__count
    #
    #
    # print(f'Площадь треугольника по формуле Герона {Area.triangle_area1(3, 4, 5)}')
    # print(f'Площадь треугольника через основание и высоту {Area.triangle_area2(6, 7)}')
    # print(f'Площадь квадрата {Area.squre_area(float(input("a->")))}')
    # print(f'Площадь прямоугольника {Area.rectangle_area(2, 6)}')
    # print(Area.get_count())

    # class Date:
    #     def __init__(self, day, mounth, year):
    #         self.day = day
    #         self.mounth = mounth
    #         self.year = year
    #
    #     @classmethod
    #     def from_string(cls, string_date):
    #         day, mounth, year = map(int, string_date.split('.'))
    #         return cls(day, mounth, year)
    #
    #     @staticmethod
    #     def is_date_valid(string_date):
    #         if string_date.count('.') == 2:
    #             day, mounth, year = map(int, string_date.split('.'))
    #             return day <= 31 and mounth <= 12 and year <= 3999
    #
    #     def string_to_do(self):
    #         return f'{self.year}-{self.mounth}-{self.day}'
    #
    #     # string_date = '23.10.2022'
    #     # print(string_date.split('.'))
    #     # day, mounth, year = map(int, string_date.split('.'))
    #
    #
    # # date = Date.from_string('23.10.2022')
    # # print(date.string_to_do())
    # # date2 = Date.from_string('15.09.1988')
    # # print(date2.string_to_do())
    # dates = [
    #     '30.12.2020',
    #     '30-12-2020',
    #     '01.01.2021',
    #     '12.31.2020'

    # for string_date in dates:
    #     if Date.is_date_valid(string_date):
    #         date = Date.from_string(string_date)
    #         print(date.string_to_do())
    #
    #     else:
    #         print('Неправильная дата или формат строки с датой')

    # class Acount:
    #     rate_usd = 0.013
    #     rate_eur = 0.011
    #     suffix = 'RUB'
    #     suffix_usd = 'USD'
    #     suffix_eur = 'EUR'
    #
    #     def __init__(self, surname, num, percent, value=0):
    #         self.surname = surname
    #         self.num = num
    #         self.percent = percent
    #         self.value = value
    #         print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт.')
    #         print('*' * 50)
    #
    #     @classmethod
    #     def set_usd_rate(cls, rate):
    #         cls.rate_usd = rate
    #
    #     @classmethod
    #     def set_eur_rate(cls, rate):
    #         cls.rate_eur = rate
    #
    #     @staticmethod
    #     def convert(value, rate):
    #         return value * rate
    #
    #     def convert_to_usd(self):
    #         usd_val = Acount.convert(self.value, Acount.rate_usd)
    #         print(f'Состояние счёта: {usd_val} {Acount.suffix_usd}.')
    #
    #     def convert_to_eur(self):
    #         eur_val = Acount.convert(self.value, Acount.rate_eur)
    #         print(f'Состояние счёта: {eur_val} {Acount.suffix_eur}.')
    #
    #     def add_percents(self):
    #         print('Проценты начислены!')
    #         self.value = self.value + self.value * self.percent
    #         self.print_balance()
    #
    #     def with_draw_money(self, val):
    #         if val > self.value:
    #             print(f'К сожалению у вас нет {val} {Acount.suffix}.')
    #             self.print_balance()
    #         else:
    #             self.value -= val
    #             print(f'{val} {Acount.suffix} успешно сняты!')
    #             self.print_balance()
    #
    #     def add_money(self, val):
    #         print(f'{val} {Acount.suffix} успешно зачислены!')
    #         self.value += val
    #         self.print_balance()
    #
    #     def edit_owner(self, surname):
    #         self.surname = surname
    #
    #     def print_balance(self):
    #         print(f'Текущий баланс: {self.value} {Acount.suffix}')
    #
    #     def print_info(self):
    #         print('Информация о счёте:')
    #         print('-' * 20)
    #         print(f'#{self.num}')
    #         print(f'Владелец: {self.surname}')
    #         self.print_balance()
    #         print(f'Проценты: {self.percent:.0%}')
    #
    #         print('-' * 20)
    #
    #     def __del__(self):
    #         print('*' * 50)
    #         print(f'Счёт #{self.num} принадлежащий {self.surname} был закрыт.')
    #
    #
    # acc = Acount('Долгих', '12345', 0.03, 1000)
    # acc.print_info()
    # acc.convert_to_usd()
    # acc.convert_to_eur()
    # print()
    # acc.set_usd_rate(2)
    # acc.convert_to_usd()
    # acc.set_eur_rate(.5)
    # acc.convert_to_eur()
    # print()
    # acc.edit_owner('Дюма')
    # acc.print_info()
    # acc.add_percents()
    # print()
    # acc.with_draw_money(100)
    # print()
    # acc.add_money(5000)
    # print()

    # import re

    # class UserData:
    #     def __init__(self, fio, old, ps, weight):
    #         self.verify_fio(fio)
    #         self.verify_old(old)
    #         self.verify_weight(weight)
    #         self.verify_ps(ps)
    #         self.__fio = fio
    #         self.__old = old
    #         self.__password = ps
    #         self.__weight = weight
    #
    #     @staticmethod
    #     def verify_fio(fio):
    #         if not isinstance(fio, str):
    #             raise TypeError('ФИО должно быть строкой.')
    #         f = fio.split()
    #         if len(f) != 3:
    #             raise TypeError('Неверный формат ФИО')
    #         letters = ''.join(re.findall(r'[a-zа-яё-]', fio, re.IGNORECASE))
    #
    #         for s in f:
    #
    #             if len(s.strip(letters)) != 0:
    #                 raise TypeError('В ФИО модно использовать только буквы и дефис')
    #
    #     @staticmethod
    #     def verify_old(old):
    #         if not isinstance(old, int) or old < 14 or old > 120:
    #             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет ')
    #
    #     @staticmethod
    #     def verify_weight(w):
    #         if not isinstance(w, float) or w < 20:
    #             raise TypeError('Вес должен быть вещественным числом больше 20кг')
    #
    #     @staticmethod
    #     def verify_ps(ps):
    #         if not isinstance(ps, str):
    #             raise TypeError('Паспорт должен быть строкой')
    #         s = ps.split()
    #         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
    #             raise TypeError('Неверный формат паспорта')
    #         for p in s:
    #             if not p.isdigit():
    #                 raise TypeError('Серия и номер паспорта должны быть числами')
    #
    #     @property
    #     def fio(self):
    #         return self.__fio
    #
    #     @fio.setter
    #     def fio(self, fio):
    #         self.verify_fio(fio)
    #         self.__fio = fio
    #
    #     @property
    #     def old(self, old):
    #         return self.__old
    #
    #     @old.setter
    #     def old(self, old):
    #         self.verify_old(old)
    #         self.__old = old
    #
    #     @property
    #     def ps(self):
    #         return self.__password
    #
    #     @ps.setter
    #     def ps(self, ps):
    #         self.verify_ps(ps)
    #         self.__password = ps
    #
    #     @property
    #     def weight(self):
    #         return self.__weight
    #
    #     @weight.setter
    #     def weight(self, w):
    #         self.verify_weight(w)
    #         self.__weight = w
    #
    #
    # p1 = UserData('Волков Виктор Николаевич', 26, '1234 567890', 80.5)
    # p1.fio = 'Соболев Игорь Николаевич'
    # p1.old = 54
    # p1.weight = 73.5
    # print(p1.__dict__)
    # print(issubclass(Point, object))
    # class Point:
    #     def __init__(self, x=0, y=0):
    #         self.x = x
    #         self.y = y
    #
    #     def __str__(self):
    #         return f'({self.x},{self.y})'
    #
    #
    # class Prop:
    #     def __init__(self, sp, ep, color='red', width=1):
    #         self._sp = sp
    #         self._ep = ep
    #         self._color = color
    #         self._width = width
    #
    #
    # class Line(Prop):
    #
    #     def draw_line(self):
    #         print(f'Рисование линии: {self._sp},{self._ep},{self._color},{self._width}')
    #
    #
    # class Rect(Prop):
    #
    #     def draw_rect(self):
    #         print(f'Рисование прямоугольника: {self._sp},{self._ep},{self._color},{self._width}')
    #
    #
    # line = Line(Point(1, 2), Point(10, 20))
    # line.draw_line()
    # rect = Rect(Point(30, 40), Point(70, 80))
    # rect.draw_rect()
    # Принцип DRY -не повторяться

    # class Figure:
    #     def __init__(self, color):
    #         self.__color = color
    #
    #     @property
    #     def color(self):
    #         return self.__color
    #
    #     @color.setter
    #     def color(self, c):
    #         self.__color = c
    #
    #
    # class Rectangle(Figure):
    #     def __init__(self, width, height, color):
    #         self.__width = width
    #         self.__height = height
    #         super().__init__(color)
    #
    #     @property
    #     def width(self):
    #         return self.__width
    #
    #     width.setter
    #
    #     def width(self, w):
    #         if w > 0:
    #             self.__width = w
    #         else:
    #             raise ValueError('no')
    #
    #     @property
    #     def height(self):
    #         return self.__height
    #
    #     height.setter
    #
    #     def height(self, h):
    #         if h > 0:
    #             self.__height = h
    #         else:
    #             raise ValueError('no')
    #
    #     def area(self):
    #         print(f'Площадь {self.color} прямоугольника {self.__width}x{self.__height}:', end=' ')
    #         return self.__width * self.__height
    #
    #
    # rect = Rectangle(10, 20, 'green')
    # print(rect.__dict__)
    # print(rect.area())

    # class Point:
    #     def __init__(self, x=0, y=0):
    #         self.x = x
    #         self.y = y
    #
    #     def __str__(self):
    #         return f'({self.x},{self.y})'
    #
    #     def is_digit(self):
    #         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
    #             return True
    #         else:
    #             return False
    #
    #     def is_int(self):
    #         if isinstance(self.x, int) and isinstance(self.y, int):
    #             return True
    #         else:
    #             return False
    #
    #
    # class Prop:
    #
    #     def __init__(self, sp, ep, color='red', width=1):
    #         print('Инициализатор базового класса Prop')
    #         self._sp = sp
    #         self._ep = ep
    #         self._color = color
    #         self._width = width
    #
    #     def set_coord(self, sp, ep):
    #         if sp.is_digit() and ep.is_digit():
    #             self._sp = sp
    #             self._ep = ep
    #         else:
    #             print('Координаты должны быть числами')
    #
    #
    # class Line(Prop):
    #
    #     def draw_line(self):
    #         print(f'Рисование линии: {self._sp},{self._ep},{self._color},{self._width}')
    #
    #
    # class Rect(Prop):
    #
    #     def draw_rect(self):
    #         print(f'Рисование прямоугольника: {self._sp},{self._ep},{self._color},{self._width}')
    #
    #     def set_coord(self, sp, ep):
    #         if sp.is_int() and ep.is_int():
    #             self._sp = sp
    #             self._ep = ep
    #
    #
    # line = Line(Point(1, 2), Point(100, 200))
    # line.draw_line()
    # rect = Rect(Point(10.1, 20), Point(200, 300))
    # rect.draw_rect()

    # class Rect:
    #     def __init__(self, width, height):
    #         self.width = width
    #         self.height = height
    #
    #     def show_rect(self):
    #         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
    #
    #
    # class RectFon(Rect):
    #     def __init__(self, width, height, background):
    #         self.fon = background
    #         super().__init__(width, height)
    #
    #     def show_rect(self):
    #         super().show_rect()
    #         print(f'Фон: {self.fon}')
    #
    #
    # class RectBorder(Rect):
    #
    #     def __init__(self, width, height, border):
    #         self.border = border
    #         super().__init__(width, height)
    #
    #     def show_rect(self):
    #         super().show_rect()
    #         print(f'Рамка: {self.border}')
    #
    #
    # shape1 = RectFon(400, 200, 'blue')
    #
    # shape1.show_rect()
    # shape2 = RectBorder(600, 300, '1px solid red')
    # shape2.show_rect()

    # class Vector(list):
    #     def __str__(self):
    #         return ' '.join(map(str, self))
    #
    #
    # v = Vector([1, 2, 3])
    # print(v)
    # print(type(v))
    #  Перегрузка методов

    # class Point:
    #     def __init__(self, x=0, y=0):
    #         self.x = x
    #         self.y = y
    #
    #     def __str__(self):
    #         return f'({self.x},{self.y})'
    #
    #     def is_digit(self):
    #         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
    #             return True
    #         else:
    #             return False
    #
    #     def is_int(self):
    #         if isinstance(self.x, int) and isinstance(self.y, int):
    #             return True
    #         else:
    #             return False
    #
    #
    # class Prop:
    #
    #     def __init__(self, sp, ep, color='red', width=1):
    #         print('Инициализатор базового класса Prop')
    #         self._sp = sp
    #         self._ep = ep
    #         self._color = color
    #         self._width = width
    #
    #     def set_coord(self, sp, ep):
    #         if sp.is_digit() and ep.is_digit():
    #             self._sp = sp
    #             self._ep = ep
    #         else:
    #             print('Координаты должны быть числами')
    #
    #
    # class Rect(Prop):
    #
    #     def draw_rect(self):
    #         print(f'Рисование прямоугольника: {self._sp},{self._ep},{self._color},{self._width}')
    #
    #     def set_coord(self, sp, ep=None):
    #         if ep is None:
    #             if sp.is_int():
    #                 self._sp = sp
    #             else:
    #                 print('Первая координата должна быть числом.')
    #         else:
    #             if sp.is_int() and ep.is_int():
    #                 self._sp = sp
    #                 self._ep = ep
    #
    #
    # rect = Rect(Point(1, 2), Point(10, 20))
    # rect.draw_rect()
    # rect.set_coord(Point(10, 30), Point(40, 70))
    # rect.draw_rect()
    # rect.set_coord((Point(-10, -20)))
    # rect.draw_rect()

    # Абстрактные методы

    # class Point:
    #     def __init__(self, x=0, y=0):
    #         self.x = x
    #         self.y = y
    #
    #     def __str__(self):
    #         return f'({self.x},{self.y})'
    #
    #     def is_digit(self):
    #         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
    #             return True
    #         else:
    #             return False
    #
    #     def is_int(self):
    #         if isinstance(self.x, int) and isinstance(self.y, int):
    #             return True
    #         else:
    #             return False
    #
    #
    # class Prop:
    #
    #     def __init__(self, sp, ep, color='red', width=1):
    #         # print('Инициализатор базового класса Prop')
    #         self._sp = sp
    #         self._ep = ep
    #         self._color = color
    #         self._width = width
    #
    #     def set_coord(self, sp, ep):
    #         if sp.is_digit() and ep.is_digit():
    #             self._sp = sp
    #             self._ep = ep
    #         else:
    #             print('Координаты должны быть числами')
    #
    #     def draw(self):
    #         raise NotImplementedError('В дочерном классе ')
    #
    # class Line(Prop):
    #     def draw(self):
    #         print(f'Рисование линии:{self._sp}, {self._ep}, {self._color}, {self._width}')
    #
    #
    # class Rect(Prop):
    #     def draw(self):
    #         print(f'Рисование прямоугольника:{self._sp}, {self._ep}, {self._color}, {self._width}')
    #
    #
    # class Ellipse(Prop):
    #     def draw(self):
    #         print(f'Рисование эллипса:{self._sp}, {self._ep}, {self._color}, {self._width}')
    #
    #
    # figs = list()
    # figs.append(Line(Point(0, 0), Point(10, 20)))
    # figs.append(Line(Point(15, 25), Point(33, 44)))
    # figs.append(Rect(Point(4, 24), Point(34, 44)))
    # figs.append(Ellipse(Point(100, 200), Point(304, 404)))
    # for f in figs:
    #     f.draw()

    # from abc import ABC, abstractmethod
    #
    #
    # class Chess(ABC):  # абстрактный класс
    #     def draw(self):
    #         print('Нарисовал шахматную фигуру')
    #
    #     @abstractmethod
    #     def move(self):  # абстрактный метод
    #         print('move()')
    #
    #
    # class Queen(Chess):
    #     def move(self):
    #         super().move()
    #         print("Ферзь премещёна е2 е4")

    # q = Queen()
    # q.move()
    # q.draw()

    # from math import pi
    #
    #
    # class Table:
    #     def __init__(self, width=None, lenght=None, radius=None):
    #         if radius is None:
    #             self._width = width
    #             self._lenght = lenght
    #         else:
    #             self._radius = radius
    #
    #     def calc_area(self):
    #         raise NotImplementedError('В дочернем классе должен быть метод calc_area()')
    #
    #
    # class SqTable(Table):
    #     def calc_area(self):
    #         return self._width * self._lenght
    #
    #
    # class RoundTable(Table):
    #     def calc_area(self):
    #         return round(self._radius ** 2 * pi, 2)
    #
    #
    # t = SqTable(20, 10)
    # print(t.__dict__)
    # print(t.calc_area())
    # t1 = RoundTable(radius=20)
    # print(t1.__dict__)
    # print(t1.calc_area())

    # from abc import ABC, abstractmethod
    #
    #
    # class Currency(ABC):
    #     def __init__(self, value):
    #         self.value = value
    #
    #     @abstractmethod
    #     def convert_to_rub(self):
    #         pass
    #
    #     @abstractmethod
    #     def print_value(self):
    #         print(self.value, end=' ')
    #
    #
    # class Dollar(Currency):
    #     rate_to_rub = 74.16
    #     suffix = 'USD'
    #
    #     def print_value(self):
    #         super().print_value()
    #         print(Dollar.suffix, end=' ')
    #
    #     def convert_to_rub(self):
    #         return self.value * Dollar.rate_to_rub
    #
    #
    # class Euro(Currency):
    #     rate_to_rub2 = 90.14
    #     suffixe = 'EUR'
    #
    #     def print_value(self):
    #         super().print_value()
    #         print(Euro.suffixe, end=' ')
    #
    #     def convert_to_rub(self):
    #         return self.value * Euro.rate_to_rub2
    #
    #
    # print('*' * 50)
    # d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
    # for i in d:
    #     i.print_value()
    #     print(f'= {i.convert_to_rub():.2f} RUB')
    # print('*' * 50)
    # e = [Euro(5), Euro(10), Euro(50), Euro(100)]
    # for i in e:
    #     i.print_value()
    #     print(f'= {i.convert_to_rub():.2f} RUB')
    # print('*' * 50)

    # Интерфейсы

    # from abc import ABC, abstractmethod
    #
    #
    # class Father(ABC):
    #     @abstractmethod
    #     def display1(self):
    #         pass
    #
    #     def display2(self):
    #         pass
    #
    #
    # class Child(Father):
    #     def display1(self):
    #         print('Child')
    #
    #
    # class GrandChild(Child):
    #     def display2(self):
    #         print('GrandChild')
    #
    #
    # go = Child()
    # go.display1()
    # go.display2()

    # def func():
    #     x = 2
    #
    #     def inner():
    #         n = 4
    #         return n + x
    #     return inner()
    #
    #
    # print(func())

    # class MyOuter:
    #     age = 18
    #
    #     def __init__(self, name):
    #         self.name = name
    #
    #     @classmethod
    #     def outer_class_method(cls):
    #         print('outer_class_method')
    #
    #     def outer_obj_method(self):
    #         print('outer_obj_method')
    #
    #     class MyInner:
    #         def __init__(self, innername, obj):
    #             self.innername = innername
    #             self.obj = obj
    #
    #         def inner_method(self):
    #             print('inner_method', MyOuter.age, self.obj.name)
    #             MyOuter.outer_class_method()
    #             self.obj.outer_obj_method()
    #
    #
    # out = MyOuter('внешний')
    # print(out.name)
    # inner = out.MyInner('внутренний', out)
    # print(inner.innername)
    # (inner.inner_method())

    # class Color:
    #     def __init__(self):
    #         self.name = 'Green'
    #         self.lg = self.Lightgreen()
    #
    #     def show(self):
    #         print("name", self.name)
    #
    #     class Lightgreen:
    #         def __init__(self):
    #             self.name = 'Light Green'
    #
    #         def display(self):
    #             print('name', self.name)
    #
    #
    # outer = Color()
    # outer.show()
    # g = outer.lg
    # g.display()

    # class Intern:
    #     def __init__(self):
    #         self.name = input('name')
    #
    #     def display(self):
    #         print('name', self.name)
    #
    #
    # class Employee:
    #     def __init__(self):
    #         self.name = "Employee"
    #         self.head = self.Head()
    #         self.intern = Intern()
    #
    #     def show(self):
    #         print('name', self.name)
    #
    #     class Head:
    #         def __init__(self):
    #             self.name = "Alba"
    #
    #         def display2(self):
    #             print('name', self.name)
    #
    #
    # outer = Employee()
    # outer.show()
    # d1 = outer.intern
    # d2 = outer.head
    # d1.display()
    # d2.display2()
    # class Outer:
    #     def __init__(self):
    #         self.inner = self.Inner()
    #
    #     def show(self):
    #         print('Внешний класс')
    #
    #     class Inner:
    #         def __init__(self):
    #             self.inner_inner = self.InnerClass()
    #
    #         def show(self):
    #             print('Вложенный класс')
    #
    #         class InnerClass:
    #             def show(self):
    #                 print('Класс внутри вложенного класса')
    #
    #
    # outer = Outer()
    # outer.show()
    # inner1 = outer.inner
    # inner1.show()
    # inner2 = inner1.inner_inner
    # inner2.show()
    # class Computer:
    #     def __init__(self):
    #         self.name = 'PC001'
    #         self.os = self.OS()
    #         self.cpu = self.CPU()
    #
    #     class OS:
    #
    #         def system(self):
    #             return 'Windows 10'
    #
    #     class CPU:
    #         def make(self):
    #             return 'Intel'
    #
    #         def model(self):
    #             return 'Core-i7'
    #
    #
    # comp = Computer()
    # my_os = Computer.OS()
    # my_cpu = comp.cpu
    # print(comp.name)
    # print(my_os.system())
    # print(my_cpu.make())
    # print(my_cpu.model())
    # class Base:
    #     def __init__(self):
    #         self.db = self.Inner()
    #
    #     def display(self):
    #         print('Базовый класс')
    #
    #     class Inner:
    #         def display2(self):
    #             print('Вложенный класс внутри базового')
    #
    #
    # class SubClass(Base):
    #     def __init__(self):
    #         print('Дочерний класс')
    #         super().__init__()
    #
    #     class Inner(Base.Inner):
    #         def display3(self):
    #             print('Вложенный класс внутри дочернего')

    #
    # a = SubClass()
    # a.display()
    # # b = a.db
    # b = SubClass.Inner()
    # b.display2()
    # b.display3()

    # class Cat:
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def __repr__(self):
    #         return f'{self.__class__}: {self.name}'
    #
    #     def __str__(self):
    #         return f'{self.name}'
    #
    #
    # cat = [Cat('Пушок'), Cat('Мурзик')]
    # print(cat)
    # class Point:
    #     def __init__(self, *args):
    #         self.__coord = args
    #         print(self.__coord)
    #
    #     def __len__(self):
    #         return len(self.__coord)
    #
    #
    # p = Point(5, 9, 6)
    # print(len(p))
    # import math
    #
    #
    # class Point:
    #     __slots__ = ('x', 'y', '__lenght')
    #
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #         self.lenght = math.sqrt(x * x + y * y)
    #
    #     @property
    #     def lenght(self):
    #         return self.__lenght
    #
    #     @lenght.setter
    #     def lenght(self, value):
    #         self.__lenght = value
    #
    #
    # p1 = Point(3, 4)
    # print(p1.lenght)
    # # print(p1.__dict__)

    # class Point2D:
    #
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #
    #
    # p1 = Point(5, 10)
    # p2 = Point2D(5, 10)
    # print('p1 =', p1.__sizeof__())
    # print('p2 =', p2.__sizeof__()+p2.__dict__.__sizeof__())
    # class Point:
    #     __slots__ = ('x', 'y')
    #
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #
    #
    # class Point3D(Point):
    #     __slots__ = 'z'
    #
    #     def __init__(self, x, y, z):
    #         self.z = z
    #         super().__init__(x, y)
    #
    #
    # p1 = Point(5, 10)
    # p3 = Point3D(5, 10, 20)
    #
    # print(p3.x, p3.y, p3.z)

    # Множественное наследование
    # class Creature:
    #     def __init__(self, name):
    #         self.name = name
    #
    #
    # class Animal(Creature):
    #     def sleep(self):
    #         print(self.name, 'is sleeping.')
    #
    #
    # class Pet(Creature):
    #     def play(self):
    #         print(self.name, 'is playing.')
    #
    #
    # class Dog(Animal, Pet):
    #     def bark(self):
    #         print(self.name, 'is barking.')
    #
    #
    # b = Dog('Buddy')
    # b.bark()
    # b.play()
    # b.sleep()
    # class A:
    #     def __init__(self):
    #         print('Class A')
    #
    #
    # class B(A):
    #     def __init__(self):
    #         print('Class B')
    #
    #
    # class C(A):
    #     def __init__(self):
    #         print('Class C')
    #
    #
    # class D(B, C):
    #     # def __init__(self):
    #     #     print('Class D')
    #     ...
    #
    # d = D()
    # print(D.mro())

    # 24*60*60=86400(число секунд в одном дне)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError('секунды должны быть целым числом')
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return print(f'{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}')
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#
# cl = Clock(600)
# cl2 = Clock(600)
# if cl == cl2:
#     print('Время равно')
# else:
#     print('Время не равно')
# cl.get_format_time()
#
# cl2.get_format_time()
# cl2 += cl
# cl.get_format_time()
# cl2.get_format_time()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise IndexError('Индекс должен быть целым положительным числом')
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#             self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         del self.marks[key]
#
#
# s1 = Student('Виктор', [5, 5, 3, 4, 5])
# print(s1[2])
# s1[5] = 4
# del s1[2]
# print(s1.marks)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError('секунды должны быть целым числом')
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return print(f'{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}')
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         if item == 'min':
#             return (self.sec // 60) % 60
#         if item == 'sec':
#             return self.sec % 60
#         return 'Неверный ключ'
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError('Ключ должен быть строковым значением')
#         if not isinstance(value, int):
#             raise ValueError('Значение должно быть целым числом')
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.sec = value + 60 * m + 3600 * h
#
#
# cl = Clock(80000)
# cl.get_format_time()
# print(cl['hour'])
# print(cl['min'])
# print(cl['sec'])
# cl['hour'] = 9
# cl['min'] = 3
# cl['sec'] = 13
# cl.get_format_time()
# print(cl['hour'])
# print(cl['min'])
# print(cl['sec'])

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f'{self.name} is good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is good girl!!!'
#         else:
#             return f'{self.name} is good Kitty!!!'
#
#     def __repr__(self):
#         return f'Cat(name="{self.name}", age={self.age}, pol="{self.pol}"'
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat('No name', 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError('Типы не совместимы')
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Else', 5, 'F')
# cat3 = Cat('Murzik', 5, 'M')
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per_fig(self):
#         return 2 * (self.w + self.h)
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_per_fig(self):
#         return 2 * (self.a + self.b + self.c)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per_fig(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1, 4, 7)
# t2 = Triangle(5, 10, 15)
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_per_fig())

# class Number:
#     def __init__(self, value):
#         self.value = value
#

#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('10')
# print(t1.total(35))
# print(t2.total(35))
# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'{self.surname} {self.name} {self.age}', end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.group} {self.rating}')
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, cabinet):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.cabinet = cabinet
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.cabinet}')
#
#
# class Graduate(Human):
#     def __init__(self, surname, name, age, speciality, group, rating, dip):
#         super().__init__(surname, name, age)
#         self.spec = speciality
#         self.group = group
#         self.rating = rating
#         self.dip = dip
#
#     def info(self):
#         super().info()
#         print(f'{self.spec} {self.group} {self.rating} {self.dip}')
#
#
# group = [
#     Student('Батодалаев', 'Даши', 16, 'ГК', 'Web_011', 5),
#     Student('Загидуллин', 'Линар', 32, 'РПО', 'PD_011', 5),
#     Graduate('Шугани', 'Сергей', 15, 'РПО', 'PD_011', 5, 'Защита персональных данных'),
#     Teacher('Башкиров', 'Алексей', 45, 'Разработка приложений', 20),
#     Student('Маркин', 'Даниил', 17, 'ГК', 'Python_011', 5),
#     Teacher('Даньшин', 'Андрей', 38, 'Астрофизика', 110)
# ]
# for i in group:
#     i.info()


# Функторы

# def func():
#     def wrap():
#         return 'Hello'
#
#     return wrap
#
#
# a = func()
# print(a())

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#
#         self.count += 1
#         print(self.count)
#
#
# c1 = Counter()
# c1(5)
# c1(5)
# c1(5)
# c1(5)
# c1(5)
# class StripChars:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#         return args[0].strip(self.chars)
#
#
# s1 = StripChars('*?;!,:. ')
# print(s1('! ?Hello World; . :'))
#
#
# def strip_char(chars):
#     def call(string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой')
#         return string.strip(chars)
#
#     return call
#
#
# s2 = strip_char('*?;!,:. ')
# print(s2('! ?Hello World; . :'))

# Декораторы
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(a, b))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def result(a, b):
#     return a * b
#
#
# print(result(2, 3))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **b):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(*args, **b))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# @MyDecorator
# def hello1(a, b, c):
#     return a * b * c
#
#
# print(hello(2, 5))
# print(hello1(2, 5, 2))

# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **b):
#             res = 'перед вызовом функции\n'
#             res += self.arg + str(func(*args, **b))
#             res += '\nпосле вызова функции'
#             return res
#
#         return wrap
#
#
# @MyDecorator('Результата умножения: ')
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **b):
#             res2 = (func(*args, **b)) ** self.arg
#             res = 'перед вызовом функции\n'
#             res += str(res2)
#             res += '\nпосле вызова функции'
#             return res
#
#         return wrap
#
#
# @Power(6)
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 2))
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
#
# p1 = Person('Виталий', 'Карасёв')
# p1.info()
# def decorator(cls):
#     class Wrapper(cls):
#         def method2(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Инициализатор ActualClass')
#
#     def method1(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method1(4))
# print(obj.method2(6))


# Дескритторы
# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self,value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person('Иван', 'Петров')
# p.name = 'Алексей'
# print(p.name)
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Иван', 'Петров')
# print(p.name)
# print(p.surname)
# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('значение должно быть больше нуля')
#
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quality = NonNegative()
#
#     def __init__(self, name, price, quality):
#         self.name = name
#         self.price = price
#         self.quality = quality
#
#     def total(self):
#         return self.price * self.quality
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())
# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise ValueError('должна быть целым числом')
#
#
# def __set_name__(self, owner, name):
#     self.name = '_' + name
#
#
# def __get__(self, instance, owner):
#     return instance.__dict__[self.name]
#
#
# def __set__(self, instance, value):
#     self.verify_coord(value)
#
#     instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p = Point3D(1, 2.2, 3)
# print(p.__dict__)

# Создание модулей


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per_fig(self):
#         return 2 * (self.w + self.h)
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_per_fig(self):
#         return 2 * (self.a + self.b + self.c)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per_fig(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1, 4, 7)
# t2 = Triangle(5, 10, 15)
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_per_fig())

# from car.electrocar import ElectroCar
#
#
# def main():
#     car = ElectroCar('Tesla', 'T', 2018, 99000)
#     car.show_car()
#     car.description_battery()
#
#
# if __name__ == '__main__':
#     main()

# Упаковка данных (сериализация)
# Распаковка данных(десериализация)
# marshal(*.pyc)
# pickle
# json
# dump() - сохраняет данные в открытый файл.
# dumps() - сохраняет(серилизует) данные в строку.

# load() - считывает данные из открытого файла.
# loads() - считывает данные из строки.


# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': 'морковь',
#     'бюджет': 1000
# }
# with open(file_name, 'wb') as f:
#     pickle.dump(shop_list, f)
# with open(file_name, 'rb') as f:
#     shop2 = pickle.load(f)
# print(shop2)

# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#     d = {'first': 'б', 'second': 2}
#
#     def __str__(self):
#         return f'Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}\nСловарь: {Test.d}.'
#
#
#
# obj = Test()
# # print(obj)
# my_obj = pickle.dumps(obj)
# print(my_obj)
# ob = pickle.loads(my_obj)
# print(ob)
# print(ob.d)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(6)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstname': 'Alice',
#             'age': 6
#         }
#
#     ]
#
# }
# # with open('data_file.json', 'w') as f:
# #     json.dump(data, f, indent=4)
# # with open('data_file.json', 'r') as f:
# #     data1 = json.load(f)
# # print(data1)
# json_string = json.dumps(data,sort_keys=False)
# # print(json_string)
# # print(type(json_string))
# # print(json_string[0])
#
# data1 = json.loads(json_string)
# # print(type(data1))
# # print(data1['name'])
#
# print(data1)
#
# x = {
#     'name':'Виктор'
# }
#
# print(json.dumps(x))
# print(json.dumps(x,ensure_ascii=False))

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#     letters = ['a', 'b', 'c', 'd', 'e', 'g', 'm', 'n', 'k']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data =[]
#     data.append(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))
#         # for i in self.marks:
#         #     a += str(i) + ', '
#
#         return f'Студент: {self.name} - {a}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': self.name, 'marks': self.marks})
#         with open(file_name, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.group = group
#         self.students = students
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f'Группа {self.group}.\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_goup(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#     @staticmethod
#     def upload_journal(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(1, 5)
# # print(st1)
# # print(st1.average_mark())
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# # print(my_group)
# # print()
# my_group.add_student(st3)
# # print(my_group)
# # print()
# my_group.remove_student(1)
# # print(my_group)
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# # print()
# # print(my_group2)
# Group.change_goup(my_group, my_group2, 0)
# # print()
# # print(my_group)
# # print()
# # print(my_group2)
# # file1 = 'Student_list.json'
# # st1.dump_to_json(file1)
# # st1.load_from_file(file1)
# # st2.dump_to_json(file1)
# # st2.load_from_file(file1)
# # st3.dump_to_json(file1)
# # st3.load_from_file(file1)
# file2 = 'Group_list.json'
# my_group.dump_group(file2)
# my_group2.dump_group(file2)
# my_group.upload_journal(file2)


# pip install reqests
# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# # print(response)
# # print(response.text)
# todos = json.loads(response.text)
# # print(todos)
#
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# top2 = sorted(todos_by_user.values(), reverse=True)
# print(top_users)
# print(top2)
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_user = ' and '.join(users)
# print(max_user)
# n = 's' if len(users) > 1 else ''
# print(f'User{n} {max_user} completed {max_complete} todos.')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)

# CSV (Commo Separated Values - переменные разделённые запятыми)

# import csv
#
# print('Лёша')
# with open('data.csv') as f:
#     file_reader = csv.reader(f)
#     print(file_reader)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {",".join(row)}')
#         else:
#             print(f'\t\t{row[0]} - {row[1]}. Родился в {row[2]} году.')
#         count += 1
# print(f'Всего в файле {count} строки.')

# import csv
#
# with open('data2.csv') as f:
#     file = csv.reader(f,delimiter=';')
#     for r in file:
#         print(r)

# import csv
#
# with open('data.csv', encoding='UTF-8') as f:
#     fields = ['Name', 'Profesion', 'birthday']
#     file_reader = csv.DictReader(f, fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         print(f'\t\t{row["Name"]} - {row["Profesion"]}. Родился в {row["birthday"]} году.')
#         count += 1
# import csv

# with open('students.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])

# data = [
#     ['hostname', 'vendor', 'location'],
#     ['sw1', 'Cisco', '3750', 'London, Best str'],
#     ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#     ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#     ['sw4', 'Cisco', '3650', 'London, Best str']
# ]
# with open('data_new2.cvs', 'w') as f:
#     writer = csv.writer(f, lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
# with open('students2.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     writer = csv.DictWriter(f, fieldnames=names, lineterminator='\r')
#     writer.writeheader()
#     writer.writerow({'Имя': 'Женя', "Возраст": '15'})
#     writer.writerow({'Имя': 'Саша', 'Возраст': '12'})
#     writer.writerow({'Имя': 'Маша', 'Возраст': '18'})
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
#
#     }, {'hostname': 'sw3',
#         'location': 'Liverpool',
#         'model': '3650',
#         'vendor': 'Cisco'
#
#         }, {'hostname': 'sw4',
#             'location': 'London',
#             'model': '3650',
#             'vendor': 'Cisco'
#
#             }
#
# ]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), lineterminator='\r')
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# with open('todos.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(todos[0].keys()), lineterminator='\r')
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)
# pip install beautifulsoup4 или bs4
# from bs4 import BeautifulSoup

# f = open('homework3.html', encoding='UTF-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find('li')
# # print(row)
# # row = soup.find('li', string="Основы")
# # print(row)
# # row = soup.find('li', string='Основы').parent
# # print(row)
# # row = soup.find('li', string='Основы').find_parent('li')
# # print(row)
# # row = soup.find('li', string='Основы').find_next_sibling()
# # print(row)
# row = soup.find('li', string='Основы').find_previous_sibling()
# print(row)
# def get_copywriter(tag):
#     fg = tag.find('ul', class_='fg')
#     print(fg)
#     if '<li>' in fg:
#         return tag
#     return None
#
#
# f = open('homework3.html', encoding='UTF-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('ul', class_='fg')
# print(row)
# copywr = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywr.append(cw)
#
# print(copywr)
# import re
#
#
# def get_num(s):
#     pat = r'\d+'
#     res = re.findall(pat, s)
#     # res = re.search(pat,s)
#     print(res)
#
#
# f = open('homework3.html', encoding='UTF-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('ul', class_='fg')
# print(row)
# for i in row:
#     get_num(i.text)

# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get('https://ru.wordpress.org/')
# res.encoding = 'UTF-8'
# # print(res.status_code)
# # print(res.headers['content-type'])
# print(res.text)
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#
#     return res.text
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     get_data(get_html(url))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title')
#     p2 = p1.text
#     print(p2)
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
#
# import csv
#
#
# def write_csv(data):
#     with open('plug.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_html(url):
#     res = requests.get(url)
#     res.encoding = 'UTF-8'
#
#     return res.text
#
#
# def refind(s):
#     return re.sub(r'\D+', '', s)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[3]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3')
#         print(name.text)
#         url = plugin.find('h3').find('a').get('href')  # ['href']
#         print(url)
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refind(rating)
#         print(r)
#         data = {'name': name, 'url': url, 'rating': r}
#         print(data)
#         write_csv(data)
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#
#     return res.text
#
#
# def main():
#     for i in range(2, 5):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}'
#         get_data(get_html(url))


# def write_csv(data):
#     with open('plug2.csv', 'a') as f:
#         wr = csv.writer(f, lineterminator='\r')
#         wr.writerow((data['name'], data['url'], data['snipet'], data['active'], data['cy']))
#
#
# def refine(s):
#     return s.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('article', class_='plugin-card')
#     for el in p1:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#         # print(name)
#         try:
#             url = el.find('h3').find('a')['href']
#         except ValueError:
#             url = ''
#         # print(url)
#         try:
#             snippet = el.find('div', class_='entry-excerpt').find('p').text
#         except ValueError:
#             snippet = ''
#         # print(snippet)
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#
#         except ValueError:
#             active = ''
#         # print(active)
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine(c)
#
#         except ValueError:
#             cy = ''
#         # print(cy)
#         data = {'name': name, 'url': url, 'snipet': snippet,
#                 'active': active, 'cy': cy}
#
#         write_csv(data)
#
#
# if __name__ == '__main__':
#     main()
# from parsers import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# import socket
# from view import index,blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return "HTTP/1.1 404 Page Not Found\n\n", 404
#     return 'HTTP 1.1 200!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found</h3>'
#     elif code == 405:
#         return '<h1>405</h1.<h3>Page Not Allowed</h3>'
#
#     else:
#         return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f'Клиент: {addr} => \n{request}\n')
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()


# con = sqlite3.connect('profile.db')
# cur = con.cursor()
# cur.execute('''
# ''')
# con.close()

# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date TEXT
#     )
#     ''')


# cur.execute('''CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT "+79090000000",
# age INTEGER CHECK(age>0 AND age<100),
# email TEXT UNIQUE
# )
# ''')
# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table
# """)
# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address
# """)
# cur.execute("""
# ALTER TABLE person_table
# DROP COLUMN home_address
# """)
# cur.execute("""
# DROP TABLE person_table
#
#
# """)

# import sqlite3
#
# with sqlite3.connect('db_4.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2,5
#     """)
#     # res = cur.fetchall()
#     # print(res)
#     # for res in cur:
#     #     print(res)
#     res = cur.fetchone()
#     print(res)
#     res2=cur.fetchone()
#     print(res2)
#     res3=cur.fetchmany(2)
#     print(res3)
#     for res in cur:
#         print(res)


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 100000})

# cur.executemany("INSERT INTO cars VALUES(NULL,?,?)", cars)

# for car in cars:
#       cur.execute("INSERT INTO cars VALUES(NULL,?,?)",car)
# cur.execute("INSERT INTO cars VALUES(1,'Renault',22000)")
# cur.execute("INSERT INTO cars VALUES(2,'Volvo',29000)")
# cur.execute("INSERT INTO cars VALUES(3,'Mercedes',57000)")
# cur.execute("INSERT INTO cars VALUES(4,'Bentley',35000)")
# cur.execute("INSERT INTO cars VALUES(5,'Audy',52000)")

# con.commit()
# con.close()
# con = None
# try:
#     con = sqlite3.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL,'Renault',22000);
#     UPDATE cars SET price = price + 100
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print('Ошибка выполнения запроса' + str(e))
# finally:
#     if con:
#         con.close()

# import sqlite3


# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,tr_in INTEGER,buy INTEGER
#     );
#
#     """)
#     cur.execute("INSERT INTO cars VALUES(NULL,'Запорожец',1000)")
#     last_row_id = cur.lastrowid
#
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья',?,?)", (last_row_id, buy_car_id))


# with sqlite3.connect('cars.db') as con:
#     con.row_factory=sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,tr_in INTEGER,buy INTEGER
#     );
#
#     """)
#
#     cur.execute("SELECT model,price FROM cars")
#     # rows=cur.fetchall()
#     # print(rows)
#     for res in cur:
#         print(res['price'])
# def read_ava(n):
#     try:
#         with open(f'avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
# with sqlite3.connect('cars.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#     name TEXT,ava BLOB,score INTEGER
#     )
#     """)
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья',?,1000)", (binary,))
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#     output = write_ava('out.png', img)
#     print(output)

# import sqlite3
#
# # with sqlite3.connect('cars.db') as con:
# #     cur = con.cursor()
# #     with open('sql_dump.sql','w') as f:
# #         for sql in con.iterdump():
# #             f.write(sql)
# with sqlite3.connect('cars_dump.db') as con:
#     cur = con.cursor()
#     with open('sql_dump.sql') as f:
#         sql=f.read()
#         cur.executescript(sql)

# ORM - SQLAlchemy

import os
from sqlalchemy import and_, or_, not_, desc, func, distinct

from models.database import DATABASE_NAME, Session

import create_database as db_creator

from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
    session = Session()
    # print(session.query(Lesson).all())
    # print('*' * 60)
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)
    # print(session.query(Lesson).count())
    # print('*' * 60)
    # for it in session.query(Lesson).filter(not_(Lesson.id > 3),not_( Lesson.lesson_title.like('Ф%'))):
    #     print(it)
    # for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(and_(association_table.c.lesson_id ==
    #                     Lesson.id, Group.group_name == 'MDA-9')):
    #     print(it, gr)
    # print(session.query(Student).filter(Student.age.between(16, 17)).all())
    # print("*" * 60)
    # print(session.query(Student).filter(not_(Student.age.between(16, 17))).all())
    # print("*" * 60)

    # print(session.query(Student).filter(Student.age.like('1%')).all())
    # print("*" * 60)
    # for it in session.query(Student).filter(Student.age.like('1%')).limit(4): print(it)
    # print("*" * 60)
    # for it in session.query(Student).filter(Student.age.like('1%')).limit(4).offset(3): print(it)
    # print("*" * 60)

    # for it in session.query(Student).order_by(Student.surname):print(it)
    # print('*'*60)
    # for it in session.query(Student).order_by(desc(Student.surname)): print(it)
    # print('*' * 60)

    # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'): print(it)
    # print('*' * 60)

    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name): print(it)
    # print('*' * 60)

    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name). \
    #         having(func.count(Student.surname) < 25): print(it)
    # print('*' * 60)
    # for it in session.query(distinct(Student.age)):
    #     print(it)

    # for it in session.query(distinct(Student.age)).filter(Student.age <20):
    #     print(it)

    # for it in session.query(Student.age).filter(Student.age < 20).distinct():
    #     print(it)

    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)
    # i = session.query(Lesson).first()
    # i.lesson_title = 'Информатика'
    # session.add(i)
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)
    #
    # session.query(Lesson).filter(Lesson.lesson_title.like('%м%')).update({'lesson_title': 'М'},
    #                                                                      synchronize_session='fetch')
    # session.commit()
    #
    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)
    # session.add(Lesson(lesson_title='Математика'))
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)
    #
    # i = session.query(Lesson).filter(Lesson.lesson_title=='Физика').first()
    # session.delete(i)
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)

# Jinja  шаблонизатор в питоне
# pip install jinja2

# from jinja2 import Template

# per = {'name': 'Игорь', 'age': 28}
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#
# per = Person('Оля',26)
#
#
#
# tm = Template("Привет {{ p.get_name().upper() }}.Тебе {{ p.get_age()/2+5 }} лет?")
# msg = tm.render(p=per)
#
# print(msg)
# per = [9, 5, 7, 1, 3, 4, 6]
# link = """
# {%- for i in p -%}
# {{ i }}
# {%- endfor %}
#
# """
# tm = Template(link)
# msg = tm.render(p=per)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ялта'},
#     {'id': 5, 'city': 'Ярославль'},
#
# ]
# link = """
# <select name = 'sites'>
#     {% for c in cities -%}
#     {% if c.id >3 -%}
#     <option values='{{ c.id }}'>{{ c.city }}</option>
#     {% elif c.city == 'Москва' %}
#     {{ c.city.upper() }}
#     {% else  %}
#     {{ c.city }}
#     {% endif %}
#     {%- endfor %}
# </select>
# """
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renault', 'price': 44000},
#     {'model': 'Wolksvagen', 'price': 21000},
# ]
# # tpl = "{{ (cs | max(attribute='price')).model }}"
#
# tpl = "{{ cs | random }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.5},
# ]

# tpl = """
# {%- for u in users %}
#    {% filter upper %} {{ u.name }} {% endfilter -%}
#    {%- filter string %} {{ u.year }} - {{ u.weight }} {% endfilter %}
#
# {%- endfor  %}
#
#
# """
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)
# html = """"
# {% macro text_input(name,value='',type='text',size=20) %}
#     <input type='{{ type }}' name = '{{ name }}' value = '{{ value }}' size = '{{ size }}' >
#
# {% endmacro %}
# <p>{{ text_input('username') }}</p>
# <p>{{ text_input('email') }}</p>
# <p>{{ text_input('password','Пароль','password') }}</p>
# """
#
#
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# html = """"
# {% macro text_input(name,placeholder,type='text') %}
#     <input type='{{ type }}' name = '{{ name }}' placeholder=' {{ placeholder }}' >
#
# {% endmacro %}
# <p>{{ text_input('firstname','Имя') }}</p>
# <p>{{ text_input('lastname','Фамилия') }}</p>
# <p>{{ text_input('address','Адрес') }}</p>
# <p>{{ text_input('phone','Телефон','tel') }}</p>
# <p>{{ text_input('email','Емэйл','email') }}</p>
# """
#
#
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.5},
# ]
#
# html = """"
# {% macro list_users(list_of_user) %}
# <ul>
#     {%- for u in list_of_user %}
#     <li>{{ u.name }} {{ caller(u) }}</li>
#     {%- endfor %}
# </ul>
#
#
# {% endmacro %}
# {% call(user) list_users(users) %}
# <ul>
#     <li>age:{{ user.year }}</li>
#     <li>weight:{{ user.weight }}</li>
# </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

from jinja2 import Environment, FileSystemLoader

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.5},
# ]
# subs = ['Культура', 'Наука', "Политика", "Спорт"]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('about2.html')
msg = tm.render()

print(msg)

# Flask pip install flask
# Django фреймворки


