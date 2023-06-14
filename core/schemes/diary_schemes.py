from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class DiaryPost(BaseModel):
    """
    Diary Post
    """
    _id: str
    user_id: str
    title: str = Field(
        ..., title="The description of the item", min_length = 5, max_length=120
    )
    content: str = Field(
        ..., title="The description of the item", min_length = 50, max_length=3000
    )
    anexed_file: Optional[str] = Field(default=null, alias="Anexed File")
    tags: Optional[str] = Field(default=null, alias="Tags")
    public: bool = Field(default=False, alias="Visibility")


class DiaryCreateResponse(BaseModel):
    """
    Diary create response
    """
    msg: str
    data: object = {}


class DiaryGetResponse(BaseModel):
    """
    Diary get response scheme
    """
    msg: str
    data: object = {}

class DiaryDeleteResponse(BaseModel):
    """
        Diary delete response scheme
        """
    msg: str
    data: object = {}