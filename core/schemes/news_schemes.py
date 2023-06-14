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
    user_id: str
    title: str = Field(
        ..., title="The description of the item", min_length = 5, max_length=120
    )
    content: dict
    content_type: str
    date: datetime


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
