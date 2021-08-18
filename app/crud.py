from app.schemas import author
from sqlalchemy.orm import Session

from app import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_author_by_name(db: Session, name: str):
    return db.query(models.Author).filter(models.Author.name == name).first()

def get_authors(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Author).offset(skip).limit(limit).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name, books=author.books)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    db_author = db.query(models.Author).filter_by(id=author_id).first()
    db.delete(db_author)
    db.commit()
    return db_author

def update_author(db: Session, db_author: schemas.AuthorInDB, author: schemas.AuthorUpdate):
    db_author.name = author.name
    db_author.books = author.books  
    db.commit()
    db.refresh(db_author)
    return db_author


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_books(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter_by(id=book_id).first()
    db.delete(db_book)
    db.commit()
    return db_book

def update_book(db: Session, db_book: schemas.BookInDB, book: schemas.BookUpdate):
    db_book.title = book.title
    db_book.description = book.description 
    db.commit()
    db.refresh(db_book)
    return db_book