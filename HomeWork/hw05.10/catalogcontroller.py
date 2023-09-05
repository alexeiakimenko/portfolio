from catalogview import UserInterface
from catalogmodel import CatalogFilms


class Controller:
    catalog_films = {}

    def __init__(self):
        self.user_interface = UserInterface()
        self.film_model = CatalogFilms()

    def run(self):
        self.catalog_films = self.film_model.load_catalog_films()
        choice = None
        while choice != "q":
            choice = self.user_interface.choice_user()
            self.choice_made(choice)

    def choice_made(self, choice):
        if choice == '1':
            film = self.user_interface.made_film()
            self.catalog_films = self.film_model.introduction_catalog_films(film)


        elif choice == '2':
            self.user_interface.show_catalog_films(self.catalog_films)
        elif choice == '3':
            title_film = self.user_interface.get_single_film()
            try:
                self.film_model.single_film_view(title_film, self.catalog_films)
            except KeyError:
                self.film_model.film_error(title_film)
        elif choice == '4':
            title_film = self.user_interface.get_single_film()
            try:
                self.catalog_films = self.film_model.remove_film(title_film, self.catalog_films)
            except KeyError:
                self.film_model.film_error(title_film)

        elif choice == 'q':
            self.film_model.save_catalog_films(self.catalog_films)
        else:
            self.film_model.choice_error(choice)
