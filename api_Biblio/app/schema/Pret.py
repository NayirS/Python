from pydantic import BaseModel, EmailStr, validator
from datetime import date

class PretCreate(BaseModel):
    book_id: int
    borrower_email: EmailStr
    loan_date: date
    expected_return_date: date

    # La date de retour doit être après ou égales à la date d'emprunt
    @validator('expected_return_date')
    def check_dates(cls, v, values):
        if 'pret_date' in values and v < values['pret_date']:
            raise ValueError("La date de retour ne peut pas être antérieure à la date d'emprunt.")
        return v