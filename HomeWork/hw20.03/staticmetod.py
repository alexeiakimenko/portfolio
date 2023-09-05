class Static:

    @staticmethod
    def maximum(n1, n2, n3, n4):
        print(f'Максимальное число: {max(n1, n2, n3, n4)}')

    @staticmethod
    def minimum(n1, n2, n3, n4):
        print(f'Минимальное число: {min(n1, n2, n3, n4)}')

    @staticmethod
    def arith_mean(n1, n2, n3, n4):
        print(f'Среднее арифметическое: {(n1 + n2 + n3 + n4) / 4}')

    @staticmethod
    def factorial(n):
        ch = n
        res = 1
        while n > 0:
            res = res * n
            n = n - 1
        print(f'Факториал числа {ch} равен {res}')


Static.maximum(3, 5, 7, 9)
Static.minimum(3, 5, 7, 9)
Static.arith_mean(3, 5, 7, 9)
Static.factorial(5)
