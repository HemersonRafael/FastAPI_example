from sqlalchemy.orm  import Session
from fastapi.encoders import jsonable_encoder

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
    book1 = crud.book.create(db=db, obj_in=book_in)
    description2 = random_lower_string()
    book_update = BookUpdate(title=title, description=description2)
    book2 = crud.book.update(db=db, db_obj=book1, obj_in=book_update) 
    assert book1.id == book2.id
    assert book1.title == book2.title
    assert book2.description == description2
    assert book2.description != description


def test_delete_book(db: Session) -> None:
    book = create_random_book(db=db)
    rm_book = crud.book.remove(db=db, id=book.id)
    stored_book = crud.book.get(db=db, id=rm_book.id)
    assert  stored_book is None
    assert  jsonable_encoder(rm_book) == jsonable_encoder(book)


def test_get_book_by_id(db: Session) -> None:
    book = create_random_book(db=db)
    stored_book = crud.book.get(db=db, id=book.id)
    assert stored_book.id == book.id


def test_get_multi_book(db: Session) -> None:
    num = random_int_number()
    books_id = []
    for x in range(num):
        book = create_random_book(db=db)
        books_id.append(book.id)
    stored_books = crud.book.get_multi(db=db)
    count = 0
    for std_book in stored_books:
        for id in books_id:
            if std_book.id == id:
                count+=1
    assert count == num


def test_get_book_by_title(db: Session) -> None:
    book_in = create_random_book(db=db)
    stored_books = crud.book.get_multi(db=db,title=book_in.title)
    assert len(stored_books) == 1