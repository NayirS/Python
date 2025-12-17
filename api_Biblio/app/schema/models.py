from enum import Enum
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime, date

# --- Catégories ---
class Category(str, Enum):
    FICTION = "Fiction"
    SCIENCE = "Science"
    HISTOIRE = "Histoire"
    PHILOSOPHIE = "Philosophie"

# --- Auteur ---
class Author(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: date
    nationality: str = Field(..., min_length=2, max_length=3)
    biography: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Victor",
                "last_name": "Hugo",
                "birth_date": "1802-02-26",
                "nationality": "FR",
                "biography": "Ecrivain francais"
            }
        }

# --- Livre ---
class Book(BaseModel):
    id: int
    title: str
    isbn: str = Field(..., pattern="^(978|979)[0-9]{10}$")
    publication_year: int = Field(..., ge=1450)
    author_id: int
    available_copies: int = Field(..., ge=0)
    total_copies: int = Field(..., gt=0)
    category: Category

    @validator('publication_year')
    def check_year(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError("Annee invalide")
        return v

    @validator('available_copies')
    def check_copies(cls, v, values):
        if 'total_copies' in values and v > values['total_copies']:
            raise ValueError("Erreur stock")
        return v
    
    # j'ai utiliser l'ia pour un faux exemple 
    class Config:
        schema_extra = {
            "example": {
                "id": 101,
                "title": "Les Misérables",
                "isbn": "9782070409228",
                "publication_year": 1862,
                "author_id": 1,
                "available_copies": 4,
                "total_copies": 5,
                "category": "Fiction"
            }
        }

# --- Emprunt ---
class Loan(BaseModel):
    id: int
    book_id: int
    borrower_name: str
    borrower_email: EmailStr
    loan_date: datetime
    expected_return_date: date
    actual_return_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            #Fake client exemple 
            "example": {
                "id": 500,
                "book_id": 101,
                "borrower_name": "Jean Dupont",
                "borrower_email": "jean.dupont@email.com",
                "loan_date": "2023-10-25T14:30:00",
                "expected_return_date": "2023-11-08"
            }
        }