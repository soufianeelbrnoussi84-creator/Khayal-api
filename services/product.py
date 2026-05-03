from fastapi import HTTPException
from models.product import Product
from schemas.product import ProductCreate,ProductResponse,ProductUpdate
from sqlmodel import select,Session



def create_product(product:ProductCreate, session:Session):
    db_product=Product(
        name= product.name,
        description= product.description,
        price= product.price,
        size= product.size,
        color= product.color,
        quantity= product.quantity,
        category= product.category,
        image_url= product.image_url,
        discount= product.discount 
    )
    
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product  


def get_product(session:Session):
    products= session.exec(select(Product)).all()
    return products


def get_product_by_name(name: str, session: Session):
    product= session.exec(select(Product).where(Product.name == name)).all()
    return product


def product_update(product_id: int, product_data: ProductUpdate, session: Session):
    update= session.exec(select(Product).where(Product.id == product_id)).first()
    if not update:
        raise HTTPException(status_code=404, detail= "Product not found" )
    
    products=product_data.model_dump(exclude_unset=True)
    
    for key, value in products.items():
        setattr(update, key, value)
    
    session.add(update)
    session.commit()
    session.refresh(update)
    return update  
        

def delete_product(product_id: int, session: Session):
    delete= session.exec(select(Product).where(Product.id == product_id)).first()
    if not delete:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(delete)
    session.commit()
    return {"status": "Product deleted"}    