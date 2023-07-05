from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class Content(BaseModel):
    type: str = Field(title="The type of file", description="The type of file", default="")
    path: str = Field(title="The path of file", description="The path of file", default="")


class NewsPost(BaseModel):
    """
    News Post
    """
    _id: str
    user_id: str
    text: str = Field(..., title="The description of the item")
    content: Content = Field(alias="content")
    link: Optional[str] = Field(default="", alias="link")
    favorites: Optional[list] = Field(default=[], alias="list favorites news")
    likes: Optional[list] = Field(default=[], alias="list likes news")


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