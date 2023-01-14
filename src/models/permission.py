
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.document import Category, Document


class CategoryPermission(Model):
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        'models.Category', related_name='category_permissions')
    member = fields.ForeignKeyField(
        'models.Member', related_name='category_permissions')
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()


class DocumentPermission(Model):
    document: fields.ForeignKeyRelation[Document] = fields.ForeignKeyField(
        'models.Document', related_name='document_permissions')
    member = fields.ForeignKeyField(
        'models.Member', related_name='document_permissions')
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()


CategoryPermissionPydantic = pydantic_model_creator(CategoryPermission, name="CategoryPerPy")
CategoryPermissionInPydantic = pydantic_model_creator(CategoryPermission, name="CategoryPerPyIn", exclude_readonly=True)

DocumentPermissionPydantic = pydantic_model_creator(DocumentPermission, name="CategoryDocPy")
DocumentPermissionInPydantic = pydantic_model_creator(DocumentPermission, name="CategoryDocPyIn", exclude_readonly=True)

