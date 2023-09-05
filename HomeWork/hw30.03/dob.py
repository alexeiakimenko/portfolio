from math import pi


class Table:
    def __init__(self, width=None, lenght=None, radius=None):
        if radius is None:
            if lenght is None:
                self._width = width
                self._lenght = width
            else:
                self._width = width
                self._lenght = lenght
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError('В дочернем классе должен быть метод calc_area()')


class SqTable(Table):
    def calc_area(self):
        return self._width * self._lenght


class RoundTable(Table):
    def calc_area(self):
        return round(self._radius ** 2 * pi, 2)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())
t2 = SqTable(20)
print(t2.__dict__)
print(t2.calc_area())
t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())
