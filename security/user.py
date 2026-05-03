from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlmodel import Session,select
from db.database import get_session
from models.user import User, UserRole


load_dotenv()

SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(h_password: str):
    return pwd_context.hash(h_password)

def verify_password(plain_password: str, hash_password: str):
    return pwd_context.verify(plain_password, hash_password)

def creat_access_token(data: dict):
    to_encode= data.copy()
    expire= datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(
    token: str= Depends(oauth2_scheme),
    session:Session = Depends(get_session)
    ):
    try:
        payload= jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email= payload.get("sub")
        
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user = session.exec(select(User) .where(User.email == email)).first()
        
        if user is None:
            raise HTTPException(status_code=401, detail="user not found")
        
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    

def get_current_admin(
    current_user: User = Depends(get_current_user)
    ):
    if current_user.role != UserRole.admin:
        raise HTTPException(
            status_code=403,
            detail="Admin privileges required"
        )
        
    return current_user