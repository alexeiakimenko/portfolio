from random import randint

a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
print('Стороны параллелепипеда:')
print('a=', a)
print('b=', b)
print('c=', c)


def area_surface(a1, b1, c1):
    area_sur = 0

    def area_sizes():
        nonlocal area_sur
        s1 = a1 * b1
        s2 = a1 * c1
        s3 = b1 * c1
        area_sur = 2 * (s1 + s2 + s3)

    area_sizes()
    print('Площадь поверхности параллелепипеда:', area_sur)


area_surface(a, b, c)
