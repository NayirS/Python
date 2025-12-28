from typing import Optional
from beanie import Document
from pydantic import Field

class Book(Document):
    title: str
    isbn: str = Field(index=True)
    publication_year: int
    author_id: int 
    available_copies: int
    total_copies: int
    description: Optional[str] = None
    
    category: str 
    language: str 
    
    pages: int
    publisher: str
    is_active: bool = True

    class Settings:
        name = "books"