from jose import JWTError,jwt
from datetime import datetime,time,timedelta
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from .database_orm import get_db
from . import models



oath_scheme= OAuth2PasswordBearer(tokenUrl='user_login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode=data.copy()
    expire= datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token :str,credential_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id: str= payload.get('user_id')
        if id is None:
            raise credential_exception
        return id
    except JWTError:
        raise credential_exception


def get_current_user(token : str = Depends(oath_scheme),db=Depends(get_db)):
    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    id= verify_token(token,credential_exception)
    if not id :
        return credential_exception
    user=db.query(models.user_information).filter(models.user_information.id==id).first()
    if not user:
        return credential_exception
    return user
    
    