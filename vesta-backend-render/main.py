import sys
import os

# 🔧 Render import hatasını çözmek için
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from database import engine, Base
from routers import users  # varsa başka router'larını da buraya ekle

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vestra Estates API",
    description="Backend for Vestra Estates platform",
    version="1.0.0"
)

# Router'ları ekle
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Vestra Backend is running 🚀"}
