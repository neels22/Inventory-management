

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base

from sqlalchemy.orm import relationship


# this is db structure or table structure

class BlogModel(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("UserModel", back_populates="blogs")



class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime)

    blogs = relationship("BlogModel", back_populates="creator")

