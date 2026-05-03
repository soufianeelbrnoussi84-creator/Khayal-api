from fastapi import APIRouter,Depends
from db.database import get_session
from sqlmodel import Session,select
from schemas.product import ProductCreate,ProductResponse,ProductUpdate
from services.product import product_update,get_product,get_product_by_name,create_product,delete_product
from security.user import get_current_admin,get_current_user
from models.user import User
from models.product import Product


product_routes = APIRouter()

@product_routes.post("/create_product", response_model=ProductResponse)
def create(product:ProductCreate,
                   session: Session = Depends(get_session),
                   admin:User = Depends(get_current_admin)
                   ):
    return create_product(product,session)


@product_routes.get("/products",response_model=list[ProductResponse])
def all_product(
    session: Session= Depends(get_session)
):
    return get_product(session)
    

@product_routes.get("/name_product",response_model=list[ProductResponse])
def get_name_product(
    name: str,
    session:Session=Depends(get_session)
):
    return get_product_by_name(name,session)


@product_routes.put("/update/product",response_model=ProductResponse)
def updete_product(
    product_id:int,
    product_data: ProductUpdate,
    admin: User=Depends(get_current_admin),
    session: Session=Depends(get_session)
):
    return product_update(product_id,product_data,session)


@product_routes.delete("/delete_product")
def product_delete(
    product_id: int,
    admin: User=Depends(get_current_admin),
    session:Session=Depends(get_session)
):
    return delete_product(product_id,session)