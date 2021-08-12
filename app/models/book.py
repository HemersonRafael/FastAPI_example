from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Book(Base):
    """
    Defines the book model
    """

    __tablename__ = "book"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    description = Column(String)

    def __repr__(self) -> str:
        return f"<Book {self.title}>"