from fastapi import APIRouter, Depends
from database import SessionLocal
from models import VaultCollection
from models import Property
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/request')
def request_vault(data: dict, db=Depends(get_db)):
    user_id = data.get('user_id')
    message = data.get('message','')
    vc = VaultCollection(user_id=user_id, property_ids='[]')
    db.add(vc)
    db.commit()
    db.refresh(vc)
    return {'status':'requested', 'id': vc.id}
