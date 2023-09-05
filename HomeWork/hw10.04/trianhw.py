class Check:

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 0 or not isinstance(value, int):
            raise TypeError('Сторона треугольника должна быть целым положительным числом')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Triangle:
    a = Check()
    b = Check()
    c = Check()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if a < (b + c) and b < (a + c) and c < (a + b):
            print(f'треугольник со сторонами ({a},{b},{c}) существует')
        else:
            print(f'треугольник со сторонами ({a},{b},{c}) не существует')


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
