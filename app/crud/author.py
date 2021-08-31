from typing import List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorUpdate


class CRUDAuthor(CRUDBase[Author, AuthorCreate, AuthorUpdate]):
    def get_multi_by_name(
        self, db: Session, name: str,  skip: int = 0, limit: int = 100
    ) -> List[Author]:
        return (
            db.query(Author)
            .filter_by(name=name)
            .offset(skip)
            .limit(limit)
            .all()
        )


author = CRUDAuthor(Author)