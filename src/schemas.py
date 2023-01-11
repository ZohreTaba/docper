from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """
    pass


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime]
    modified_at: Optional[datetime]


class IDModelMixin(BaseModel):
    id: int
