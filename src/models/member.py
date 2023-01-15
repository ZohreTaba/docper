
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.permission import CategoryPermission, DocumentPermission


class Member(Model):

    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=255, null=False, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    category_permissions: fields.ReverseRelation["CategoryPermission"]
    document_permissions: fields.ReverseRelation["DocumentPermission"]

    class Meta:
        table: str = 'documents_entity'
        ordering = ["id"]



