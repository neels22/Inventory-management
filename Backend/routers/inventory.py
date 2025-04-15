

from fastapi import APIRouter, Depends, HTTPException
from schema import ProductBase, SaleBase
from typing import List, Optional, Dict

from constants.products import products as product_data
from constants.sales import sales as sales_data

router = APIRouter()

# @router.post("/inventory")

@router.get("/inventory")
async def get_inventory():
    """
    Get all products in the inventory.
    """
    # Logic to get all products in the inventory

    return {"message": "Inventory retrieved successfully", "inventory": product_data}