from sqlalchemy.orm import Session
from app.models.sale import Sale, SaleProduct
from app.models.product import Product
from app.schemas.sale import SaleCreate, SaleUpdate, SaleProductCreate
from typing import List, Optional, Dict
from datetime import datetime

def _enrich_sale_product(db: Session, sale_product: SaleProduct) -> None:
    """Helper function to enrich a sale product with product details."""
    product = db.query(Product).filter(Product.id == sale_product.product_id).first()
    if product:
        sale_product.product_name = product.name
        sale_product.product_price = product.price
        sale_product.unit_price = product.price

def get_sale(db: Session, sale_id: int) -> Optional[Sale]:
    db_sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if not db_sale:
        return None
    # Enrich each sale product with product details
    for sale_product in db_sale.products:
        _enrich_sale_product(db, sale_product)
    return db_sale

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
    sales = query.offset(skip).limit(limit).all()
    # Enrich each sale product with product details
    for db_sale in sales:
        for sale_product in db_sale.products:
            _enrich_sale_product(db, sale_product)
    return sales

def _validate_stock(db: Session, products: List[SaleProductCreate]) -> Dict[int, Product]:
    """Validate stock availability for all products and return a mapping of product_id to Product."""
    product_map = {}
    for product_data in products:
        product = db.query(Product).filter(Product.id == product_data.product_id).first()
        if not product:
            raise ValueError(f"Product with ID {product_data.product_id} not found")
        
        if product.quantity < product_data.quantity:
            raise ValueError(
                f"Insufficient stock for product '{product.name}'. "
                f"Requested: {product_data.quantity}, Available: {product.quantity}"
            )
        
        product_map[product.id] = product
    return product_map

def create_sale(db: Session, sale: SaleCreate) -> Sale:
    # Validate stock for all products first
    product_map = _validate_stock(db, sale.products)
    
    # Create the sale
    db_sale = Sale()
    db.add(db_sale)
    db.flush()  # Get the sale ID

    total_price = 0.0
    
    # Add products to the sale
    for product_data in sale.products:
        product = product_map[product_data.product_id]
        
        # Calculate total for this product
        product_total = product.price * product_data.quantity
        
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
    
    # Enrich the response with product details
    for sale_product in db_sale.products:
        _enrich_sale_product(db, sale_product)
    
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
        # Validate stock for all products first
        product_map = _validate_stock(db, sale.products)
        
        # Remove existing sale products and restore stock
        for sale_product in db_sale.products:
            product = db.query(Product).filter(Product.id == sale_product.product_id).first()
            if product:
                product.quantity += sale_product.quantity
            db.delete(sale_product)

        # Add new sale products
        total_price = 0.0
        for product_data in sale.products:
            product = product_map[product_data.product_id]
            
            product_total = product.price * product_data.quantity
            
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
    
    # Enrich the response with product details
    for sale_product in db_sale.products:
        _enrich_sale_product(db, sale_product)
    
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