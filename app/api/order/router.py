from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database
from .models import Order, OrderCreate, OrderOut
from ..product.models import Product
from ..user.models import User
router = APIRouter()

get_db = database.get_db

@router.post("/orders/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):

    user = db.query(User).get(order.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    product = db.query(Product).get(order.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_order = Order(user_id=order.user_id,product_id=order.product_id,quantity=order.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
