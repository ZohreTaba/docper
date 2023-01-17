
from typing import List
from settings import settings
from models.schemas import *

from fastapi import APIRouter, Depends, Header, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


@router.get("/",
            description="Fake methode for authorize member",
            include_in_schema=False)
async def check_if_user_is_admin(user_admin: str | None = Header(default=None)):
    if not settings.DEFAULT_USER == user_admin:
        raise HTTPException(status_code=404, detail=f"Member {user_admin} not access to change")


@router.get("/documents",
            description="Gets all documents",
            response_model=List[DocumentPyResult])
async def get_all(current_user: str | None = Header(default=None)):
    user_access_document_list = await Document.filter(
        document_permissions__member__user_name=current_user).prefetch_related("category")

    user_access_document_by_category_list = await Document.filter(
        category__category_permissions__member__user_name=current_user).prefetch_related("category")

    all_documents = await Document.all().prefetch_related("category", "author")

    results = []
    for item in all_documents:
        result = DocumentPyResult(can_create=False,
                                  can_read=False,
                                  can_update=False,
                                  can_delete=False,
                                  id=item.id,
                                  category=CategoryPyResult(id=item.category.id,
                                                            name=item.category.name),
                                  author=AuthorPyResult(id=item.author.id,
                                                        name=item.author.name))

        for cat in user_access_document_by_category_list:
            if item.id == cat.id and item.category.id == cat.category.id:
                per = await get_permission_on_category(cat.category.id, current_user)
                result.can_create = per.can_creat
                result.can_read = per.can_read
                result.can_update = per.can_update
                result.can_delete = per.can_delete

        for doc in user_access_document_list:
            if item.id == doc.id and item.category.id == doc.category.id:
                per = await get_permission_on_document(item.id, current_user)
                result.can_create = per.can_creat
                result.can_read = per.can_read
                result.can_update = per.can_update
                result.can_delete = per.can_delete

        results.append(result)

    return results


@router.post("/create",
             description="Register the document",
             response_model=DocumentPydantic,
             dependencies=[Depends(check_if_user_is_admin)])
async def create_document(document: DocumentInPydantic, category_id: int, author_id: int):
    document_obj = await Document.create(**document.dict(exclude_unset=True),
                                         category_id=category_id,
                                         author_id=author_id)

    return await DocumentPydantic.from_tortoise_orm(document_obj)


@router.put("/update/{document_id}",
            description="Updates the document",
            response_model=DocumentUpdatePydantic,
            dependencies=[Depends(check_if_user_is_admin)],
            responses={404: {"model": HTTPNotFoundError}})
async def update_document(document_id: int, document: DocumentUpdatePydantic):
    await Document.filter(id=document_id).update(**document.dict(exclude_unset=True))
    return await DocumentInPydantic.from_queryset_single(Document.get(id=document_id))


@router.delete("/document/{document_id}",
               description="Deletes the document",
               response_model=Status,
               dependencies=[Depends(check_if_user_is_admin)],
               responses={404: {"model": HTTPNotFoundError}})
async def delete_document(document_id: int):
    deleted_count = await Document.filter(id=document_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Document {document_id} not found")
    return Status(message=f"Deleted document {document_id}")


async def get_permission_on_document(doc, user_name):
    return await DocumentPermission.filter(document_id=doc, member__user_name=user_name).first()


async def get_permission_on_category(cat, user_name):
    return await CategoryPermission.filter(category_id=cat, member__user_name=user_name).first()
