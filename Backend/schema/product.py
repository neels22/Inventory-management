

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict


class ProductBase(BaseModel):
    id: int
    code: Optional[str]
    name: str
    nickname: str
    quantity: int
    threshold: int
    description: Optional[str]
    price: float
    category: Optional[str]
    brand: Optional[str]
    location: Optional[str]


class SaleBase(BaseModel):
    id: int
    quantity: int
    date: datetime
    total_price: float
    products: List[ProductBase]








