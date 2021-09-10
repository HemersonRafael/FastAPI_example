from starlette import responses
from tests  import client

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI Example"}

def test_create_book():
    response = client.post(
        "/books/",
        json={"title": "string", "description": "string"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "string",
        "description": "string",
        "id":1
    }

def test_create_author():
    response = client.post(
        "/authors/",
        json={"name": "string", "books": [], "books_id": [1]}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "string",
        "books": [
        {
            "title": "string",
            "description": "string",
            "id": 1
        }
        ],
        "id": 1
    }

def test_read_book_by_id():
    response = client.get("/books/1/")
    assert response.status_code == 200
    assert response.json() == {
        "title": "string",
        "description": "string",
        "id":1
    }

def test_read_author_by_id():
    response = client.get("/authors/1/")
    assert response.status_code == 200
    assert response.json() == {
        "name": "string",
        "books": [
            {
                "title": "string",
                "description": "string",
                "id": 1
            }
        ],
        "id": 1
    }

def test_read_book_by_name():
    response = client.get("/books/?name=string&skip=0&limit=100")
    assert response.status_code == 200
    assert response.json() != []

def test_read_author_by_name():
    response = client.get("/authors/?name=string&skip=0&limit=100")
    assert response.status_code == 200
    assert response.json() != []

def test_update_book():
    response = client.put(
        "/books/1",
        json={"title": "updated", "description": "string"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "updated",
        "description":"string",
        "id":1
    }

def test_update_author():
    response = client.put(
        "/authors/1", 
        json={"name": "updated", "books": [], "books_id": [1]}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "updated",
        "books": [
            {
                "title": "updated",
                "description": "string",
                "id": 1
            }
        ],
        "id": 1
    }

def test_delete_author():
    response = client.delete("/authors/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "updated",
        "books": [
            {
                "title": "updated",
                "description": "string",
                "id": 1
            }
        ],
        "id": 1
    }

def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {
                "title": "updated",
                "description": "string",
                "id": 1
    }

def test_read_authors_to_see_if_it_returned_an_empty_list():
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json() == []

def test_read_books_to_see_if_it_returned_an_empty_list():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []
