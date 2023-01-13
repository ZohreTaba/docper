from typing import List

from src.models.member import *
from src.settings import settings
from src.schemas import Status

from fastapi import APIRouter, Depends, Header, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


@router.get("/",
            description="Fake methode for authorize member",
            include_in_schema=False)
async def validate_current_user(user_agent: str | None = Header(default=None)):
    if not settings.DEFAULT_USER == user_agent:
        raise HTTPException(status_code=404, detail=f"Member {user_agent} not access to change")


@router.get("/members",
            description="Gets all members",
            response_model=List[MemberPydantic])
async def get_all():
    return await MemberPydantic.from_queryset(Member.all())


@router.get("/{user_id}",
            description="Gets the member with user ID",
            response_model=MemberPydantic,
            responses={404: {"model": HTTPNotFoundError}})
async def get_member_by_id(user_id: int):
    return await MemberPydantic.from_queryset_single(Member.get(id=user_id))


@router.get("/{user_name}",
            description="Gets the member with user name",
            response_model=MemberPydantic,
            responses={404: {"model": HTTPNotFoundError}})
async def get_member_by_name(user_name: str):
    return await MemberPydantic.from_queryset_single(Member.get(user_name=user_name))


@router.post("/create",
             description="Registers the member",
             response_model=MemberPydantic,
             dependencies=[Depends(validate_current_user)])
async def create_member(member: MemberInPydantic):
    member_obj = await Member.create(**member.dict(exclude_unset=True))
    return await MemberPydantic.from_tortoise_orm(member_obj)


@router.put("/update/{user_id}",
            description="Updates the member",
            response_model=MemberPydantic,
            responses={404: {"model": HTTPNotFoundError}})
async def update_member(user_id: int, member: MemberInPydantic):
    await Member.filter(id=user_id).update(**member.dict(exclude_unset=True))
    return await MemberPydantic.from_queryset_single(Member.get(id=user_id))


@router.delete("/delete/{user_id}",
               description="Deletes the member",
               response_model=Status,
               responses={404: {"model": HTTPNotFoundError}})
async def delete_member(user_id: int):
    deleted_count = await Member.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Member {user_id} not found")
    return Status(message=f"Deleted member {user_id}")
