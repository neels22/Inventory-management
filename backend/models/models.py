from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.dbconnection import Base
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.dbconnection import Base

# Association table
sale_product_association = Table(
    'sale_product_association',
    Base.metadata,
    Column('sale_id', Integer, ForeignKey('sales.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)


class SaleModel(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String,default=datetime.utcnow)
    total_price = Column(Float, default=0.0)
    total_products_sold = Column(Integer, default=0)
    date = Column(DateTime, default=datetime.utcnow)

    products = relationship(
        "ProductModel",
        secondary=sale_product_association,
        back_populates="sales"
    )


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="")
    nickname = Column(String, default="")
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    code = Column(String, default="")
    category = Column(String, default="")
    threshold = Column(Integer, default=0)
    location = Column(String, default="")
    supplier = Column(String, default="")
    description = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

