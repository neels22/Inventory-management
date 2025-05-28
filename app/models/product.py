from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    shortname = Column(String, unique=True, index=True)
    barcode = Column(String, unique=True, index=True)
    quantity = Column(Integer, default=0)
    price = Column(Float)
    threshold = Column(Integer, default=10)
    location = Column(String)
    category = Column(String, index=True)
    brand = Column(String, index=True)

    # Relationships
    sale_products = relationship("SaleProduct", back_populates="product") 