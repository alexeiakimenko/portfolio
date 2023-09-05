import re

while True:
    password = input('Введите пароль:')
    reg = r'^[A-Za-z0-9_@-]{6,18}$'

    pr = re.findall(reg, password)

    if pr == []:
        print(f'Пароль: *{password}* некорректен')
    else:
        print(f'Пароль: *{password}* корректен')
        break
