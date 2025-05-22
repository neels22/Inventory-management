from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schema.sales import SaleCreateSchema, SaleUpdateSchema
from db.dbconnection import get_db
from models.models import ProductModel, SaleModel
from auth.dependencies import get_current_active_user
from models.user import User

router = APIRouter(
    prefix="/api/sales",
    tags=["Sales"]
)


@router.get("/", response_model=List[SaleCreateSchema], status_code=status.HTTP_200_OK)
def get_all_sales(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return db.query(SaleModel).all()


@router.post("/", response_model=SaleCreateSchema, status_code=status.HTTP_201_CREATED)
def create_sale(
    sale: SaleCreateSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    new_sale = SaleModel(
        customer_name=sale.customer_name,
        total_price=sale.total_price,
        total_products_sold=sale.total_products_sold,
        date=sale.date
    )
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale
