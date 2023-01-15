from typing import List

from src.models.document import *
from src.settings import settings
from src.models.schemas import *

from fastapi import APIRouter, Depends, Header, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


@router.get("/",
            description="Fake methode for authorize member",
            include_in_schema=False)
async def check_if_user_is_admin(user_admin: str | None = Header(default=None)):
    if not settings.DEFAULT_USER == user_admin:
        raise HTTPException(status_code=404, detail=f"Member {user_admin} not access to change")


@router.get("/categories",
            description="Gets all categories",
            response_model=List[CategoryPydantic])
async def get_all():
    return await CategoryPydantic.from_queryset(Category.all())


@router.post("/create",
             description="Register the category",
             response_model=CategoryPydantic,
             dependencies=[Depends(check_if_user_is_admin)])
async def create_category(category: CategoryInPydantic):
    category_obj = await Category.create(**category.dict(exclude_unset=True))
    return await CategoryPydantic.from_tortoise_orm(category_obj)


@router.put("/update/{category_id}",
            description="Updates the category",
            response_model=CategoryPydantic,
            dependencies=[Depends(check_if_user_is_admin)],
            responses={404: {"model": HTTPNotFoundError}})
async def update_category(category_id: int, category: CategoryInPydantic):
    await Category.filter(id=category_id).update(**category.dict(exclude_unset=True))
    return await CategoryPydantic.from_queryset_single(Category.get(id=category_id))


@router.delete("/delete/{category_id}",
               description="Deletes the category",
               response_model=Status,
               dependencies=[Depends(check_if_user_is_admin)],
               responses={404: {"model": HTTPNotFoundError}})
async def delete_category(category_id: int):
    deleted_count = await Category.filter(id=category_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return Status(message=f"Deleted category {category_id}")

