from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    total_price = Column(Float, default=0.0)

    # Relationships
    products = relationship("SaleProduct", back_populates="sale")

class SaleProduct(Base):
    __tablename__ = "sale_products"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total = Column(Float)

    # Relationships
    sale = relationship("Sale", back_populates="products")
    product = relationship("Product", back_populates="sale_products") 