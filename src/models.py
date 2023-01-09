from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Member(Model):
    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=230, null=False, unique=True)
    members: fields.ReverseRelation["Document"]
    membersToCategoryPermission: fields.ReverseRelation["CategoryPermission"]
    membersToDocumentPermission: fields.ReverseRelation["DocumentPermission"]


class Category(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=230, unique=True, null=False)
    categories: fields.ReverseRelation["Document"]
    categoriesToCategoryPermission: fields.ReverseRelation["CategoryPermission"]
    categoriesToDocumentPermission: fields.ReverseRelation["DocumentPermission"]


class Document(Model):
    id = fields.IntField(pk=True, index=True)
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        "models.Category", related_name="categories", to_field="id")
    author: fields.ForeignKeyRelation[Member] = fields.ForeignKeyField(
        "models.Member", related_name="members", to_field="id")
    subject = fields.CharField(max_length=230, null=False)
    content = fields.CharField(max_length=230, null=False)


class CategoryPermission(Model):
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        "models.Category", related_name="categoriesToCategoryPermission", to_field="id")
    author: fields.ForeignKeyRelation[Member] = fields.ForeignKeyField(
        "models.Member", related_name="membersToCategoryPermission", to_field="id")
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()


class DocumentPermission(Model):
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        "models.Category", related_name="categoriesToDocumentPermission", to_field="id")
    author: fields.ForeignKeyRelation[Member] = fields.ForeignKeyField(
        "models.Member", related_name="membersToDocumentPermission", to_field="id")
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()


category_pydantic = pydantic_model_creator(Category, name="Category")
category_pydanticIn = pydantic_model_creator(Category, name="CategoryIn", exclude_readonly=True)
category_pydanticOut = pydantic_model_creator(Category, name="CategoryOut")

document_pydantic = pydantic_model_creator(Document, name="document")
document_pydanticIn = pydantic_model_creator(Document, name="documentIn", exclude_readonly=True)
document_pydanticOut = pydantic_model_creator(Document, name="documentOut")

member_pydantic = pydantic_model_creator(Member, name="member")
member_pydanticIn = pydantic_model_creator(Member, name="memberIn", exclude_readonly=True)
member_pydanticOut = pydantic_model_creator(Member, name="memberOut")


category_permission_pydantic = pydantic_model_creator(CategoryPermission, name="categoryPermission")
category_permission_pydanticIn = pydantic_model_creator(CategoryPermission, name="categoryPermissionIn", exclude_readonly=True)
category_permission_pydanticOut = pydantic_model_creator(CategoryPermission, name="categoryPermissionOut")

document_permission_pydantic = pydantic_model_creator(DocumentPermission, name="documentPermission")
document_permission_pydanticIn = pydantic_model_creator(DocumentPermission, name="documentPermissionIn", exclude_readonly=True)
document_permission_pydanticOut = pydantic_model_creator(DocumentPermission, name="documentPermissionOut")

