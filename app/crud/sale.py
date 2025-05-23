from sqlalchemy.orm import Session
from app.models.sale import Sale, SaleProduct
from app.models.product import Product
from app.schemas.sale import SaleCreate, SaleUpdate, SaleProductCreate
from typing import List, Optional
from datetime import datetime

def get_sale(db: Session, sale_id: int) -> Optional[Sale]:
    return db.query(Sale).filter(Sale.id == sale_id).first()

def get_sales(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> List[Sale]:
    query = db.query(Sale)
    if start_date:
        query = query.filter(Sale.date >= start_date)
    if end_date:
        query = query.filter(Sale.date <= end_date)
    return query.offset(skip).limit(limit).all()

def create_sale(db: Session, sale: SaleCreate) -> Sale:
    # Create the sale
    db_sale = Sale()
    db.add(db_sale)
    db.flush()  # Get the sale ID

    total_price = 0.0
    
    # Add products to the sale
    for product_data in sale.products:
        product = db.query(Product).filter(Product.id == product_data.product_id).first()
        if not product:
            raise ValueError(f"Product with ID {product_data.product_id} not found")
        
        if product.quantity < product_data.quantity:
            raise ValueError(f"Insufficient stock for product {product.name}")
        
        # Calculate total for this product
        product_total = product.price * product_data.quantity * (1 - product.discount)
        
        # Create sale product entry
        db_sale_product = SaleProduct(
            sale_id=db_sale.id,
            product_id=product.id,
            quantity=product_data.quantity,
            total=product_total
        )
        db.add(db_sale_product)
        
        # Update product quantity
        product.quantity -= product_data.quantity
        
        total_price += product_total

    # Update sale total
    db_sale.total_price = total_price
    
    db.commit()
    db.refresh(db_sale)
    return db_sale

def update_sale(
    db: Session, 
    sale_id: int, 
    sale: SaleUpdate
) -> Optional[Sale]:
    db_sale = get_sale(db, sale_id)
    if not db_sale:
        return None

    if sale.products:
        # Remove existing sale products
        for sale_product in db_sale.products:
            product = db.query(Product).filter(Product.id == sale_product.product_id).first()
            if product:
                product.quantity += sale_product.quantity
            db.delete(sale_product)

        # Add new sale products
        total_price = 0.0
        for product_data in sale.products:
            product = db.query(Product).filter(Product.id == product_data.product_id).first()
            if not product:
                raise ValueError(f"Product with ID {product_data.product_id} not found")
            
            if product.quantity < product_data.quantity:
                raise ValueError(f"Insufficient stock for product {product.name}")
            
            product_total = product.price * product_data.quantity * (1 - product.discount)
            
            db_sale_product = SaleProduct(
                sale_id=db_sale.id,
                product_id=product.id,
                quantity=product_data.quantity,
                total=product_total
            )
            db.add(db_sale_product)
            
            product.quantity -= product_data.quantity
            total_price += product_total

        db_sale.total_price = total_price

    db.commit()
    db.refresh(db_sale)
    return db_sale

def delete_sale(db: Session, sale_id: int) -> bool:
    db_sale = get_sale(db, sale_id)
    if db_sale:
        # Return products to inventory
        for sale_product in db_sale.products:
            product = db.query(Product).filter(Product.id == sale_product.product_id).first()
            if product:
                product.quantity += sale_product.quantity
        
        db.delete(db_sale)
        db.commit()
        return True
    return False 