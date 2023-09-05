import json


class CatalogFilms:
    def __init__(self):
        self.file_name = 'catalog_films.js'

    def introduction_catalog_films(self, film):
        try:
            self.catalog[film[0]] = [film[i] for i in range(1, 9)]
        except:
            self.catalog = {film[0]: [film[i] for i in range(1, 9)]}

        return self.catalog

    def single_film_view(self, title, catalog_films):
        sp_film = ["Жанр", "Режиссёр", "Актёры", "Год выпуска", "Длительность", "Студия производства",
                   "Страна производства", "Рейтинг"]
        print(f'Назвыние фильма: {title}')
        for i in range(0, 8):
            print(f'{sp_film[i]} фильма: {catalog_films[title][i]}')

    def film_error(self, title):
        print(f'Фильма {title} нет в этом каталоге')

    def remove_film(self, title, catalog):
        catalog.pop(title)
        return catalog

    def choice_error(self, choice):
        print(f'Действие {choice} не корректно')

    def save_catalog_films(self, catalog):
        with open(self.file_name, 'w') as f:
            json.dump(catalog, f, indent=2)

    def load_catalog_films(self):
        try:
            with open(self.file_name) as f:
                catalog = json.load(f)
                return catalog
        except FileNotFoundError:
            catalog = {}
            with open(self.file_name, 'w') as f:
                json.dump(catalog, f, indent=2)
