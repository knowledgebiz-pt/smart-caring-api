from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class NewsPost(BaseModel):
    """
    News Post
    """
    _id: str
    title: str = Field(
        ..., title="The description of the item", min_length = 5, max_length=120
    )
    content: str = Field(
        ..., title="The description of the item", min_length = 50, max_length=3000
    )
    user_id: str
    picture: Optional[str] = Field(default=null, alias="picture")
    video: Optional[str] = Field(default=null, alias="video")


class NewsCreateResponse(BaseModel):
    """
    News create response
    """
    msg: str
    data: object = {}


class NewsGetResponse(BaseModel):
    """
    News get response scheme
    """
    msg: str
    data: object = {}

class NewsDeleteResponse(BaseModel):
    """
        News delete response scheme
        """
    msg: str
    data: object = {}