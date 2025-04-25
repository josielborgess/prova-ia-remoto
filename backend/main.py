from fastapi import FastAPI

app = FastAPI(title="Prova IA Generativa – Backend Starter", version="0.0.1")

@app.get("/health", tags=["Utils"])
def health_check():
    return {"status": "ok"}

@app.get("/", tags=["Utils"])
def hello():
    return {"message": "Hello, World!"}
