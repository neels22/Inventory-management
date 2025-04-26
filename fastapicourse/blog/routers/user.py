from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas
from ..database import get_db
from ..repository import user as user_repository
from ..oauth import get_current_user  # ✅ Import authentication dependency

router = APIRouter(
    prefix="/api/user",
    tags=["Users"]
)

@router.post("/", response_model=schemas.showUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # Optional: you can allow open registration (no authentication here)
    return user_repository.create_user(db, request)

@router.get("/", response_model=List[schemas.showUser], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user_repository.get_all_users(db)

@router.get("/{id}", response_model=schemas.showUser, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user_repository.get_user_by_id(db, id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    user_repository.delete_user(db, id)
    return {"message": "User deleted successfully"}

@router.put("/{id}", response_model=schemas.showUser, status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user_repository.update_user(db, id, request)
