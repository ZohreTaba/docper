from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class CategoryPermission(Model):
    category_id = fields.IntField()
    member_id = fields.IntField()
    # category_id = fields.ForeignKeyField(model_name="models.Document", related_name='document')
    # member_id = fields.ForeignKeyField(model_name='models.Member', related_name='member')
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()

    def __str__(self):
        return self.member_id


class DocumentPermission(Model):
    document_id = fields.IntField()
    member_id = fields.IntField()
    # document_id = fields.ForeignKeyField(model_name="models.Document", related_name='document')
    # member_id = fields.ForeignKeyField(model_name='models.Member', related_name='member')
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()

    def __str__(self):
        return self.member_id


category_permission_pydantic = pydantic_model_creator(CategoryPermission, name="categoryPermission")
category_permission_pydanticIn = pydantic_model_creator(CategoryPermission, name="categoryPermissionIn", exclude_readonly=True)
category_permission_pydanticOut = pydantic_model_creator(CategoryPermission, name="categoryPermissionOut")

document_permission_pydantic = pydantic_model_creator(DocumentPermission, name="documentPermission")
document_permission_pydanticIn = pydantic_model_creator(DocumentPermission, name="documentPermissionIn", exclude_readonly=True)
document_permission_pydanticOut = pydantic_model_creator(DocumentPermission, name="documentPermissionOut")
