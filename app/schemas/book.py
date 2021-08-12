from typing import Optional
from pydantic import BaseModel


# Shared properties
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None

# Properties to receive on book creation
class BookCreate(BookBase):  
    title: str
    description: str

# Properties to receive on book update
class BookUpdate(BookBase):
    pass

# Properties shared by models stored in DB
class BookInDBBase(BookBase):
    id: int
    title: str

    class Config:
        orm_mode = True

# Properties to return to client
class Book(BookInDBBase):
    pass


# Properties properties stored in DB
class BookInDB(BookInDBBase):
    pass