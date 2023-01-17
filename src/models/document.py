
from tortoise import fields
from tortoise.models import Model

# from src.models.permission import CategoryPermission, DocumentPermission


class Category(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255, unique=True, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    documents: fields.ReverseRelation["Document"]
    # category_permissions: fields.ReverseRelation["CategoryPermission"]


class Author(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255, null=False, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    documents: fields.ReverseRelation["Document"]


class Document(Model):
    id = fields.IntField(pk=True, index=True)
    subject = fields.CharField(max_length=255, null=False)
    content = fields.CharField(max_length=255, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        "models.Category", related_name="category")
    author: fields.ForeignKeyRelation[Author] = fields.ForeignKeyField(
        'models.Author', related_name='author')

    # document_permissions: fields.ReverseRelation["DocumentPermission"]


