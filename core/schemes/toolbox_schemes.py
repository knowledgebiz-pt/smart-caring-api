from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class ToolBoxResponseData(BaseModel):
    items: list
    total_products: int


class ToolBoxGetResponse(BaseModel):
    """
    Toolbox get response scheme
    """
    msg: str
    data: ToolBoxResponseData
