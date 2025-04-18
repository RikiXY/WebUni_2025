from fastapi import APIRouter
from models.book import Book
from data.books import books
from typing import Annotated
from fastapi import Path, HTTPException

router = APIRouter(prefix="/books")

@router.get("/")
def get_all_books() -> list[Book]:
    """Get all books."""
    return list(books.values())

@router.get("/{id}")
def get_book_by_id(
    id: Annotated[int, Path(description="The ID of the book to get")]
) -> Book:
    """Get a book by ID."""
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
    
