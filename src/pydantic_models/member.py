
from pydantic import validator
from src.schemas import CoreModel, DateTimeModelMixin, IDModelMixin
from typing import Optional


# simple check for valid username
def validate_username(username: str) -> str:
    assert len(username) >= 3, "Username must be 3 characters or more."
    return username


class MemberBase(CoreModel):
    """
    Member Base
    """
    user_name: str
    is_active: bool = True
    is_superuser: bool = False


class MemberCreate(CoreModel):
    """
    Member Create
    """
    user_name: str

    # @validator("username", pre=True)
    # def username_is_valid(cls, username: str) -> str:
    #     return validate_username(username)

    class Config:
        orm_mode = True


class MemberInDB(IDModelMixin, DateTimeModelMixin, MemberBase):
    """
    Add in id, created_at, updated_at
    """

    class Config:
        orm_mode = True


class MemberPublic(DateTimeModelMixin, MemberBase):
    """
    for response model we do not want to return id to the user
    """

    class Config:
        orm_mode = True
