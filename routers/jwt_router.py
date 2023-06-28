import json
import time
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import APIRouter

router = APIRouter()
SECRET_KEY = "0ok25e928xbb6cc2556c817271b3a9563b93f0092f6f0f4caa6cf63b87e8d4e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Function return the generated token (JWT)
def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decode_token["user_id"] if decode_token["expires"] >= time.time() else None
    except JWTError:
        return None
