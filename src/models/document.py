from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Category(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.id


class Document(Model):
    id = fields.IntField(pk=True, index=True)
    category_id = fields.IntField()
    author = fields.IntField()
    # category_id = fields.ForeignKeyField("models.Category", related_name="category")
    # author = fields.ForeignKeyField("models.Member", related_name="member")
    subject = fields.CharField(max_length=30, null=False)
    content = fields.CharField(max_length=30, null=False)

    def __str__(self):
        return self.id


category_pydantic = pydantic_model_creator(Category, name="Category")
category_pydanticIn = pydantic_model_creator(Category, name="CategoryIn", exclude_readonly=True)
category_pydanticOut = pydantic_model_creator(Category, name="CategoryOut")

document_pydantic = pydantic_model_creator(Document, name="document")
document_pydanticIn = pydantic_model_creator(Document, name="documentIn", exclude_readonly=True)
document_pydanticOut = pydantic_model_creator(Document, name="documentOut")


