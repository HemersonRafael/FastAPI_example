from typing import Any, List, Optional

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, dependencies


router = APIRouter()


@router.post("/books/", response_model=schemas.Book)
async def create_book(
    book_in: schemas.BookCreate, db: Session = Depends(dependencies.get_db)
) -> Any:
    """
    Create new book.
    """
    return crud.book.create(db=db, obj_in=book_in)

@router.put("/books/{book_id}", response_model=schemas.Book)


async def update_book(
    book_in: schemas.BookUpdate, 
    book_id: int, 
    db: Session = Depends(dependencies.get_db)
) -> Any:
    """
    Update a book.
    """
    db_book = crud.book.get(db=db, id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")

    return crud.book.update(db=db, db_obj=db_book, obj_in=book_in)


@router.get("/books/{book_id}", response_model=schemas.Book)
async def read_book(
    book_id: int, db: Session = Depends(dependencies.get_db)
) -> Any:
    """
    Get book by ID.
    """
    db_book = crud.book.get(db=db, id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")

    return db_book


@router.get("/books/", response_model=List[schemas.Book])
async def read_books(
    title: Optional[str] = None, 
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(dependencies.get_db)
) -> Any:
    """
    Retrieve books.
    """
    return crud.book.get_multi(db=db, title=title, skip=skip, limit=limit)


@router.delete("/books/{book_id}", response_model=schemas.Book)
async def delete_book(
    book_id: int, db: Session = Depends(dependencies.get_db)
) -> Any:
    """
    Delete a book.
    """
    db_book = crud.book.get(db=db, id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found!")

    return crud.book.remove(db=db, id=book_id)