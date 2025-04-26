from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..hashing import Hash
from ..JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post("/")
def login(request:OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=403, detail="Invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "name": user.name,
            "email": user.email
        }
    }
