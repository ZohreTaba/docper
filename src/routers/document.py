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


@router.get("/documents",
            description="Gets all documents",
            response_model=List[DocumentPydantic])
async def get_all():
    return await DocumentPydantic.from_queryset(Document.all())


@router.post("/create",
             description="Register the document",
             response_model=DocumentPydantic,
             dependencies=[Depends(validate_current_user)])
async def create_document(document: DocumentInPydantic, category_id: int, author_id: int):
    document_obj = await Document.create(**document.dict(exclude_unset=True),
                                         category_id=category_id,
                                         author_id=author_id)

    return await DocumentPydantic.from_tortoise_orm(document_obj)


@router.put("/update/{document_id}",
            description="Updates the document",
            response_model=DocumentPydantic,
            dependencies=[Depends(validate_current_user)],
            responses={404: {"model": HTTPNotFoundError}})
async def update_document(document_id: int, document: DocumentInPydantic):
    await Document.filter(id=document_id).update(**document.dict(exclude_unset=True))
    return await DocumentInPydantic.from_queryset_single(Document.get(id=document_id))


@router.delete("/document/{document_id}",
               description="Deletes the document",
               response_model=Status,
               dependencies=[Depends(validate_current_user)],
               responses={404: {"model": HTTPNotFoundError}})
async def delete_document(document_id: int):
    deleted_count = await Author.filter(id=document_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Document {document_id} not found")
    return Status(message=f"Deleted document {document_id}")
