from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.dbconnection import Base
from sqlalchemy import DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class SaleModel(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String,default=datetime.utcnow)
    total_price = Column(Float, default=0.0)
    total_products_sold = Column(Integer, default=0)
    date = Column(DateTime, default=datetime.utcnow)

    products = relationship("ProductModel", back_populates="sale")


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="",index=True)
    nickname = Column(String, default="",index=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    code = Column(String, default="",index=True)
    category = Column(String, default="")
    threshold = Column(Integer, default=0)
    location = Column(String, default="")
    supplier = Column(String, default="")
    description = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign key to link product to a sale
    sale_id = Column(Integer, ForeignKey('sales.id'))
    sale = relationship("SaleModel", back_populates="products")

