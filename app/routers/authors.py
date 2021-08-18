from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas, dependencies


router = APIRouter()


@router.post("/authors/", response_model=schemas.Author)
async def create_authors(
    author: schemas.AuthorCreate, db: Session = Depends(dependencies.get_db)
):
    for i in range(len(author.books_id)):
        book_db = db.query(models.Book).filter(models.Book.id == author.books_id[i]).first()

        if book_db is None:
            raise HTTPException(status_code=404, detail=f"Book ID = {i+1} not found!")
        else:
            author.books.append(book_db)

    return crud.create_author(db=db, author=author)

@router.get("/authors/{author_id}", response_model=schemas.Author)
async def read_author(
    author_id: int, db: Session = Depends(dependencies.get_db)
):
    db_author = crud.get_book(db, author_id)

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found!")

    return db_author

@router.get("/authors/?name={name}", response_model=schemas.Author)
async def read_author_by_name(
    name: str, db: Session = Depends(dependencies.get_db)
):
    db_author = crud.get_author_by_name(db=db, name=name)

    if db_author is None:
        raise HTTPException(status_code=404, detail="There is no Author with the name!")

    return db_author

@router.get("/authors/", response_model=List[schemas.Author])
async def read_authors(
    skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)
):
    authors = crud.get_authors(db, skip=skip, limit=limit)

    return authors

@router.delete("/authors/{author_id}", response_model=schemas.Author)
async def remove_author(
    author_id: int, db: Session = Depends(dependencies.get_db)
):
    db_author = crud.delete_author(db=db, author_id=author_id)

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found!")

    return db_author

@router.put("/authors/{author_id}", response_model=schemas.Author)
async def alter_author(
    author: schemas.AuthorCreate, author_id: int, db: Session = Depends(dependencies.get_db)
):
    db_author = crud.get_author(db, author_id)

    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found!")

    for i in range(len(author.books_id)):
        book_db = db.query(models.Book).filter(models.Book.id == author.books_id[i]).first()
        if book_db is None:
            raise HTTPException(status_code=404, detail=f"Book ID = {i+1} not found!")
        else:
            author.books.append(book_db)

    return crud.update_author(db=db, db_author=db_author, author=author)