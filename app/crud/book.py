from typing import List, Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def get_multi(
        self, db: Session,
        title: Optional[str] = None,
        *,
        skip: int = 0,
        limit: int = 100
    ) -> List[Book]:
        if title:
            return (
                db.query(Book)
                .filter_by(title=title)
                .offset(skip)
                .limit(limit)
                .all()
            )

        return db.query(Book).offset(skip).limit(limit).all()


book = CRUDBook(Book)