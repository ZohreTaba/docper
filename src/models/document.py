
from tortoise import fields
from tortoise.models import Model

from tortoise.contrib.pydantic import pydantic_model_creator


class Category(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255, unique=True, null=False)
    documents: fields.ReverseRelation["Document"]
    created_at = fields.DatetimeField(auto_now_add=True)


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


DocumentPydantic = pydantic_model_creator(Document, name="DocumentPy")
DocumentUpdatePydantic = pydantic_model_creator(Document, name="DocumentUpdatePydantic", exclude=("created_at", "id"))
DocumentInPydantic = pydantic_model_creator(Document, name="DocumentPyIn", exclude_readonly=True)

CategoryPydantic = pydantic_model_creator(Category, name="CategoryPy")
CategoryInPydantic = pydantic_model_creator(Category, name="CategoryPyIn", exclude_readonly=True)

AuthorPydantic = pydantic_model_creator(Author, name="AuthorPy")
AuthorInPydantic = pydantic_model_creator(Author, name="AuthorPyIn", exclude_readonly=True)
