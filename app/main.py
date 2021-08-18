from fastapi import FastAPI

from app.routers import authors, books

app = FastAPI()


app.include_router(authors.router)
app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "FastAPI Example"}
