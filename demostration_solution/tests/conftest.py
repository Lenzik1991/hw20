from unittest.mock import MagicMock

import pytest

#from dao.director import DirectorDAO У МЕНЯ НЕ РАБОТАЕТ ТАК
#from dao.model.director import Director У МЕНЯ НЕ РАБОТАЕТ ТАК

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.genre import Genre
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="John")
    d2 = Director(id=2, name="Aleks")
    d3 = Director(id=1, name="Kevin")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Comedy")
    genre_2 = Genre(id=2, name="Thriller")
    genre_3 = Genre(id=1, name="Drama")

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=genre_3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title="Movie_1", description="Description", year=2020)
    movie_2 = Movie(id=2, title="Movie_2", year=1999, rating=10)
    movie_3 = Movie(id=1, title="Movie_3", genre_id=1, trailer="...")

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=movie_3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao

