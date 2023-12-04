import logging
import os
import json

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


class Movie:
    def __init__(self, title: str):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self) -> list[str]:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()

        # Vérifier que le fim n'est pas déjà dans la liste
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            # Si c'est déjà le cas, on renvoie une exception
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False

    def remove_from_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            # Si c'est déjà le cas, on renvoie une exception
            logging.warning(f"Le film {self.title} n'existe pas dans la liste.")


def get_movies():
    with open(DATA_FILE, 'r') as f:
        movies_title = json.load(f)

    return [Movie(movie_title) for movie_title in movies_title]


if __name__ == "__main__":
    print(get_movies())

