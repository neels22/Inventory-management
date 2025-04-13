
from fastapi import APIRouter, Depends, HTTPException

from schema import ProductBase, SaleBase
from typing import List, Optional, Dict

router = APIRouter()


product = {
    1: {
        "id": 1,
        "code": "P001",
        "name": "Product 1",
        "nickname": "Prod1",
        "quantity": 10,
        "threshold": 5,
        "description": "Description of Product 1",
        "price": 100.0,
        "category": "Category A",
        "brand": "Brand X",
        "location": "Location A"
    },
    # Add more products as needed
}

@router.post("/product")
async def create_product():
    """
    Create a new product.
    """
    # Logic to create a product

    return {"message": "Product created successfully"}


@router.get("/product/{product_id}", response_model=ProductBase)
async def get_product(product_id: int,query: Optional[str] = None):
    """
    Get a product by its ID.
    """
    # Logic to get a product by ID

    return {"message": "Product retrieved successfully", "product": product[product_id]}

