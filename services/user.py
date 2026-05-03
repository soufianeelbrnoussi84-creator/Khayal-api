from fastapi import HTTPException
from schemas.user import UserCreate,UserLogin
from models.user import User
from security.user import hashed_password,creat_access_token,verify_password
from sqlmodel import Session,select





def creat_user(account:UserCreate, session:Session):
    email = account.email
    check_email = session.exec(select(User).where(User.email == email)).first()
    
    if check_email:
        raise HTTPException(status_code=400, detail=" This email is already exists ")
    
    
    hashed_pw = hashed_password(account.password)
    db_account = User(
        first_name= account.first_name,
        last_name= account.last_name,
        email= account.email,
        date_of_birth= account.date_of_birth,
        hashed_password= hashed_pw
    )
    
    
    
    session.add(db_account)
    session.commit()
    session.refresh(db_account)
    return db_account


def login(account: UserLogin, session:Session):
    email= account.email
    password= account.password
    db_user= session.exec(select(User).where(User.email==email)).first()
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Email not found")
    
    
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Password not correct")
    
    creat_token= creat_access_token(
        data={"sub": account.email, "role": db_user.role}
    )
    
    return{
        "access_token":creat_token,
        "type":"bearer"
    }