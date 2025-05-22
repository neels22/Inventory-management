from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SaleCreateSchema(BaseModel):
    customer_name: str
    total_price: float
    total_products_sold: int
    date: datetime
    product_ids: List[int]  # List of product IDs in the sale

    class Config:
        from_attributes = True

        
class SaleUpdateSchema(BaseModel):
    customer_name: Optional[str] = None
    total_price: Optional[float] = None
    total_products_sold: Optional[int] = None
    date: Optional[datetime] = None
    product_ids: Optional[List[int]] = None  # Optional update to product list

    class Config:
        from_attributes = True
