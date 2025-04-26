



from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas, models

from ..hashing import Hash
router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)
@router.post("/")
def login(request:schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    

    return user
