from typing import List
from pydantic import BaseModel
from app.schemas.book import Book


# Shared properties
class AuthorBase(BaseModel):
    name: str
    books: List[Book] = []


# Properties to receive on author creation
class AuthorCreate(AuthorBase):  
    name: str
    books_id: List[int] = []

# Properties to receive on author update
class AuthorUpdate(AuthorBase):
    pass

# Properties shared by models stored in DB
class AuthorInDBBase(AuthorBase):
    id: int
    name: str
    books: List[Book] = []

    class Config:
        orm_mode = True

# Properties to return to client
class Author(AuthorInDBBase):
    pass


# Properties properties stored in DB
class AuthorInDB(AuthorInDBBase):
    pass


