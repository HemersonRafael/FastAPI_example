from fastapi.testclient import TestClient
from sqlalchemy.orm.session import Session

from app import crud
from app.crud import author
from app.tests.utils.author import create_random_author
from app.tests.utils.book import create_random_book
from app.tests.utils.utils import random_lower_string, random_int_number

def test_create_author(client: TestClient, db: Session):
    books_id = []
    num = random_int_number()
    for x in range(num):
        book = create_random_book(db=db)
        books_id.append(book.id)
    data = {
        "name": random_lower_string(10), 
        "books": [], 
        "books_id": books_id
    }
    response = client.post("/authors/", json=data)
    content = response.json()
    assert response.status_code == 200
    assert content["name"] == data["name"]
    assert len(content["books"]) == num
    assert "id" in content


def test_read_author_by_id(client: TestClient, db: Session):
    author = create_random_author(db=db)
    response = client.get(f"/authors/{author.id}/")
    content = response.json()
    assert response.status_code == 200
    assert content["id"] == author.id


def test_read_author_by_name(client: TestClient, db: Session):
    author = create_random_author(db=db)
    response = client.get(f"/authors/?name={author.name}&skip=0&limit=100")
    content = response.json()
    assert response.status_code == 200
    assert len(content) == 1


def test_update_author(client: TestClient, db: Session):
    author = create_random_author(db=db)
    data = {
        "name": random_lower_string(10)
    }
    response = client.put(f"/authors/{author.id}", json=data)
    content = response.json()
    assert response.status_code == 200
    assert content["id"] == author.id
    assert content["name"] == data["name"]
    assert len(content["books"]) == len(author.books)


def test_delete_author(client: TestClient, db: Session):
    author = create_random_author(db=db)
    response = client.delete(f"/authors/{author.id}")
    content = response.json() 
    assert response.status_code == 200
    assert content["id"] == author.id


def test_read_authors(client: TestClient, db: Session):
    stored_book = crud.author.get_multi(db=db)
    num = random_int_number()
    authors = []
    for x in range(num):
        author = create_random_author(db=db)
        authors.append(author)
    response = client.get("/authors")
    content = response.json()
    assert response.status_code == 200
    assert len(content) == len(stored_book) + len(authors)