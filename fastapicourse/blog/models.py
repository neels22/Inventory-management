

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

# this is db structure or table structure

class BlogModel(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

