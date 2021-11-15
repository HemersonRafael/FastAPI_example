import logging

from functools import lru_cache
from fastapi import FastAPI
from typing import Any

from app.config import Settings
from app.routers import authors, books


log = logging.getLogger("uvicorn")


app = FastAPI()


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings")
    return Settings()
    

app.include_router(authors.router)
app.include_router(books.router)


@app.get("/")
async def root() -> Any:
    return {"message": "FastAPI Example"}