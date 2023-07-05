from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class Message(BaseModel):
    type: str
    content: str
    date: datetime
    id_user_sender: str
    ids_users_receivers: list
    deleted: bool
    viewed: bool
    sent: bool


class GroupPost(BaseModel):
    """
    Group scheme
    """
    _id: str
    user_id_creator: str
    users_ids_receivers: list
    message: Message
    

class GroupCreateResponse(BaseModel):
    """
    Group create response
    """
    msg: str
    data: object = {}


class GroupGetResponse(BaseModel):
    """
    Group get response scheme
    """
    msg: str
    data: object = {}

class GroupDeleteResponse(BaseModel):
    """
        Group delete response scheme
        """
    msg: str
    data: object = {}