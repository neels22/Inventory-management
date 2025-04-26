from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas
from ..database import get_db
from ..repository import blog as blog_repository
from ..oauth import get_current_user  # ✅ Import get_current_user for authentication

router = APIRouter(
    prefix="/api/blog",
    tags=["Blogs"]
)


@router.get("/", response_model=List[schemas.showBlog], status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repository.get_all_blogs(db)


@router.post("/", response_model=schemas.showBlog, status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repository.create_blog(db, request)


@router.get("/{id}", response_model=schemas.showBlog, status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repository.get_blog_by_id(db, id)


@router.put("/{id}", response_model=schemas.showBlog, status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repository.update_blog(db, id, request)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog_repository.delete_blog(db, id)
    return {"message": "Blog deleted successfully"}
