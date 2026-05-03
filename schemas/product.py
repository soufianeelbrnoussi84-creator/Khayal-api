from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from models.product import Product,ProductCategory,ProductSize


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    color: str
    size: ProductSize
    discount: int
    quantity: int
    category: ProductCategory
    image_url:str


class ProductUpdate(BaseModel):
    name: Optional[str]=None
    description: Optional[str]=None
    price: Optional[float] = None
    quantity: Optional[int]= None
    discount: Optional[int]= None
    color:Optional[str]=None
    size:Optional[ProductSize]=None
    is_available:Optional[bool]=True
    image_url:Optional[str]=None

    
class ProductResponse(BaseModel):
    model_config = {
        "from_attributes": True  # ✅ v2 replacement for orm_mode
    }
    id: int
    name: str
    description: Optional[str] = None
    price: float
    color: str
    size: ProductSize
    discount: int
    quantity: int
    category: ProductCategory
    is_available: bool 
    image_url:Optional[str]=None
    created_at: datetime
    




