import re


class Acount:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.verify_name_client(surname)
        self.verify_num(num)
        self.verify_percent(percent)
        self.verify_value(value)
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Acount.convert(self.value, Acount.rate_usd)
        print(f'Состояние счёта: {usd_val} {Acount.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Acount.convert(self.value, Acount.rate_eur)
        print(f'Состояние счёта: {eur_val} {Acount.suffix_eur}.')

    def add_percents(self):
        print('Проценты начислены!')
        self.value = self.value + self.value * self.percent
        self.print_balance()

    def with_draw_money(self, val):
        if val > self.value:
            print(f'К сожалению у вас нет {val} {Acount.suffix}.')
            self.print_balance()
        else:
            self.value -= val
            print(f'{val} {Acount.suffix} успешно сняты!')
            self.print_balance()

    def add_money(self, val):
        print(f'{val} {Acount.suffix} успешно зачислены!')
        self.value += val
        self.print_balance()

    def edit_owner(self, surname):
        self.verify_name_client(surname)
        self.surname = surname

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Acount.suffix}')

    def print_info(self):
        print('Информация о счёте:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')

        print('-' * 20)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.num} принадлежащий {self.surname} был закрыт.')

    @staticmethod
    def verify_name_client(surname):
        a = re.findall(r'[А-ЯЁ][а-яё]*', surname)
        if not isinstance(surname, str) or a[0] != surname:
            raise TypeError(
                'Имя клиента должно быть строкой,начинаться с заглавной буквы и дальше содержать только маленькие буквы')

    @staticmethod
    def verify_num(num):
        if not isinstance(num, str) or not num.isdigit():
            raise TypeError('Номер счёта должен быть строкой содержащий только цифры')
        s = len(num)
        if s < 5 or s > 7:
            raise TypeError('В номере счёта должно быть от пяти до семи цифр')

    @staticmethod
    def verify_percent(per):
        if not isinstance(per, float):
            raise TypeError('Начисляемые проценты должны быть вещественным числом')
        if per != 0.03:
            raise TypeError('По этому счёту начисляются только 3%')

    @staticmethod
    def verify_value(value):
        if not isinstance(value, float):
            raise TypeError('Баланс счёта должен быть вещественным числом')
        if value < 1000:
            raise TypeError(f'Для открытия счёта нужна сумма не менее 1000.0 {Acount.suffix}')


acc = Acount('Долгих', '12345', 0.03, 1000.0)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.set_usd_rate(2)
acc.convert_to_usd()
acc.set_eur_rate(.5)
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_percents()
print()
acc.with_draw_money(100)
print()
acc.add_money(5000)
print()
