from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class LikesPost(BaseModel):
    """
    Likes Post
    """
    _id: str
    is_like: bool
    user_id: str
    news_id: str


class LikesCreateResponse(BaseModel):
    """
    Likes create response
    """
    msg: str
    data: object = {}


class LikesGetResponse(BaseModel):
    """
    Likes get response scheme
    """
    msg: str
    data: object = {}

class LikesDeleteResponse(BaseModel):
    """
        Likes delete response scheme
        """
    msg: str
    data: object = {}