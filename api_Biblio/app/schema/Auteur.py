from pydantic import BaseModel, Field, validator, HttpUrl
from typing import Optional
from datetime import date

class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    nationality: str  
    biography: Optional[str] = None
    death_date: Optional[date] = None
    website: Optional[str] = None

    #La date de naissance ne peut pas être dans le futur
    @validator('birth_date')
    def check_birth_date(cls, v):
        if v > date.today():
            raise ValueError("Un auteur ne peut pas naître dans le futur !")
        return v

    #  Si date de décès, elle doit être après la naissance
    @validator('death_date')
    def check_death_date(cls, v, values):
        if v and 'birth_date' in values and v < values['birth_date']:
            raise ValueError("La date de décès doit être postérieure à la naissance.")
        return v