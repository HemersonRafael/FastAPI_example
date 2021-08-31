from typing import Any, List, Optional

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, dependencies


router = APIRouter()


@router.post("/authors/", response_model=schemas.Author)
async def create_author(
    author_in: schemas.AuthorCreate, db: Session = Depends(dependencies.get_db)
)-> Any:
    if author_in.books_id:
        for i in range(len(author_in.books_id)):
            book_db = crud.book.get(db=db, id=author_in.books_id[i])

            if not book_db:
                raise HTTPException(
                    status_code=404,
                    detail=f"Book ID = {author_in.books_id[i]} not found!"
                )
            else:
                author_in.books.append(book_db)
    
    author_in = author_in.dict(exclude={"books_id"})

    return crud.author.create(db=db, obj_in=author_in)


@router.get("/authors/{author_id}", response_model=schemas.Author)
async def read_author(
    author_id: int, db: Session = Depends(dependencies.get_db)
)-> Any:
    db_author = crud.author.get(db=db, id=author_id)

    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found!")

    return db_author


@router.get("/authors/", response_model=List[schemas.Author])
async def read_authors(
   name: Optional[str] = None,
   skip: int = 0,
   limit: int = 100,
   db: Session = Depends(dependencies.get_db)
)-> Any:
    if name:
        return (
            crud.author.get_multi_by_name(
                db=db, 
                name=name, 
                skip=skip, 
                limit=limit
            )
        )
    
    return crud.author.get_multi(db=db, skip=skip, limit=limit)


@router.delete("/authors/{author_id}", response_model=schemas.Author)
async def delete_author(
    author_id: int, db: Session = Depends(dependencies.get_db)
)-> Any:
    db_author = crud.author.get(db=db, id=author_id)

    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found!")
    
    return crud.author.remove(db=db, id=author_id)


@router.put("/authors/{author_id}", response_model=schemas.Author)
async def update_author(
    author_in: schemas.AuthorCreate,
    author_id: int,
    db: Session = Depends(dependencies.get_db)
) -> Any:
    db_author = crud.author.get(db=db, id=author_id)

    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found!")

    for i in range(len(author_in.books_id)):
        book_db = crud.book.get(db=db, id=author_in.books_id[i])
        if not book_db:
            raise HTTPException(
                status_code=404,
                detail=f"Book ID = {author_in.books_id[i]} not found!"
            )
        else:
            author_in.books.append(book_db)

    return crud.author.update(db=db, db_obj=db_author, obj_in=author_in)