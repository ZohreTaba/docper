
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Zohre(Model):
    pass


class CategoryPermission(Model):
    category = fields.ForeignKeyField('models.Category', related_name='category_permission')
    member = fields.ForeignKeyField('models.Member', related_name='category_member_permission')
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()


class DocumentPermission(Model):
    # document = fields.ForeignKeyField('models.Document', related_name='document_permission')
    member = fields.ForeignKeyField('models.Member', related_name='document_member_permission')
    can_creat = fields.BooleanField()
    can_read = fields.BooleanField()
    can_update = fields.BooleanField()
    can_delete = fields.BooleanField()

