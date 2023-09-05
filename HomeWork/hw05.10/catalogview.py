def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, "="))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def choice_user(self):
        print('Действия с фильмами:')
        print('1 - добавление фильма')
        print('2 - каталог фильмов')
        print('3 - просмотр определённого фильма')
        print('4 - удаление фильма')
        print('q - выход из программы')
        choice = input('Выберите вариант действия: ')
        return choice

    @add_title('Ввод данных фильма')
    def made_film(self):
        a = ''
        sp_film = ["название", "жанр", "режиссёра", "актёры", "год выпуска", "длительность", "студию производства",
                   "страну производства", "рейтинг"]
        film = []
        for i in sp_film:
            a = input(f'Введите {i} фильма: ')
            film.append(a)

        return film

    @add_title('Каталог фильмов')
    def show_catalog_films(self, catalog_films):
        for key, value in enumerate(catalog_films, 1):
            print(
                f'{key}.Название фильма: {value}, жанр: {catalog_films[value][0]}, рейтинг: {catalog_films[value][7]}')

    def get_single_film(self):
        single_film = input('Введите название фильма: ')
        return single_film


