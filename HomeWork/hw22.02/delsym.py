st = input('Введите строку: ')
sym = input('Введите символ для удаления: ')


def delsym(s, symbol):
    i = 0
    st2 = ""
    while i < len(s):
        if s[i] != symbol:
            st2 = st2 + s[i]
        i += 1
    return st2


st_new = delsym(st, sym)
print('Первоначальная строка: ', st)
print('Изменённая строка: ', st_new)
