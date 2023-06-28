from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class ToolBoxPost(BaseModel):
    """
    ToolBox Post
    """
    _id: str
    tool_name: str = Field(
        ..., title="Name of the tool", min_length = 3, max_length=32
    )
    tool_description: str = Field(
        ..., title="Description of the tool", min_length = 8, max_length=128
    )
    tool_image: Optional[str] = Field(default=null, alias="tool image")
    tool_languages: Optional[str] = Field(default=null, alias="tool languages")
    tool_rating: Optional[str] = Field(default=null, alias="classificação")
    tool_website: Optional[str] = Field(default=null, alias="aplication website")
    tool_tags: Optional[str] = Field(default=null, alias="Tool Tags")
    tool_category: Optional[str] = Field(default=null, alias="Tool category")
    tool_price: Optional[str] = Field(default=null, alias="Tool Price")


class ToolBoxCreateResponse(BaseModel):
    """
    Toolbox create response
    """
    msg: str
    data: object = {}


class ToolBoxGetResponse(BaseModel):
    """
    Toolbox get response scheme
    """
    msg: str
    data: object = {}


class ToolBoxDeleteResponse(BaseModel):
    """
    Toolbox delete response scheme
    """
    msg: str
    data: object = {}