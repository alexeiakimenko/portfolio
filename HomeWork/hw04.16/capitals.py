import json

try:
    dic_capitals = json.load(open('capitals.json'))
except FileNotFoundError:
    dic_capitals = {}


def add_country(country, capital):
    try:
        dic_capitals = json.load(open('capitals.json'))
    except FileNotFoundError:
        dic_capitals = {}

    dic_capitals[country] = capital

    with open('capitals.json', 'w') as f:
        json.dump(dic_capitals, f, indent=2)


def del_country(country):
    dic_capitals.pop(country)
    with open('capitals.json', 'w') as f:
        json.dump(dic_capitals, f, indent=2)


def search_country(country):
    dic_capitals = json.load(open('capitals.json'))
    try:
        print(f'Страна: {country} ,её столица: {dic_capitals[country]} ')
    except KeyError:
        print('Эта страна не внесена или её не существует')


def view_country():
    dic_capitals = json.load(open('capitals.json'))

    for k in dic_capitals:
        print(f'Страна: {k} ,её столица:{dic_capitals[k]}  ')


while True:
    print('*' * 50)
    print('Выбор действия:')
    print('1-добавление данных')
    print('2-удаление данных')
    print('3-поиск данных')
    print('4-редактирование данных')
    print('5-просмотр данных')
    print('6-завершение работы')
    action = input('Ввод:')
    if action == '6':
        break
    elif action == '1':
        country = input('Введите название страны(с заглавной буквы):')
        capital = input('Введите название столицы(с заглавной буквы):')
        add_country(country, capital)
    elif action == '2':
        country = input('Введите название страны(с заглавной буквы) которую хотите удалить:')
        del_country(country)
    elif action == '3':
        country = input('Введите название страны(с заглавной буквы) которую хотите найти:')
        search_country(country)
    elif action == '4':
        country = input('Введите название страны,столицу которой хотите изменить: ')
        capital = input('Введите новое название столицы: ')
        add_country(country, capital)
    elif action == '5':
        view_country()

    else:
        print('Такой символ не применим.')
