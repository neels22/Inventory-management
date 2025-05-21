

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ...schema.product import Product
from ...schema.sales import Sale
from ...database import get_db
from ...models.models import ProductModel, SaleModel

router = APIRouter(
    prefix="/api/sales",
    tags=["Sales"]
)


@router.get("/", response_model=List[Sale], status_code=status.HTTP_200_OK)
def get_all_sales(db: Session = Depends(get_db)):
    return db.query(SaleModel).all()


@router.post("/", response_model=Sale, status_code=status.HTTP_201_CREATED)
def create_sale(sale: Sale, db: Session = Depends(get_db)):
    new_sale = SaleModel(customer_name=sale.customer_name, total_price=sale.total_price, total_products_sold=sale.total_products_sold, date=sale.date)
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale
