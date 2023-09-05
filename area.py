from math import pi


def area_triangle(a, b):
    return a * b / 2


def area_rectangle(a, b):
    return a * b


def area_circle(a):
    return round(pi * a * a, 2)


print("Выбрать площадь какой фигуры вы хотите найти.")
f = input("1-треугольник; 2-прямоугольник;3-круг: ")
if f == "1":
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    print("Площадь треугольника:", area_triangle(base, height))
if f == "2":
    height = float(input("Введите высоту прямоугольника: "))
    width = float(input("Введите ширину прямоугольника"))
    print("Площадь прямоугольника:", area_rectangle(height, width))
if f == "3":
    radius = float(input("Введите радиус круга: "))
    print("Площадь круга: ", area_circle(radius))
