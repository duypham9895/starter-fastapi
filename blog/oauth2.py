from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from . import schemas, database, models, token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # user = get_user(fake_users_db, username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    # return user
    return token.verify_token(data, credentials_exception)
