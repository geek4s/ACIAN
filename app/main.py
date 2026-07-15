# backend/app/main.py

from fastapi import FastAPI
from app.api import search
from app.api.ingestion import router as ingestion_router

from app.database.database import Base, engine
from app.models import *
from app.api.auth import router as auth_router
from app.api.competitors import router as competitor_router
from app.api.test import router as test_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ACIAN API",
    version="1.0.0"
)
app.include_router(ingestion_router)
app.include_router(auth_router)
app.include_router(competitor_router)
app.include_router(search.router)
app.include_router(test_router)
@app.get("/")
def root():
    return {"message": "Welcome to ACIAN API"}

@app.get("/health")
def health():
    return {"status": "running"}