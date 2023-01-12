from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """
    pass


class Status(BaseModel):
    message: str
