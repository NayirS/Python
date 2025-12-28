from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from typing import Optional

class PretCreate(BaseModel):
    book_isbn: str 
    borrower_name: str
    
    borrower_email: EmailStr 
    
    card_number: str
    
    loan_date: datetime = Field(default_factory=datetime.now)
    
    expected_return_date: Optional[datetime] = None

    @validator('loan_date')
    def check_date_pas_nimp(cls, v):
        if v > datetime.now():
            raise ValueError("Ehoh tu peux pas emprunter dans le futur, on a pas de machine a voyager dans le temps")
        return v

    
    @validator('expected_return_date')
    def check_logique_temporel(cls, v, values):
        if v and 'loan_date' in values and v < values['loan_date']:
            raise ValueError("C'est mort, tu peux pas rendre le livre avant de l'avoir pris !")
        return v