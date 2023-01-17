
from fastapi import APIRouter, Header, HTTPException, Depends

from models.schemas import *
from settings import *

router = APIRouter()


@router.get("/",
            description="Fake methode for authorize member",
            include_in_schema=False)
async def check_if_user_is_admin(user_admin: str | None = Header(default=None)):
    if not settings.DEFAULT_USER == user_admin:
        raise HTTPException(status_code=404, detail=f"Member {user_admin} not access to change")


@router.post("/set_document_permission",
             description="Sets document permission",
             response_model=DocumentPermissionPydantic,
             dependencies=[Depends(check_if_user_is_admin)])
async def set_permission_on_document(document_per: DocumentPermissionInPydantic,
                                     document_id: int,
                                     member_id: int):
    document_obj = await DocumentPermission.create(**document_per.dict(exclude_unset=True),
                                                   document_id=document_id,
                                                   member_id=member_id)
    return await DocumentPermissionPydantic.from_tortoise_orm(document_obj)


@router.post("/set_category_permission",
             description="Sets category permission",
             response_model=CategoryPermissionPydantic,
             dependencies=[Depends(check_if_user_is_admin)])
async def set_permission_on_category(category_per: CategoryPermissionInPydantic,
                                     category_id: int,
                                     member_id: int):
    category_obj = await CategoryPermission.create(**category_per.dict(exclude_unset=True),
                                                   category_id=category_id,
                                                   member_id=member_id)
    return await CategoryPermissionPydantic.from_tortoise_orm(category_obj)
