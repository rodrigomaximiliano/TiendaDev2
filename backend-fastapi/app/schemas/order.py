from pydantic import BaseModel

class OrderSchema(BaseModel):
    total_price: float
    status: str
