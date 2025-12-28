from fastapi import APIRouter, HTTPException
from typing import List

from app.models.book import Book as BookModel

from app.schema.Book import BookCreate

router = APIRouter(tags=["Books"])

@router.post("/books/", response_model=BookModel, status_code=201)
async def create_book(book: BookCreate):
    
    existing = await BookModel.find_one(BookModel.isbn == book.isbn).first_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Cet ISBN existe déjà.")
    new_book = BookModel(**book.dict())
    
    await new_book.insert()
    
    return new_book

@router.get("/books/", response_model=List[BookModel])
async def get_books():
    return await BookModel.find_all().to_list()