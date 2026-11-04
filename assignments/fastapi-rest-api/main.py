from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


class Book(BookCreate):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", year=1937)
}
next_book_id = 2

# Add the GET, POST, PUT, and DELETE routes described in README.md.
