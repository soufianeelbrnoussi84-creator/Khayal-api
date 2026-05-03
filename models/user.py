from sqlmodel import SQLModel,Field
from typing import Optional
from enum import Enum
from datetime import date,datetime


class UserRole(str, Enum):
    admin= "admin"
    user= "user"
   
class User(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field (unique=True, index=True)
    hashed_password: str
    date_of_birth: date
    role: UserRole = Field(default=UserRole.user) # "user" or "admin"
    is_active: bool= Field(default=True)
    created_at: datetime=Field(default_factory=datetime.utcnow)
    