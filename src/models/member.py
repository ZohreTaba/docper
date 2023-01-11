
from tortoise import fields
from tortoise.models import Model


class Member(Model):

    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=230, null=False, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    is_active = fields.BooleanField(nullable=False, default="True")
    is_superuser = fields.BooleanField(nullable=False, default="False")



