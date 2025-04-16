


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class Product(BaseModel):
    name: str
    price: float
    description: str = None