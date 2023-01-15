
from tortoise import Tortoise
from pydantic import BaseModel

from src.models.document import *
from src.models.member import *
from src.models.permission import *


Tortoise.init_models(["src.models.document", "src.models.member", "src.models.permission"],
                     'models')


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """
    pass


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
