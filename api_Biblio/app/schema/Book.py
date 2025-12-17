from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    title: str
    isbn: str = Field(..., pattern="^(978|979)[0-9]{10}$")
    publication_year: int = Field(..., ge=1450)
    author_id: int
    available_copies: int = Field(..., ge=0)
    total_copies: int = Field(..., gt=0)
    description: Optional[str] = None
    category: str
    pages: int
    publisher: str