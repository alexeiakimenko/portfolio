class Automobile:
    def __init__(self, model='m', year=0, made='m', power=0, color='c', price=0):
        self.model = model
        self.year = year
        self.made = made
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print('Название модели:', self.model)
        print('Год выпуска:', self.year, 'г.')
        print('Производитель:', self.made)
        print('Мощность двигателя:', self.power, 'л.с.')
        print('Цвет машины:', self.color)
        print('Цена:', self.price, "RUB")

    def input_model(self):
        self.model = input('Введите название модели: ')

    def input_year(self):
        self.year = input('Введите  год выпуска: ')
        self.year = input_int(self.year)

    def input_made(self):
        self.made = input('Введите имя производителя: ')

    def input_power(self):
        self.power = input('Введите мощность двигателя: ')
        self.power = input_int(self.power)

    def input_color(self):
        self.color = input('Введите цвет модели: ')

    def input_price(self):
        self.price = input('Введите цену модели: ')
        self.price = input_int(self.price)


def input_int(i):
    while True:

        try:
            int(i)
            return i
        except ValueError:
            try:
                i = int(input('Введите числовое значение:'))
            except ValueError:
                print('Опять не верно!')


auto = Automobile()
auto.input_model()
auto.input_year()
auto.input_made()
auto.input_power()
auto.input_color()
auto.input_price()

print('Данные автомобиля'.center(50, '*'))
auto.print_info()
print('=' * 50)
while True:
    print("Что вы хотели бы изменить?")
    print('1-Название модели.')
    print('2-Год выпуска.')
    print('3-Производителя.')
    print('4-Мощность двигателя.')
    print('5-Цвет машины.')
    print('6-Цену машины.')
    print('Любой другой символ прекращает редактирование!')
    r = input('->')
    if r == '1':
        auto.input_model()
    elif r == '2':
        auto.input_year()
    elif r == '3':
        auto.input_made()
    elif r == '4':
        auto.input_power()
    elif r == '5':
        auto.input_color()
    elif r == '6':
        auto.input_price()
    else:
        break
print('Данные автомобиля'.center(50, '*'))
auto.print_info()
print('=' * 50)
