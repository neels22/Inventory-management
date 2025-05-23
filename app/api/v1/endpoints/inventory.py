from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.product import Product
from app.models.sale import Sale
from typing import Dict

router = APIRouter()

@router.get("/summary")
def get_inventory_summary(db: Session = Depends(get_db)):
    # Get total products count
    total_products = db.query(func.count(Product.id)).scalar()
    
    # Get total sales count
    total_sales = db.query(func.count(Sale.id)).scalar()
    
    # Get total sales value
    total_sales_value = db.query(func.sum(Sale.total_price)).scalar() or 0.0
    
    # Get out of stock products count
    out_of_stock = db.query(func.count(Product.id)).filter(Product.quantity == 0).scalar()
    
    # Get low stock products count
    low_stock = db.query(func.count(Product.id)).filter(Product.quantity <= Product.threshold).scalar()
    
    return {
        "total_products": total_products,
        "total_sales": total_sales,
        "total_sales_value": total_sales_value,
        "out_of_stock": out_of_stock,
        "low_stock": low_stock
    } 