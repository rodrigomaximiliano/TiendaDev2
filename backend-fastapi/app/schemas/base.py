from pydantic import BaseModel
from typing import Optional, Any

class ResponseModel(BaseModel):
    status: bool = True
    message: str
    data: Optional[Any] = None
