from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def get_multi_by_title(
        self, db: Session, title: str,  skip: int = 0, limit: int = 100
    ) -> List[Book]:
        return (
            db.query(Book)
            .filter_by(title=title)
            .offset(skip)
            .limit(limit)
            .all()
        )


book = CRUDBook(Book)