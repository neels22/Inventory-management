from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Sale(BaseModel):
    id: Optional[int] = None
    customer_name: str
    total_price: float
    total_products_sold: int
    date: datetime

    class Config:
        from_attributes = True
