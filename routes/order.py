from fastapi import APIRouter,Depends
from db.database import get_session
from sqlmodel import Session,select
from schemas.order import OrderResponse,OrderStatusUpdate,OrderCreate
from services.order import creat_order, get_orders,get_order_by_status,update_order_status,delete_order
from security.user import get_current_admin,get_current_user
from models.order import Order
from models.user import User


order_routes= APIRouter()

@order_routes.post("/create_order",response_model=OrderResponse)
def order_create(order:OrderCreate,
                 session:Session=Depends(get_session),
                 ):
    return creat_order(order,session)

@order_routes.get("/orders",response_model=list[OrderResponse])
def all_orders(
    admin: User=Depends(get_current_admin),
    session: Session=Depends(get_session)
):
    return get_orders(session)

@order_routes.get("/get_order_by_status",response_model=list[OrderResponse])
def get_status_order(
    status:str,
    session:Session=Depends(get_session)
):
    return get_order_by_status(status,session)


@order_routes.put("/update",response_model=OrderResponse)
def update_order(
    order_id:int,
    order_data: OrderStatusUpdate,
    admin: User=Depends(get_current_admin),
    session: Session=Depends(get_session)
):
    return update_order_status(session,order_data,order_id)


@order_routes.delete("/delete")
def order_delete(
    order_id: int,
    admin: User=Depends(get_current_admin),
    session:Session=Depends(get_session)
):
    return delete_order(order_id,session)