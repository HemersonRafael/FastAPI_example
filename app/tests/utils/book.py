from sqlalchemy.orm  import Session

from app import crud
from app.models.book import Book
from app.schemas.book import BookCreate
from app.tests.utils.utils import random_lower_string


def create_random_book(db: Session) -> Book:
    title = random_lower_string()
    description = random_lower_string()
    book_in = BookCreate(title=title, description=description)
    book = crud.book.create(db=db, obj_in=book_in)
    return book