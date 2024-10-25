from movies import VideoRental
import pytest


@pytest.fixture
def store():
    movies = [
        "Toy Story",
        "Batman Begins",
        "Star Wars: A New Hope",
        "How To Train Your Dragon",
        "Venom 3"]

    return VideoRental(movies)


def test_rent_movie(store):
    assert store.rent_movie("Toy Story")


def test_rent_unavailable_movie(store):
    store.rent_movie("Toy Story")
    assert not store.rent_movie("Toy Story")


def test_check_available_movies(store):
    store.rent_movie("Toy Story")
    # note that 'Toy Story' is not present in this comparison list...
    movies = [
        "Batman Begins",
        "Star Wars: A New Hope",
        "How To Train Your Dragon",
        "Venom 3"]

    assert store.check_available_movies() == movies


def test_return_movie(store):
    store.rent_movie("Toy Story")
    assert store.return_movie("Toy Story")


def test_return_non_rented_movie(store):
    assert not store.return_movie("Toy Story")