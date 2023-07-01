import os
import jwt
import datetime
from jose import JWTError

SECRET_KEY = os.getenv("SECRET_KEY_JWT")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)


# Function return the generated token (JWT)
def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": str(datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        date_one = datetime.datetime.strptime(decode_token["expires"], "%Y-%m-%d %H:%M:%S.%f")
        return decode_token["user_id"] if date_one >= datetime.datetime.utcnow() else None
    except JWTError:
        return None
