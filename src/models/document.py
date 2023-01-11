
from tortoise import fields
from tortoise.models import Model


class Category(Model):

    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=230, unique=True, null=False)
    documents: fields.ReverseRelation["Document"]
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table: str = 'categories_entity'


class Author(Model):
    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=230, null=False, unique=True)

    documents: fields.ReverseRelation["Document"]

    class Meta:
        table: str = 'authors_entity'


class Document(Model):
    id = fields.IntField(pk=True, index=True)
    subject = fields.CharField(max_length=230, null=False)
    content = fields.CharField(max_length=230, null=False)
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        "models.Category", related_name="document")
    author: fields.ForeignKeyRelation[Author] = fields.ForeignKeyField(
        'models.Author', related_name='author')
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table: str = 'documents_entity'




