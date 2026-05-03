from sqlmodel import SQLModel,Field
from typing import Optional
from enum import Enum
from datetime import date,datetime

    
class OrderStatus(str,Enum):
    pending= "pending"
    confirmed= "confirmed"
    shipped= "shipped"
    delivered= "delivered"
    cancelled= "cancelled"

class Order(SQLModel, table=True):
    id: Optional[int]= Field(default=None,primary_key=True)
    first_name: str
    last_name: str
    email:  Optional[str]= Field(default=None)
    phone: str
    city: str
    address: Optional[str]= Field(default=None)
    product_id:int
    quantity: int
    total_price:float
    status: OrderStatus= Field(default=OrderStatus.pending)
    note: Optional[str]= Field(default=None)
    created_at: datetime=Field(default_factory=datetime.utcnow)
    country: str