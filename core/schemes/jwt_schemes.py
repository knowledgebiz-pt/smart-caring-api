from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str
