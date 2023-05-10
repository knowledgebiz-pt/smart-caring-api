from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class UserAdress(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str
    door_number: str

class UserPost(BaseModel):
    """
    User Post
    """
    _id: str
    name: str
    email: str
    receives_notification: Optional[bool] = Field(default=True, alias="receivesNotifications")
    notification_email: Optional[str] = Field(default=null, alias="notificationEmail")
    password: Optional[str] = Field(default=null, alias="password")
    picture: Optional[str] = Field(default=null, alias="picture")
    phone: Optional[str] = Field(default=null, max_length=11, alias="phone")
    birth_date: Optional[str] = Field(default=null, alias="birthDate", max_length=10)
    gmail_access_token: Optional[str] = Field(default=null, alias="gmailAccessToken")
    exponent_push_token: Optional[str] = Field(default=null, alias="exponentPushToken")
    address: UserAdress
    #partner: Optional[bool] = Field(default=False, alias="isPartner")


class UserCreateResponse(BaseModel):
    """
    User create response
    """
    msg: str
    data: object = {}


class UserGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}

