from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from ..database import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


class ProductBase(BaseModel):
    name: str
    description: str


class ProductCreate(ProductBase):
    price: float
    quantity: int
    class Config:
        orm_mode = True