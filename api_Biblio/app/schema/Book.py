from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from app.schema.Enums import CategoryEnum, LanguageEnum

class BookCreate(BaseModel):
    title: str
    isbn: str = Field(..., pattern="^(978|979)[0-9]{10}$", description="ISBN-13 valide")
    publication_year: int = Field(..., ge=1450)
    author_id: int 
    available_copies: int = Field(..., ge=0)
    total_copies: int = Field(..., gt=0)
    description: Optional[str] = None
    
    category: CategoryEnum
    language: LanguageEnum = LanguageEnum.FRENCH
    
    pages: int = Field(..., gt=0)
    publisher: str


    @validator('publication_year')
    def check_year_not_future(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError(f"L'année {v} est dans le futur !")
        return v

    @validator('available_copies')
    def check_copies_logic(cls, v, values):
        if 'total_copies' in values and v > values['total_copies']:
            raise ValueError("Erreur de stock : Disponible > Total")
        return v
    
    @validator('title')
    def format_title(cls, v):
        return v.strip().title()