
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Member(Model):

    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=230, null=False, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table: str = 'documents_entity'
        ordering = ["id"]


MemberPydantic = pydantic_model_creator(Member, name="MemberPy")
MemberInPydantic = pydantic_model_creator(Member, name="MemberPyIn", exclude_readonly=True)
