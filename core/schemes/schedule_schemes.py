from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class SchedulePost(BaseModel):
    """
    News Schedule Event
    """
    _id: str
    id_user: str
    event_name: str = Field(
        ..., title="The description of the item", min_length = 5, max_length=32
    )
    event_description: Optional[str] = Field(
        ..., title="The description of the item", min_length = 50, max_length=3000
    )
    date: datetime


class ScheduleCreateResponse(BaseModel):
    """
    News create response
    """
    msg: str
    data: object = {}


class ScheduleGetResponse(BaseModel):
    """
    News get response scheme
    """
    msg: str
    data: object = {}

class ScheduleDeleteResponse(BaseModel):
    """
        News delete response scheme
        """
    msg: str
    data: object = {}