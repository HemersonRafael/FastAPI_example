from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.database import SessionLocal, Engine
from app.config import Settings
from app.database import Base
from app.main import app, get_settings


def get_settings_override() -> Settings:
    return Settings(
        SQLALCHEMY_DATABASE_URI="postgresql://fastapi:fastapi@localhost:5432/fastapi_test"
    )
    
    
app.dependency_overrides[get_settings] = get_settings_override


@pytest.fixture(scope="session")
def db() -> Generator:
    db = SessionLocal()
    Base.metadata.create_all(bind=Engine)
    try:
        yield db
    finally:
        db.close()
    Base.metadata.drop_all(bind=Engine)


@pytest.fixture(scope="module")
def client() -> Generator:    
    with TestClient(app) as c:
        yield c