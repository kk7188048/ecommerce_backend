from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    class Config:
        orm_mode = True

        
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
