


from fastapi import FastAPI , status ,HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from .schemas import Blog , showBlog, User , showUser
from .database import engine
from . import models
from sqlalchemy.orm import Session
from .database import SessionLocal
from fastapi import Depends

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from .hashing import Hash



models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/blog",status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create_blog(request:Blog,db:Session = Depends(get_db)):
    new_blog = models.BlogModel(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT , tags=["Blogs"])
def delete_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)

    db.commit()
    return {"message": "Blog deleted successfully"}


@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED , response_model=showBlog, tags=["Blogs"])
def update_blog(id:int, request:Blog, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update(
        {
            "title": request.title,
            "body": request.body
        },
        synchronize_session=False
    )
    db.commit()
    return {"message": "Blog updated successfully"}






@app.get("/blog/",response_model=list[showBlog], status_code=status.HTTP_200_OK, tags=["Blogs"])
def get_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.BlogModel).all()
    return blogs

@app.get("/blog/{id}",status_code=status.HTTP_200_OK, response_model=showBlog, tags=["Blogs"])
def get_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()

    if not blog:
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    return blog




@app.post("/user",status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(request:User, db:Session = Depends(get_db)):
    # Hash the password
    hashed_password = Hash.encrypt(request.password)

    new_user = models.UserModel(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user",status_code=status.HTTP_200_OK, tags=["Users"])
def get_user(db:Session = Depends(get_db)):
    users = db.query(models.UserModel).all()
    return users

@app.get("/user/{id}",status_code=status.HTTP_200_OK, response_model=showUser, tags=["Users"])
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()

    if not user:
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user


@app.delete("/user/{id}",status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id)
    if not user.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.delete(synchronize_session=False)

    db.commit()
    return {"message": "User deleted successfully"}



@app.put("/user/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=showUser, tags=["Users"])
def update_user(id:int, request:User, db:Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id)
    if not user.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.update(
        {
            "name": request.name,
            "email": request.email,
            "password": request.password
        },
        synchronize_session=False
    )
    db.commit()
    return {"message": "User updated successfully"}
