
from .schemas import TokenData,Token

from datetime import datetime, timedelta
from jose import JWTError, jwt


secret_key="your_secret_key"
algorithm="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30



def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt