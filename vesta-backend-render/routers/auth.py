from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from models import User, InviteCode
from utils.security import hash_password, verify_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/register')
def register(data: dict, db=Depends(get_db)):
    email = data.get('email')
    password = data.get('password')
    invite_code = data.get('invite_code')
    if not email or not password or not invite_code:
        raise HTTPException(status_code=400, detail='email, password, invite_code required')
    inv = db.query(InviteCode).filter(InviteCode.code==invite_code).first()
    if not inv or inv.is_used:
        raise HTTPException(status_code=400, detail='Invalid or used invite')
    hashed = hash_password(password)
    user = User(email=email, name=data.get('name'), password_hash=hashed, invite_code_id=inv.id)
    db.add(user)
    inv.is_used = True
    db.add(inv)
    db.commit()
    db.refresh(user)
    token = create_access_token(user.id)
    return {'access_token': token, 'token_type': 'bearer'}

@router.post('/login')
def login(data: dict, db=Depends(get_db)):
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        raise HTTPException(status_code=400, detail='email and password required')
    user = db.query(User).filter(User.email==email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_access_token(user.id)
    return {'access_token': token, 'token_type': 'bearer'}
