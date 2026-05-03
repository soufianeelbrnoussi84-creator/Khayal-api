from fastapi import APIRouter,Depends
from db.database import get_session
from sqlmodel import Session
from schemas.user import UserCreate,UserResponse,UserLogin,TokenResponse
from services.user import creat_user, login


routes = APIRouter()

@routes.post("/register", response_model=UserResponse)
def register(account: UserCreate,
             session: Session = Depends(get_session)
             ):

    return creat_user(account,session)
    
@routes.post("/login", response_model= TokenResponse)
def user_login(account: UserLogin,
          session: Session= Depends(get_session)
          ):
    
    return login(account,session)



    
