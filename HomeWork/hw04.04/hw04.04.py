class Clock:
    __DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError('секунды должны быть целым числом')
        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}'

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')

        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        return self.sec == other.sec

    def __ne__(self, other):
        return self.sec != other.sec

    def __lt__(self, other):
        return self.sec < other.sec

    def __gt__(self, other):
        return self.sec > other.sec


cl1 = Clock(600)
cl2 = Clock(200)

cl3 = cl1 + cl2

print(f'c1: {cl1.get_format_time()}')
print(f'c2: {cl2.get_format_time()}')
print(f'c1+c2: {cl3.get_format_time()}')
cl1 += cl2
print(f'c1+=c2: {cl1.get_format_time()}')
cl1 = Clock(600)
cl2 = Clock(200)
cl3 = cl1 - cl2
print(f'c1-c2: {cl3.get_format_time()}')
cl1 -= cl2
print(f'c1-=c2: {cl1.get_format_time()}')
cl1 = Clock(600)
cl2 = Clock(200)
cl3 = cl1 * cl2
print(f'c1*c2: {cl3.get_format_time()}')
cl1 *= cl2
print(f'c1*=c2: {cl1.get_format_time()}')
cl1 = Clock(600)
cl2 = Clock(200)
cl3 = cl1 // cl2
print(f'c1//c2: {cl3.get_format_time()}')
cl1 //= cl2
print(f'c1//=c2: {cl1.get_format_time()}')
cl1 = Clock(600)
cl2 = Clock(200)
cl3 = cl1 % cl2
print(f'c1%c2: {cl3.get_format_time()}')
cl1 %= cl2
print(f'c1%=c2: {cl1.get_format_time()}')
cl1 = Clock(600)
cl2 = Clock(200)
if cl1 == cl2:
    print('Время равно')
else:
    print('Время не равно')
if cl1 != cl2:
    print('c1 не равно с2')
if cl1 > cl2:
    print('c1 больше с2')
if cl1 < cl2:
    print('c1 меньше с2')
