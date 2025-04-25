from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models
from ..schemas import User
from ..hashing import Hash


def create_user(db: Session, request: User):
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


def get_all_users(db: Session):
    return db.query(models.UserModel).all()


def get_user_by_id(db: Session, id: int):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


def delete_user(db: Session, id: int):
    user_query = db.query(models.UserModel).filter(models.UserModel.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user_query.delete(synchronize_session=False)
    db.commit()


def update_user(db: Session, id: int, request: User):
    user_query = db.query(models.UserModel).filter(models.UserModel.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    hashed_password = Hash.encrypt(request.password)
    user_query.update(
        {
            "name": request.name,
            "email": request.email,
            "password": hashed_password
        },
        synchronize_session=False
    )
    db.commit()
    return user_query.first()
