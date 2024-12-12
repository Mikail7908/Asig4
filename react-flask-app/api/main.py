import logging
from app import app

class Film:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
class Actor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class genre:
    def __init__(self, genre):
        self.genre = genre


def main():
    app.run(debug=True)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info('Script started')
    main()
    logging.info('Script finished')