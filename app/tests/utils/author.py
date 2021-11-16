from sqlalchemy.orm import Session

from app import crud
from app.models.author import Author
from app.schemas.author import AuthorCreate
from app.tests.utils.utils import random_lower_string, random_int_number
from app.tests.utils.book import create_random_book


def create_random_author(db: Session) -> Author:
    name = random_lower_string()
    books_id = []
    books = []
    for x in range(random_int_number()):
        book_in = create_random_book(db=db)
        books.append(book_in)
        books_id.append(book_in.id)
    author_in = AuthorCreate(name=name, books_id=books_id)
    author_in.books = books
    author = crud.author.create(db=db, obj_in=author_in)
    return author