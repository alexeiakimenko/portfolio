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

    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):

        print('1-Создание статьи')
        print('2-Просмотр статей')
        print('3-Просмотр определённой статьи')
        print('4-Удаление статьи')
        print('q-выход из программы')
        user_answer = input('Выберите варианты действия')

        return user_answer

    def add_user_article(self):
        dict_article = {
            'название': None,
            'автор': None,
            'количество страниц': None,
            'описание': None
        }

        print('Создание статьи'.center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи')
        return dict_article

    def show_all_articles(self, articles):
        print('Список статей'.center(50, '='))
        for ind, article in enumerate(articles, 1):
            print(f'{ind}. {article}')
        print('=' * 50)

    @add_title('Просмотр статьи.')
    def show_single_article(self, article):
        for key in article:
            print(f'{key} статьи = {article[key]}')

    def get_user_interface(self):
        user_article = input('Введите название статьи')
        return user_article

    @add_title('Сообщение об ошибке')
    def show_incorrect_title_error(self, user_title):
        print(f'Статьи с названием {user_title} не существует.')

    @add_title('Удаление статьи')
    def remove_single_article(self, article):
        print(f'Статья {article} - была удалена.')

    @add_title('Сообщение об ошибке.')
    def show_inccorect_answer_error(self, answer):
        print(f'Вариант {answer} не существует')

    @add_title('Ввод назавания статьи')
    def get_user_article(self):
        user_article = input('Введите название статьи: ')
        return user_article
