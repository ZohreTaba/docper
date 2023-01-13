from typing import List

from src.models.document import *
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


@router.get("/authors",
            description="Gets all authors",
            response_model=List[AuthorPydantic])
async def get_all():
    return await AuthorPydantic.from_queryset(Author.all())


@router.post("/create",
             description="Register the author",
             response_model=AuthorPydantic,
             dependencies=[Depends(validate_current_user)])
async def create_author(author: AuthorInPydantic):
    author_obj = await Author.create(**author.dict(exclude_unset=True))
    return await AuthorPydantic.from_tortoise_orm(author_obj)


@router.put("/update/{author_id}",
            description="Updates the author",
            response_model=AuthorPydantic,
            dependencies=[Depends(validate_current_user)],
            responses={404: {"model": HTTPNotFoundError}})
async def update_author(author_id: int, author: AuthorInPydantic):
    await Author.filter(id=author_id).update(**author.dict(exclude_unset=True))
    return await AuthorInPydantic.from_queryset_single(Author.get(id=author_id))


@router.delete("/delete/{author_id}",
               description="Deletes the author",
               response_model=Status,
               dependencies=[Depends(validate_current_user)],
               responses={404: {"model": HTTPNotFoundError}})
async def delete_author(author_id: int):
    deleted_count = await Author.filter(id=author_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Author {author_id} not found")
    return Status(message=f"Deleted author {author_id}")

