from sqlalchemy.orm  import Session

from app import crud
from app.schemas.book import BookCreate, BookUpdate
from app.tests.utils.utils import random_lower_string, random_int_number
from app.tests.utils.book import create_random_book


def test_create_book(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    book_in = BookCreate(title=title, description=description)
    book = crud.book.create(db=db, obj_in=book_in)
    assert book.title == title
    assert book.description == description

def test_update_book(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    book_in = BookCreate(title=title, description=description)
    db_book = create_random_book(db=db)
    book = crud.book.update(db=db, db_obj=db_book, obj_in=book_in)
    assert book.title == title
    assert book.description == description

def test_delete_book(db: Session) -> None:
    book = create_random_book(db=db)
    book_rm = crud.book.remove(db=db, id=book.id)
    assert  book_rm.title == book.title
    assert  book_rm.description == book.description
    assert  book_rm.id == book.id

def test_get_book(db: Session) -> None:
    book = create_random_book(db=db)
    book_out = crud.book.get(db=db, id=book.id)
    assert book_out.id == book.id

def test_get_multi_book(db: Session) -> None:
    for x in range(3):
        book_in = create_random_book(db=db)
    db_books = crud.book.get_multi(db=db)
    assert len(db_books) >= 3

def test_get_by_title(db: Session) -> None:
    book_in= create_random_book(db=db)
    db_books = crud.book.get_multi(db=db,title=book_in.title)
    assert 1 == len(db_books)
