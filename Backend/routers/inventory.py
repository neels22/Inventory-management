

from fastapi import APIRouter, Depends, HTTPException
from schema import ProductBase, SaleBase
from typing import List, Optional, Dict

router = APIRouter()

# @router.post("/inventory")

@router.get("/inventory")
async def get_inventory():
    """
    Get all products in the inventory.
    """
    # Logic to get all products in the inventory
    return {"message": "Inventory retrieved successfully", "inventory": []}