from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models
from ..schemas import Blog


def get_all_blogs(db: Session):
    return db.query(models.BlogModel).all()


def create_blog(db: Session, request: Blog):
    new_blog = models.BlogModel(
        title=request.title,
        body=request.body,
        user_id=1  # Static user_id; you may want to make this dynamic later
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog_by_id(db: Session, id: int):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    return blog


def update_blog(db: Session, id: int, request: Blog):
    blog_query = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )

    blog_query.update(
        {
            "title": request.title,
            "body": request.body
        },
        synchronize_session=False
    )
    db.commit()
    return blog_query.first()


def delete_blog(db: Session, id: int):
    blog_query = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()
