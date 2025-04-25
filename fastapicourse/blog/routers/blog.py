

from fastapi import APIRouter, Depends, HTTPException , status

from ..schemas import Blog, showBlog
from ..database import get_db
from typing import List
from .. import models

from sqlalchemy.orm import Session
from ..database import SessionLocal




router = APIRouter(
    prefix="/api",
    tags=["Blogs"]
)



@router.get("/blog/",response_model=list[showBlog], status_code=status.HTTP_200_OK)
def get_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.BlogModel).all()
    return blogs






@router.post("/blog",status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog,db:Session = Depends(get_db)):
    new_blog = models.BlogModel(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT )
def delete_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)

    db.commit()
    return {"message": "Blog deleted successfully"}


@router.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED , response_model=showBlog)
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



@router.get("/blog/{id}",status_code=status.HTTP_200_OK, response_model=showBlog)
def get_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()

    if not blog:
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    return blog

