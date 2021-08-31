from fastapi import FastAPI

from typing import Any

from app.routers import authors, books

app = FastAPI()


app.include_router(authors.router)
app.include_router(books.router)

@app.get("/")
async def root() -> Any:
    return {"message": "FastAPI Example"}
