from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date

class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    nationality: str = Field(..., min_length=2, max_length=2)
    biography: Optional[str] = None
    death_date: Optional[date] = None

    # Vérif : La date de décès doit être après la naissance
    @validator('death_date')
    def check_death_after_birth(cls, v, values):
        # On vérifie d'abord si birth_date est présent dans values
        if v and 'birth_date' in values:
            if v < values['birth_date']:
                raise ValueError("L'auteur n'est jamais née!")
        return v