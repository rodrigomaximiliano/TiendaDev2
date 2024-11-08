from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    username: str
    password: str

class UserCreateSchema(UserSchema):
    email: str  


class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class OrderSchema(BaseModel):
    total_price: float
    status: str
