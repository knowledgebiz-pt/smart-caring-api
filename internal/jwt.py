import jwt
import datetime
from jose import JWTError

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
