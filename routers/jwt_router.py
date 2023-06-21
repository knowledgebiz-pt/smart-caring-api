from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import internal
import database
import core.schemes
from fastapi import APIRouter


router = APIRouter()
SECRET_KEY = "0ok25e928xbb6cc2556c817271b3a9563b93f0092f6f0f4caa6cf63b87e8d4e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_email(email: str, password: str):
    email = database.user_database.return_user_by_email(email)
    if not email:
        return False
    if not internal.jwt.verify_password(password, email.hashed_password):
        return False
    return email


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(internal.jwt.oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = core.schemes.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = database.user_database.return_user_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    email = authenticate_email(form_data.email, form_data.password)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": email.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
