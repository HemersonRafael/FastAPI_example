from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.tests.utils.utils import random_int_number, random_lower_string
from app.tests.utils.book import create_random_book


def test_create_book(client: TestClient, db: Session):
    data = {
        "title": random_lower_string(10), 
        "description": random_lower_string(10)
    }
    response = client.post("/books/", json=data)
    assert response.status_code == 200
    content = response.json() 
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content


def test_read_book_by_id(client: TestClient, db: Session):
    book = create_random_book(db=db)
    response = client.get(f"/books/{book.id}/")
    content = response.json()
    assert response.status_code == 200
    assert content["id"] == book.id


def test_read_book_by_name(client: TestClient, db: Session):
    book = create_random_book(db=db)
    response = client.get(f"/books/?title={book.title}&skip=0&limit=100")
    content = response.json()
    assert response.status_code == 200
    assert len(content) == 1


def test_update_book(client: TestClient, db: Session):
    book = create_random_book(db=db)
    data = {
        "title": random_lower_string(10),
        "description": random_lower_string(10)
    }
    response = client.put(f"/books/{book.id}", json=data)
    content = response.json() 
    assert response.status_code == 200
    assert  content["id"] == book.id
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]


def test_delete_book(client: TestClient, db: Session):
    book = create_random_book(db=db)
    response = client.delete(f"/books/{book.id}")
    content = response.json()
    assert response.status_code == 200
    assert content["id"] == book.id 


def test_read_books(client: TestClient, db: Session):
    stored_books = crud.book.get_multi(db=db)
    num = random_int_number()
    books = []
    for x in range(num):
        book = create_random_book(db=db)
        books.append(book)
    response = client.get("/books")
    content = response.json()
    assert response.status_code == 200
    assert  len(content)== len(stored_books) + len(books)