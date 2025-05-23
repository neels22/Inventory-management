from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.core.database import get_db
from app.crud import sale as crud
from app.schemas.sale import Sale, SaleCreate, SaleUpdate
from app.auth.dependencies import get_current_user
from app.auth.models import User

router = APIRouter()

@router.get("/", response_model=List[Sale])
def read_sales(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    sales = crud.get_sales(
        db, 
        skip=skip, 
        limit=limit,
        start_date=start_date,
        end_date=end_date
    )
    return sales

@router.post("/", response_model=Sale)
def create_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return crud.create_sale(db=db, sale=sale)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{sale_id}", response_model=Sale)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = crud.get_sale(db, sale_id=sale_id)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@router.put("/{sale_id}", response_model=Sale)
def update_sale(
    sale_id: int,
    sale: SaleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        db_sale = crud.update_sale(db, sale_id=sale_id, sale=sale)
        if db_sale is None:
            raise HTTPException(status_code=404, detail="Sale not found")
        return db_sale
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{sale_id}")
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    success = crud.delete_sale(db, sale_id=sale_id)
    if not success:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"message": "Sale deleted successfully"} 