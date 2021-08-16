from app.models import author
from starlette.datastructures import Secret
from app.models.book import Book
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from .database import SessionLocal, engine, Base


#Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Ativo"}

@app.post("/books/", response_model=schemas.Book)
async def create_books(
    book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud.create_book(db=db, book=book)

@app.get("/books/{book_id}", response_model=schemas.Book)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")
    return db_book

@app.get("/books/title/{title}", response_model=schemas.Book)
async def read_book_by_title(title: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db, title=title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="There is no book with the title!")
    return db_book

@app.get("/books/", response_model=List[schemas.Book])
async def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.post("/authors/", response_model=schemas.Author)
async def create_authors(
    author: schemas.AuthorCreate, db: Session = Depends(get_db)
):
    for i in range(len(author.books_id)):
        book_db = db.query(models.Book).filter(models.Book.id == author.books_id[i]).first()
        if book_db is None:
            raise HTTPException(status_code=404, detail=f"Book ID = {i+1} not found!")
        else:
            author.books.append(book_db)
    return crud.create_author(db=db, author=author)

@app.get("/authors/{author_id}", response_model=schemas.Author)
async def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_book(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found!")
    return db_author

@app.get("/authors/name/{name}", response_model=schemas.Author)
async def read_author_by_name(name: str, db: Session = Depends(get_db)):
    db_author = crud.get_author_by_name(db=db, name=name)
    if db_author is None:
        raise HTTPException(status_code=404, detail="There is no Author with the name!")
    return db_author

@app.get("/authors/", response_model=List[schemas.Author])
async def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors

@app.delete("/books/{book_id}", response_model=schemas.Book)
async def remove_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")
    return db_book

@app.delete("/authors/{author_id}", response_model=schemas.Author)
async def remove_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db=db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found!")
    return db_author