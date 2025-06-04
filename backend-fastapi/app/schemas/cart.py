from pydantic import BaseModel

class AddToCartSchema(BaseModel):
    product_id: str
    quantity: int

class CartItemResponse(BaseModel):
    id: str
    product_id: str
    quantity: int
    added_at: str

    class Config:
        from_attributes = True
