from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class Content(BaseModel):
    type: str
    path: str


class Link(BaseModel):
    path: str
    show_preview: bool


class NewsPost(BaseModel):
    """
    News Post
    """
    _id: str
    user_id: str
    text: str = Field(
        ..., title="The description of the item", min_length = 5, max_length=120
    )
    content: Optional[Content] = Field(default=null, alias="content")
    link: Optional[Link] = Field(default=null, alias="content")
    likes: int
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



#content {type, path}
#link {path, show_preview}