from fastapi import HTTPException
from sqlmodel import Session,select
from models.order import Order,OrderStatus
from schemas.order import OrderCreate,OrderStatusUpdate,OrderResponse
from models.product import Product


def creat_order(order: OrderCreate, session: Session):
    product= session.exec(select(Product).where(Product.id==order.product_id)).first()
    if not product:
        
        raise HTTPException(status_code=404,detail="Product not found")
    
    if order.quantity >= product.quantity:
        raise HTTPException(status_code=404, detail="not enough stock")
    
    
    if order.city.lower() in ["rabat", "temara","salé"]:
        total= product.price * order.quantity
    else:
        total= (product.price * order.quantity) + 50
        
        
    product.quantity -= order.quantity
    
    db_order=Order(
        first_name=order.first_name,
        last_name=order.last_name,
        email=order.email,
        phone=order.phone,
        city=order.city,
        country=order.country,
        address=order.address,
        product_id=order.product_id,
        quantity=order.quantity,
        size=order.size,
        note=order.note,
        total_price=total
        )
    
    session.add(db_order)
    session.add(product)
    session.commit()
    session.refresh(db_order)
    return db_order

def get_orders(session:Session):
    order= session.exec(select(Order)).all()
    return order


def update_order_status(session:Session, order_data:OrderStatusUpdate, order_id: int):
    
    db_order= session.exec(select(Order).where(Order.id == order_id )).first()

    if not db_order:
        raise HTTPException(status_code=404,detail="order not found")
    
    product = session.exec(select(Product).where(Product.id == db_order.product_id)).first()
    
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    
    
    if order_data.quantity is not None:
        if order_data.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive")
        
        difference = order_data.quantity - db_order.quantity
        
        if difference > product.quantity:
            raise HTTPException(status_code=400, detail="Not enough stock")
        
        product.quantity -= difference
        db_order.quantity = order_data.quantity
        
        if db_order.city.lower() in ["rabat", "temara", "salé"]:
            db_order.total_price = product.price * order_data.quantity
        else:
            db_order.total_price = (product.price * order_data.quantity) + 50
    
    db_order.status = order_data.status
    
    
    session.add(db_order)
    session.add(product)
    session.commit()
    session.refresh(db_order)
    return db_order


def get_order_by_status(session:Session, order_status:OrderStatus):
    order= session.exec(select(Order).where(Order.status == order_status)).all()
    return order


def delete_order(order_id: int,session:Session):
    delete= session.exec(select(Order).where(Order.id == order_id)).first()
    if not delete:
        raise HTTPException(status_code=401, detail="order not found")
    
    session.delete(delete)
    session.commit()
    return {"status":"Order deleted"}
