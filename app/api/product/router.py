from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import ProductCreate, Product
from .. import database
from typing import List
router = APIRouter(
    prefix="/products",
    tags=['Products']
)

def get_all_products(db:Session):
    return db.query(Product).all()

def get_product(db:Session, productId:int):
    return db.query(Product).filter(Product.id == productId).first()

def create_product(db:Session, product:ProductCreate):
    new_product = Product(name=product.name,description=product.description,price = product.price, quantity = product.quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=List[Product])
def read_products(db: Session = Depends(database.get_db)):
    return get_all_products(db)

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(database.get_db)):
    product = get_product(db, product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/", response_model=Product)
def create_products(product: ProductCreate, db: Session = Depends(database.get_db)):
    return create_product(db, product)