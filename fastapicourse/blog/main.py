


from fastapi import FastAPI , status ,HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from .schemas import Blog , showBlog, User , showUser
from .database import engine
from . import models
from sqlalchemy.orm import Session
from .database import SessionLocal
from fastapi import Depends
from .database import get_db

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from .hashing import Hash
from .routers import blog, user


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)



