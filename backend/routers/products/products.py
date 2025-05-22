from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schema.product import ProductCreateSchema, ProductUpdateSchema
from schema.auth_schema import UserResponse
from db.dbconnection import get_db
from models.models import ProductModel, SaleModel, User
from auth.dependencies import get_current_active_user


router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


@router.get("/", response_model=List[ProductCreateSchema], status_code=status.HTTP_200_OK)
def get_all_products(
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    return db.query(ProductModel).all()

@router.get("/{product_id}", response_model=ProductCreateSchema, status_code=status.HTTP_200_OK)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.post("/", response_model=ProductCreateSchema, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    new_product = ProductModel(name=product.name, price=product.price, description=product.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

