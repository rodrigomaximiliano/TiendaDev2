from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


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
    imagen: Optional[str] = None

class OrderSchema(BaseModel):
    total_price: float
    status: str

class AddToCartSchema(BaseModel):
    product_id: str
    quantity: int

class CartItemResponse(BaseModel):
    id: str  # Este será el ID de carrito convertido a string
    product_id: str  # Este será el ID del producto convertido a string
    quantity: int
    added_at: str  # La fecha de cuando fue añadido

    class Config:
        from_attributes = True