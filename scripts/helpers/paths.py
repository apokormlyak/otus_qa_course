import os.path

FILE_DIR = os.path.dirname(__file__)


def get_path(filename: str) -> str:
    return os.path.join(FILE_DIR, filename)


BOOKS = get_path(filename='books.csv')
USERS = get_path(filename='users.json')
