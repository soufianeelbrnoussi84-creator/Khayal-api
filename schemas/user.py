from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from models.user import UserRole


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    password: str
    

class UserLogin(BaseModel):
    email: str
    password:str


class UserResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    email: str
    first_name: str
    last_name: str
    role: UserRole
    is_active: bool
    date_of_birth: date
    created_at: datetime
    
class TokenResponse(BaseModel):
    access_token: str
    type: str
    