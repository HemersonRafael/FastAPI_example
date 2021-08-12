from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.database import Base


association_author_book_table = Table('association_author_book', Base.metadata,
    Column('author_id', ForeignKey('author.id'), primary_key=True),
    Column('book_id', ForeignKey('book.id'), primary_key=True)
)


class Author(Base):
    """
    Defines the author model
    """

    __tablename__ = "author"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    books = relationship(
        "Book",
        secondary=association_author_book_table,
        backref="authors")

    def __repr__(self) -> str:
        return f"<Author {self.name}>"