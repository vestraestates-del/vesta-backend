from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from models import InviteCode

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/verify')
def verify_invite(payload: dict, db=Depends(get_db)):
    code = payload.get('code','').strip()
    if not code:
        raise HTTPException(status_code=400, detail='code required')
    inv = db.query(InviteCode).filter(InviteCode.code==code).first()
    if not inv:
        raise HTTPException(status_code=404, detail='Invalid code')
    if inv.is_used:
        raise HTTPException(status_code=400, detail='Invite used')
    return {'valid': True, 'code': code}
