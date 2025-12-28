from enum import Enum

class CategoryEnum(str, Enum):
    FICTION = "Fiction"
    SCIENCE_FICTION = "Science-Fiction"
    HISTORY = "Histoire"
    SCIENCE = "Science"
    BIOGRAPHY = "Biographie"
    PHILOSOPHY = "Philosophie"
    MYSTERY = "Policier"
    FANTASY = "Fantaisie"
    OTHER = "Autre"

class LanguageEnum(str, Enum):
    FRENCH = "Français"
    ENGLISH = "Anglais"
    SPANISH = "Espagnol"
    GERMAN = "Allemand"
    OTHER = "Autre"