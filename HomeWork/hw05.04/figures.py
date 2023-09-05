from abc import abstractmethod
from math import sqrt


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area_figure(self, *args):
        if len(args) == 1:
            area = args[0] ** 2

        if len(args) == 2:
            area = args[0] * args[1]

        if len(args) == 3:
            p = (args[0] + args[1] + args[2]) / 2
            area = sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
            area = round(area, 2)

        return area

    @abstractmethod
    def per_figure(self, *args):
        if len(args) == 1:
            per = args[0] * 4

        if len(args) == 2:
            per = (args[0] + args[1]) * 2

        if len(args) == 3:
            per = args[0] + args[1] + args[2]

        return per

    @abstractmethod
    def pic_figure(self, *args):
        if len(args) == 1:
            i = 0
            while i < args[0]:
                print('*' * args[0])
                i += 1
        if len(args) == 2:
            i = 0
            while i < args[0]:
                print('*' * args[1])
                i += 1
        if len(args) == 3:
            i = 1
            while i <= 11:
                print(('*' * i).center(12))
                i += 2

    @abstractmethod
    def info_figure(self, *args):
        if len(args) == 1:
            print(('Квадрат').center(30, '='))
            print('Сторона:', args[0])
            print('Цвет:', self.color)
            print('Площадь:', self.area_figure(args[0]))
            print('Периметр:', self.per_figure(args[0]))
            self.pic_figure(args[0])
        if len(args) == 2:
            print(('Прямоугольник').center(30, '='))
            print('Длина:', args[0])
            print('Ширина:', args[1])
            print('Цвет:', self.color)
            print('Площадь:', self.area_figure(args[0], args[1]))
            print('Периметр:', self.per_figure(args[0], args[1]))
            self.pic_figure(args[0], args[1])
        if len(args) == 3:
            print(('Треугольник').center(30, '='))
            print('Сторона1:', args[0])
            print('Сторона2:', args[1])
            print('Сторона3:', args[2])
            print('Цвет:', self.color)
            print('Площадь:', self.area_figure(args[0], args[1], args[2]))
            print('Периметр:', self.per_figure(args[0], args[1], args[2]))
            self.pic_figure(args[0], args[1], args[2])


class Square(Shape):

    def __init__(self, side1, color):
        super().__init__(color)
        self.side1 = side1
        super().info_figure(self.side1)


class Rectangle(Shape):
    def __init__(self, side1, side2, color):
        super().__init__(color)
        self.width = side1
        self.height = side2
        super().info_figure(self.width, self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().info_figure(self.side1, self.side2, self.side3)


sq = int(input('Введите сторону квадрата->'))
rec1 = int(input('Введите длину прямоугольника->'))
rec2 = int(input('Введите ширину прямоугольника->'))
figures = [
    Square(sq, 'red'),
    Rectangle(rec1, rec2, 'green'),
    Triangle(11, 6, 6, 'yellow')
]

for i in figures:
    i
