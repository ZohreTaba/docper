from typing import List

from src.models.document import *
from src.settings import settings
from src.schemas import Status

from fastapi import APIRouter, Depends, Header, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()
#
#
# @router.get("/document",
#             description="Fake methode for authorize member",
#             include_in_schema=False)
# async def validate_current_user(user_agent: str | None = Header(default=None)):
#     if not settings.DEFAULT_USER == user_agent:
#         raise HTTPException(status_code=404, detail=f"Member {user_agent} not access to change")
#
#
# @router.get("/categories",
#             description="Gets all categories",
#             response_model=List[CategoryPydantic])
# async def get_all():
#     return await CategoryPydantic.from_queryset(Category.all())
#
#
# @router.get("/category/{category_id}",
#             description="Gets the category with category Id",
#             response_model=CategoryPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def get_category_by_id(category_id: int):
#     return await CategoryPydantic.from_queryset_single(Category.get(id=category_id))
#
#
# @router.get("/category/{category_name}",
#             description="Gets the category with category name",
#             response_model=CategoryPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def get_category_by_name(category_name: str):
#     return await CategoryPydantic.from_queryset_single(CategoryPydantic.get(name=category_name))
#
#
# @router.post("/create",
#              description="Register the category",
#              response_model=CategoryPydantic,
#              dependencies=[Depends(validate_current_user)])
# async def create_category(category: CategoryInPydantic):
#     category_obj = await Category.create(**category.dict(exclude_unset=True))
#     return await CategoryPydantic.from_tortoise_orm(category_obj)
#
#
# @router.put("/category/{category_id}",
#             description="Updates the category",
#             response_model=CategoryPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def update_category(category_id: int, category: CategoryInPydantic):
#     await Category.filter(id=category_id).update(**category.dict(exclude_unset=True))
#     return await CategoryPydantic.from_queryset_single(Category.get(id=category_id))
#
#
# @router.delete("/category/{category_id}",
#                description="Deletes the category",
#                response_model=Status,
#                responses={404: {"model": HTTPNotFoundError}})
# async def delete_category(category_id: int):
#     deleted_count = await Category.filter(id=category_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
#     return Status(message=f"Deleted category {category_id}")
#
#
# @router.get("/authors",
#             description="Gets all authors",
#             response_model=List[AuthorPydantic])
# async def get_all():
#     return await AuthorPydantic.from_queryset(Author.all())
#
#
# @router.get("/author/{author_id}",
#             description="Gets the author with ID",
#             response_model=AuthorPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def get_author_by_id(author_id: int):
#     return await AuthorPydantic.from_queryset_single(Author.get(id=author_id))
#
#
# @router.get("/author/{author_name}",
#             description="Gets the author with name",
#             response_model=AuthorPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def get_author_by_name(author_name: str):
#     return await AuthorPydantic.from_queryset_single(AuthorPydantic.get(name=author_name))
#
#
# @router.post("/create",
#              description="Register the author",
#              response_model=AuthorPydantic,
#              dependencies=[Depends(validate_current_user)])
# async def create_author(author: AuthorInPydantic):
#     author_obj = await Author.create(**author.dict(exclude_unset=True))
#     return await AuthorPydantic.from_tortoise_orm(author_obj)
#
#
# @router.put("/author/{author_id}",
#             description="Updates the author",
#             response_model=AuthorPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def update_author(author_id: int, author: AuthorInPydantic):
#     await Author.filter(id=author_id).update(**author.dict(exclude_unset=True))
#     return await AuthorInPydantic.from_queryset_single(Author.get(id=author_id))
#
#
# @router.delete("/author/{author_id}",
#                description="Deletes the author",
#                response_model=Status,
#                responses={404: {"model": HTTPNotFoundError}})
# async def delete_author(author_id: int):
#     deleted_count = await Author.filter(id=author_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"Author {author_id} not found")
#     return Status(message=f"Deleted author {author_id}")
#
#
# @router.get("/documents",
#             description="Gets all documents",
#             response_model=List[DocumentPydantic])
# async def get_all():
#     return await DocumentPydantic.from_queryset(Document.all())
#
#
# @router.get("/document/{document_id}",
#             description="Gets the document with ID",
#             response_model=DocumentPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def get_author_by_id(document_id: int):
#     return await DocumentPydantic.from_queryset_single(Document.get(id=document_id))
#
#
# @router.get("/document/{document_name}",
#             description="Gets the document with name",
#             response_model=DocumentPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def get_document_by_name(document_name: str):
#     return await DocumentPydantic.from_queryset_single(DocumentPydantic.get(name=document_name))
#
#
# @router.post("/create",
#              description="Register the document",
#              response_model=DocumentPydantic,
#              dependencies=[Depends(validate_current_user)])
# async def create_document(document: DocumentPydantic):
#     document_obj = await Document.create(**document.dict(exclude_unset=True))
#     return await DocumentPydantic.from_tortoise_orm(document_obj)
#
#
# @router.put("/document/{document_id}",
#             description="Updates the document",
#             response_model=DocumentPydantic,
#             responses={404: {"model": HTTPNotFoundError}})
# async def update_document(document_id: int, document: DocumentInPydantic):
#     await Document.filter(id=document_id).update(**document.dict(exclude_unset=True))
#     return await DocumentInPydantic.from_queryset_single(Document.get(id=document_id))
#
#
# @router.delete("/document/{document_id}",
#                description="Deletes the document",
#                response_model=Status,
#                responses={404: {"model": HTTPNotFoundError}})
# async def delete_document(document_id: int):
#     deleted_count = await Author.filter(id=document_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"Document {document_id} not found")
#     return Status(message=f"Deleted document {document_id}")
