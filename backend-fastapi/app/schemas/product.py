from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    imagen: Optional[str] = None
