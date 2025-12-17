from fastapi import FastAPI

app = FastAPI(
    title="Gestion Bibliothèque",
)

@app.get("/")
def read_root():
    return {"message": "API fonctionnelle"}