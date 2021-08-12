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

@app.get("/books/", response_model=List[schemas.Book])
async def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")
    return db_book

@app.get("/books/title/{title}", response_model=schemas.Book)
async def read_book(title: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db, title=title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="There is no book with the title!")
    return db_book

@app.post("/authors/", response_model=schemas.Author)
async def create_authors(
    author: schemas.AuthorCreate, db: Session = Depends(get_db)
):
    return crud.create_author(db=db, author=author)

@app.get("/authors/{author_id}", response_model=schemas.Author)
async def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_book(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found!")
    return db_author

@app.get("/authors/name/{name}", response_model=schemas.Author)
async def read_authors(name: str, db: Session = Depends(get_db)):
    return crud.get_author_by_name(db=db, name=name)