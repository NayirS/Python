from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

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
    
    @validator('publication_year')
    def check_year_not_future(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError(f"L'année {v} est dans le futur, impossible !")
        return v

    @validator('available_copies')
    def check_copies_logic(cls, v, values):
        if 'total_copies' in values and v > values['total_copies']:
            raise ValueError("Il ne peut pas y avoir plus d'exemplaires disponibles que le total !")
        return v