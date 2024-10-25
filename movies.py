class VideoRental:

    def __init__(self, movies):
        self.__movies = {}
        for movie in movies:
            self.__movies[movie] = True

    def rent_movie(self, name):
        if name not in self.__movies:
            return False
        elif not self.__movies[name]:  # movie key will hold "False" if already rented...
            return False

        self.__movies[name] = False
        return True

    def check_available_movies(self):
        available_movies = []
        for movie, available in self.__movies.items():
            if available:
                available_movies.append(movie)

        return available_movies

    def return_movie(self, name):
        if name not in self.__movies:
            return False
        elif self.__movies[name]:  # movie key will hold "True" if not rented...
            return False

        self.__movies[name] = True
        return True

