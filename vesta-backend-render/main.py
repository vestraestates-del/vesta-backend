import sys
import os

# 🔧 Render dizin sorununu çözmek için (src/vesta-backend-render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from fastapi import FastAPI
from database import engine, Base
from vesta_backend_render.routers import users  # varsa diğer router'larını da buraya ekle

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
