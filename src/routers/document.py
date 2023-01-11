
from src.models.document import *

from fastapi import APIRouter

router = APIRouter()


# @router.post('/create_document')
# async def create_document(document: document_pydantic):
#     document_info = document.dict(exclude_unset=True)
#     document_obj = await Document.create(**document_info)
#     new_document = await document_pydantic.from_tortoise_orm(document_obj)
#     return {
#         "status": "ok",
#         "data": f"added document with subject {new_document.subject} in category {new_document.cateqory}"
#     }


# @router.post('/create_category')
# async def create_document(category: CreateCategory):
#     category_info = category.dict(exclude_unset=True)
#     category_obj = await Category.create(**category_info)
#     new_category = await Category.from_tortoise_orm(category_obj)
#     return {
#         "status": "ok",
#         "data": f"added category {new_category.name} , {new_category.id}"
#     }


# @router.post("/", dependencies=[Depends(current_user)])
# async def create_group(group: CreateGroup, user: User = Depends(current_user)):
#     user = await user
#     try:
#         await Group.create(**group.dict(exclude_unset=True), owner_id=user.id)
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#             detail="Group Name Already Exists"
#         )
#     return {"Group Created Successfully"}