

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_queryset_creator, pydantic_model_creator
from models.document import *
from models.member import *
from models.permission import *
from tortoise import Tortoise


# Tortoise.init_models(["models.document", "models.member", "models.permission"],
#                      'models')



class CategoryPyResult(BaseModel):
    id: int
    name: str


class AuthorPyResult(BaseModel):
    id: int
    name: str


class DocumentPyResult (BaseModel):

    can_create: bool
    can_read: bool
    can_update: bool
    can_delete: bool
    id: int
    category: CategoryPyResult
    author: AuthorPyResult


class Status(BaseModel):
    message: str


MemberPydantic = pydantic_model_creator(Member, name="MemberPy")
MemberInPydantic = pydantic_model_creator(Member, name="MemberPyIn", exclude_readonly=True)

DocumentPydantic = pydantic_model_creator(Document, name="DocumentPy")
DocumentUpdatePydantic = pydantic_model_creator(Document, name="DocumentUpdatePydantic", exclude=("created_at", "id"))
DocumentInPydantic = pydantic_model_creator(Document, name="DocumentPyIn", exclude_readonly=True)

CategoryPydantic = pydantic_model_creator(Category, name="CategoryPy")
CategoryInPydantic = pydantic_model_creator(Category, name="CategoryPyIn", exclude_readonly=True)

AuthorPydantic = pydantic_model_creator(Author, name="AuthorPy")
AuthorInPydantic = pydantic_model_creator(Author, name="AuthorPyIn", exclude_readonly=True)

CategoryPermissionPydantic = pydantic_model_creator(CategoryPermission, name="CategoryPerPy")
CategoryPermissionInPydantic = pydantic_model_creator(CategoryPermission, name="CategoryPerPyIn",
                                                      exclude_readonly=True,
                                                      exclude=("member_id", "category_id"))

DocumentPermissionPydantic = pydantic_model_creator(DocumentPermission, name="CategoryDocPy")
DocumentPermissionInPydantic = pydantic_model_creator(DocumentPermission, name="CategoryDocPyIn",
                                                      exclude_readonly=True,
                                                      exclude=("member_id", "document_id"))

