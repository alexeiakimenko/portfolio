from random import randint

a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
print('Стороны параллелепипеда:')
print('a=', a)
print('b=', b)
print('c=', c)
area_sur = 0


def area_surface(a1, b1, c1):
    global area_sur  # объявляем глобальной

    def area_sizes():
        s1 = a1 * b1
        s2 = a1 * c1
        s3 = b1 * c1
        return s1, s2, s3

    area1 = area_sizes()

    area_sur = 2 * sum(area1)


area_surface(a, b, c)

print('Площадь поверхности параллелепипеда:', area_sur)
