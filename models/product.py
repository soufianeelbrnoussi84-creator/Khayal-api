from sqlmodel import SQLModel,Field
from typing import Optional
from enum import Enum
from datetime import date,datetime


class ProductSize(str, Enum):
    S= "S"
    M= "M"
    L= "L"
    XL= "XL"
    XXL= "XXL"
    XXXL= "XXXL"
    XXXXL= "XXXXL"


class ProductCategory(str, Enum):
    jersey= "jersey"
    tshirt= "t-shirt"
    hoodie= "hoodie"
    shirt= "shirt"
    denim= "denim"
    cap= "cap"
    


class Product(SQLModel,table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    name: str
    description: str
    price: float
    discount: int = Field(default=0)
    size: ProductSize
    color: str
    quantity: int
    category: ProductCategory
    is_available: bool = Field(default=True)
    image_url: Optional[str] = Field(default=None)
    created_at: datetime=Field(default_factory=datetime.utcnow)