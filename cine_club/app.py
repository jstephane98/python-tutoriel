from PySide6 import QtWidgets, QtCore
from movie import get_movies, Movie


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné club")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.line_edit = QtWidgets.QLineEdit()
        self.btn_ajouter = QtWidgets.QPushButton("Ajouter un film")
        self.list_film = QtWidgets.QListWidget()
        self.list_film.setSelectionMode(QtWidgets.QListWidget.SelectionMode.ExtendedSelection)
        self.btn_supprimer = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.btn_ajouter)
        self.layout.addWidget(self.list_film)
        self.layout.addWidget(self.btn_supprimer)

    def setup_connections(self):
        self.btn_ajouter.clicked.connect(self.add_movie)
        self.btn_supprimer.clicked.connect(self.delete_movie)
        self.line_edit.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            self.set_movie_in_list_film(movie)

    def add_movie(self):
        movie_title = self.line_edit.text()
        if not movie_title:
            return False

        movie = Movie(movie_title)

        if movie.add_to_movies():
            self.set_movie_in_list_film(movie)

        self.line_edit.clear()

    def set_movie_in_list_film(self, movie):
        film_item = QtWidgets.QListWidgetItem(movie.title)
        film_item.movie = movie
        self.list_film.addItem(film_item)

    def delete_movie(self):
        for selected_item in self.list_film.selectedItems():
            movie = selected_item.movie
            movie.remove_from_movies()
            self.list_film.takeItem(self.list_film.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()
