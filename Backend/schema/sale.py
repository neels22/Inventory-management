


from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict



class SoldProduct(BaseModel):
    product_id: int
    quantity: int

class SaleBase(BaseModel):
    id: int
    quantity: int
    date: datetime
    total_price: float
    products: List[SoldProduct]

