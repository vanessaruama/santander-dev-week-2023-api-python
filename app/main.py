from fastapi import FastAPI
from app.database import engine, Base
from app.routers.user_router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Santander Dev Week API - Python")

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "API running"}
