from app.routers import books
from typing import List, Optional
from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorUpdate


class CRUDAuthor(CRUDBase[Author, AuthorCreate, AuthorUpdate]):
    def create(self, db: Session, *, obj_in: AuthorCreate) -> Author:
      db_obj = self.model(name=obj_in.name, books=obj_in.books)  # type: ignore
      db.add(db_obj)
      db.commit()
      db.refresh(db_obj)
      return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Author,
        obj_in: AuthorUpdate
    ) -> Author:
        db_obj.name = obj_in.name
        db_obj.books = obj_in.books
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session,
        *, 
        name: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Author]:

        if name:
            return (
                db.query(Author)
                .filter_by(name=name)
                .offset(skip)
                .limit(limit)
                .all()
            )

        return db.query(Author).offset(skip).limit(limit).all()


author = CRUDAuthor(Author)