from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .. import database
from pydantic import BaseModel


class Order(database.Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    # Relationship with User and Product models
    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")




class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    class Config:
        orm_mode = True



class OrderOut(OrderBase):
    id: int

    class Config:
        orm_mode = True
