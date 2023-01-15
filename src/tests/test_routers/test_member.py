# import pytest
# from httpx import AsyncClient
# from main import app
# from src.models.member import Member
#
#
# @pytest.mark.asyncio
# async def test_testpost():
#     name = "Taba"
#     assert await Member.filter(user_name=name).count() == 0
#
#     data = {"user_name": name}
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/member/create", json=data)
#         assert response.json() == dict(data, id=1)
#         assert response.status_code == 200
#
#         response = await ac.get("/member/members")
#         assert response.status_code == 200
#         assert response.json() == [dict(data, id=1)]
#
#     assert await Member.filter(username=name).count() == 1
#
