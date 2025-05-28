from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    shortname: str
    barcode: str
    quantity: int
    price: float
    threshold: Optional[int] = 10
    location: str
    category: str
    brand: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    shortname: Optional[str] = None
    barcode: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    threshold: Optional[int] = None
    location: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True 