from os import name
from sqlalchemy.orm import Session

from app import crud
from app.crud import author
from app.schemas import AuthorCreate, AuthorUpdate
from app.tests.utils.author import create_random_author
from app.tests.utils.utils import random_lower_string, random_int_number
from app.tests.utils.book import create_random_book


def test_create_author(db: Session) -> None:
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
    assert author.name == name
    assert len(author.books) == len(books_id)


def test_update_author(db:  Session) -> None:
    name = random_lower_string()
    books_id = []
    books = []
    for x in range(random_int_number()):
        book_in = create_random_book(db=db)
        books.append(book_in)
        books_id.append(book_in.id)
    author_in = AuthorCreate(name=name, books_id=books_id)
    author_in.books = books
    author1 = crud.author.create(db=db, obj_in=author_in)
    author_in = AuthorUpdate(name=name, books_id=[])
    author_in.books = []
    author2 = crud.author.update(db=db, db_obj= author1, obj_in=author_in)
    assert author1.name == author2.name
    assert author2.books == []
    assert len(author2.books) != len(books)


def test_delete_author(db: Session) -> None:
    book =  create_random_author(db=db)
    rm_book = crud.author.remove(db=db, id= book.id)
    stored_book = crud.author.get(db=db, id=rm_book.id)
    assert stored_book is None
    assert rm_book.id == book.id


def test_get_author_by_id(db: Session) -> None:
    book = create_random_author(db=db)
    stored_book = crud.author.get(db=db, id=book.id)
    assert book.id == stored_book.id


def test_get_multi_author(db: Session) -> None:
    num = random_int_number()
    authors_id = []
    for x in range(num):
        author_in = create_random_author(db=db)
        authors_id.append(author_in.id)
    stored_authors = crud.author.get_multi(db=db)
    count = 0
    for author in stored_authors:
        for x in authors_id:
            if x == author.id:
                count+=1
    assert num == count


def test_get_multi_author_by_name(db: Session) -> None:
    author = create_random_author(db=db)
    stored_author = crud.author.get_multi(db=db, name=author.name)
    assert len(stored_author) == 1