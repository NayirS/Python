from fastapi import FastAPI

app = FastAPI(
    title="Gestion Bibliothèque",
    description="API gestion ouvrages et emprunts",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "API fonctionnelle"}