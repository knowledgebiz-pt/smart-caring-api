from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class CommentPost(BaseModel):
    """
    Comment on Post
    """
    _id: str
    news_id: str
    comment_reply_id: Optional[str]
    user_id: str
    text: str
    link: str
    likes: Optional[list] = Field(default=[], alias="list likes comment")


class CommentCreateResponse(BaseModel):
    """
    Comment create response
    """
    msg: str
    data: object = {}


class CommentGetResponse(BaseModel):
    """
    Comments get response scheme
    """
    msg: str
    data: object = {}

class CommentDeleteResponse(BaseModel):
    """
    Comment delete response scheme
    """
    msg: str
    data: object = {}