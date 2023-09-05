st = input('Введите строку: ')
n = int(input('Введите номер позиции для удаления: '))


def delsym(s, num):
    i = 0
    st2 = ""
    while i < len(s):
        if i != num:
            st2 = st2 + s[i]
        i += 1
    return st2


st_new = delsym(st, n)
print('Первоначальная строка: ', st)
print('Изменённая строка: ', st_new)
