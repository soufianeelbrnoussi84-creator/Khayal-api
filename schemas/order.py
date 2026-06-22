from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from models.order import OrderStatus
from models.product import ProductSize


class OrderCreate(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str]=None
    phone: str
    city: str
    country: str
    address: str
    product_id: int
    quantity: int
    size: ProductSize
    note: Optional[str]=None
    

class OrderResponse(BaseModel):
    model_config={
        "from_attributes":True
    }
    id: int
    first_name: str
    last_name: str
    email: Optional[str]=None
    phone: str
    city: str
    country: str
    address: str
    product_id: int
    quantity: int
    size: ProductSize
    total_price: float
    created_at: datetime
    status: OrderStatus
    note: Optional[str]=None
    
class OrderStatusUpdate(BaseModel):
    status: OrderStatus
    quantity: Optional[int] = None
    price: Optional[float] = None