
from src.pydantic_models.member import *
from src.models.member import *

from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/create",
    description="Register the member",
    response_model=MemberPublic,
)
async def member_create(member: MemberCreate):
    return await create_member(member)


async def create_member(new_member: MemberCreate) -> MemberInDB:

    member_info = new_member.dict(exclude_unset=True)
    member_obj = await Member.create(**member_info)
    return MemberInDB.from_orm(member_obj)
