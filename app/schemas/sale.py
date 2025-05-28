from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SaleProductBase(BaseModel):
    product_id: int
    quantity: int

class SaleProductCreate(SaleProductBase):
    pass

class SaleProduct(SaleProductBase):
    id: int
    sale_id: int
    total: float
    product_name: str
    product_price: float
    unit_price: float

    class Config:
        from_attributes = True

class SaleBase(BaseModel):
    pass

class SaleCreate(SaleBase):
    products: List[SaleProductCreate]

class SaleUpdate(BaseModel):
    products: Optional[List[SaleProductCreate]] = None

class Sale(SaleBase):
    id: int
    date: datetime
    total_price: float
    products: List[SaleProduct]

    class Config:
        from_attributes = True 