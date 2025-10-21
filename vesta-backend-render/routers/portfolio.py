from fastapi import APIRouter, Depends
from database import SessionLocal
from models import Property
from typing import List
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PropertyOut(BaseModel):
    id: int
    title: str
    location: str | None
    description: str | None
    is_vault: bool
    image_url: str | None

    class Config:
        orm_mode = True

@router.get('/', response_model=List[PropertyOut])
def list_props(db=Depends(get_db)):
    props = db.query(Property).all()
    return props
