
from typing import List
from src.models.member import *

from fastapi import APIRouter, HTTPException
from src.schemas import Status

from tortoise.contrib.fastapi import HTTPNotFoundError


router = APIRouter()


@router.post(
    "/create",
    description="Register the member",
    response_model=MemberPydantic,
)
async def member_create(member: MemberInPydantic):
    member_obj = await Member.create(**member.dict(exclude_unset=True))
    return await MemberPydantic.from_tortoise_orm(member_obj)


@router.get(
    "/members",
    description="Gets members",
    response_model=List[MemberPydantic]
)
async def get_all():
    return await MemberPydantic.from_queryset(Member.all())


@router.get(
    "/member/{user_id}",
    response_model=MemberPydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def get_member_by_id(user_id: int):
    return await MemberPydantic.from_queryset_single(Member.get(id=user_id))


@router.get(
    "/member/{user_name}",
    response_model=MemberPydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def get_member_by_name(user_name: str):
    return await MemberPydantic.from_queryset_single(Member.get(user_name=user_name))


@router.put(
    "/member/{user_id}",
    response_model=MemberPydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_member(user_id: int, member: MemberInPydantic):
    await Member.filter(id=user_id).update(**member.dict(exclude_unset=True))
    return await MemberPydantic.from_queryset_single(Member.get(id=user_id))


@router.delete("/member/{user_id}",
               response_model=Status,
               responses={404: {"model": HTTPNotFoundError}})
async def delete_member(user_id: int):
    deleted_count = await Member.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Member {user_id} not found")
    return Status(message=f"Deleted member {user_id}")


async def get_member_by_username(user_name: str) -> MemberPydantic:
    return await MemberPydantic.from_queryset_single(Member.get(user_name=user_name))

