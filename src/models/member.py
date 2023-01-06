from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Member(Model):
    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.user_name


member_pydantic = pydantic_model_creator(Member, name="member")
member_pydanticIn = pydantic_model_creator(Member, name="memberIn", exclude_readonly=True)
member_pydanticOut = pydantic_model_creator(Member, name="memberOut")
