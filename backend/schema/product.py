from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreateSchema(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    nickname: Optional[str] = None
    quantity: Optional[int] = None
    code: Optional[str] = None
    category: Optional[str] = None
    threshold: Optional[int] = None
    location: Optional[str] = None
    supplier: Optional[str] = None


    class Config:
        from_attributes = True


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    nickname: Optional[str] = None
    quantity: Optional[int] = None
    code: Optional[str] = None
    category: Optional[str] = None
    threshold: Optional[int] = None
    location: Optional[str] = None
    supplier: Optional[str] = None

    class Config:
        from_attributes = True
