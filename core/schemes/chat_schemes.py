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
    id_user_receiver: str
    deleted: bool
    viewed: bool
    sent: bool


class ChatPost(BaseModel):
    """
    Chat scheme
    """
    _id: str
    user_id_sender: str
    user_id_receiver: str
    message: Message
    

class ChatCreateResponse(BaseModel):
    """
    Chat create response
    """
    msg: str
    data: object = {}


class ChatGetResponse(BaseModel):
    """
    Chat get response scheme
    """
    msg: str
    data: object = {}

class ChatDeleteResponse(BaseModel):
    """
        Chat delete response scheme
        """
    msg: str
    data: object = {}