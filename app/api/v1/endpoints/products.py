from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.crud import product as crud
from app.schemas.product import Product, ProductCreate, ProductUpdate
from app.auth.dependencies import get_current_user
from app.auth.models import User
from pydantic import BaseModel
from app.models.product import Product as ProductModel

class ProductSearch(BaseModel):
    name: str
    price: float
    quantity: int

    class Config:
        from_attributes = True

router = APIRouter()

@router.get("/", response_model=List[Product])
def read_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    brand: Optional[str] = None
):
    products = crud.get_products(db, skip=skip, limit=limit, category=category, brand=brand)
    return products

@router.post("/", response_model=Product)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_product = crud.get_product_by_barcode(db, barcode=product.barcode)
    if db_product:
        raise HTTPException(status_code=400, detail="Barcode already registered")
    return crud.create_product(db=db, product=product)

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_product = crud.update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    success = crud.delete_product(db, product_id=product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

@router.get("/low-stock/", response_model=List[Product])
def read_low_stock_products(db: Session = Depends(get_db)):
    return crud.get_low_stock_products(db)

@router.get("/search/", response_model=List[Product])
def search_products(
    q: Optional[str] = Query(None, description="Search query for product name, short name, barcode, or category"),
    db: Session = Depends(get_db)
):
    if not q:
        return []
    
    search_term = f"%{q}%"
    return db.query(ProductModel).filter(
        (ProductModel.name.ilike(search_term)) |
        (ProductModel.shortname.ilike(search_term)) |
        (ProductModel.barcode.ilike(search_term)) |
        (ProductModel.category.ilike(search_term))
    ).all() 