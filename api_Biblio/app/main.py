from fastapi import FastAPI
from app.database import init_db
from app.routers import book as book_router

app = FastAPI(title="Bibliothèque API")

@app.on_event("startup")
async def start_db():
    await init_db()
    print("base de données fonctionnelle")

app.include_router(book_router.router)