from fastapi import FastAPI
from db.database import creat_db
from models.user import User
from routes.user import routes
from models.product import Product
from routes.product import product_routes
from models.order import Order
from routes.order import order_routes

app = FastAPI()

@app.on_event("startup")
def on_startup():
    creat_db()
    
@app.get("/")
def root():
    return{"message":"E-Market API running"}

app.include_router(routes)

app.include_router(product_routes)

app.include_router(order_routes)

