



from fastapi import APIRouter, Depends, HTTPException , status

from ..schemas import Blog, showBlog, User , showUser
from ..hashing import Hash
from ..database import engine
from ..database import get_db
from typing import List
from .. import models

from sqlalchemy.orm import Session
from ..database import SessionLocal



router = APIRouter(
    prefix="/api",
    tags=["Users"]
)



@router.post("/user",status_code=status.HTTP_201_CREATED)
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


@router.get("/user",status_code=status.HTTP_200_OK)
def get_user(db:Session = Depends(get_db)):
    users = db.query(models.UserModel).all()
    return users

@router.get("/user/{id}",status_code=status.HTTP_200_OK, response_model=showUser)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()

    if not user:
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user


@router.delete("/user/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id)
    if not user.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.delete(synchronize_session=False)

    db.commit()
    return {"message": "User deleted successfully"}



@router.put("/user/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=showUser)
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
