
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"
    reputation: Optional[int] = 0

class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    seller: str