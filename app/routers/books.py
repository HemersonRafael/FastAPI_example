from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas, dependencies


router = APIRouter()


@router.post("/books/", response_model=schemas.Book)
async def create_books(
    book: schemas.BookCreate, db: Session = Depends(dependencies.get_db)
):
    return crud.create_book(db=db, book=book)

@router.get("/books/{book_id}", response_model=schemas.Book)
async def read_book(
    book_id: int, db: Session = Depends(dependencies.get_db)
):
    db_book = crud.get_book(db, book_id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")

    return db_book

@router.get("/books/?title={title}", response_model=schemas.Book)
async def read_book_by_title(
    title: str, db: Session = Depends(dependencies.get_db)
):
    db_book = crud.get_book_by_title(db, title=title)

    if db_book is None:
        raise HTTPException(status_code=404, detail="There is no book with the title!")

    return db_book

@router.get("/books/", response_model=List[schemas.Book])
async def read_books(
    skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)
):
    books = crud.get_books(db, skip=skip, limit=limit)

    return books

@router.delete("/books/{book_id}", response_model=schemas.Book)
async def remove_book(
    book_id: int, db: Session = Depends(dependencies.get_db)
):
    db_book = crud.delete_book(db=db, book_id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")

    return db_book

@router.put("/books/{book_id}", response_model=schemas.Book)
async def alter_book(
    book: schemas.BookUpdate, book_id: int, db: Session = Depends(dependencies.get_db)
):
    db_book = db.query(models.Book).filter_by(id=book_id).first()

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")

    return crud.update_book(db=db, db_book=db_book, book=book)