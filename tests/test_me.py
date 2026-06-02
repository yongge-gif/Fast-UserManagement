import pytest, uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# 获取token
@pytest.fixture()
def token():
    username = f"pytest_{uuid.uuid4().hex[:8]}"

    # 先注册
    client.post(
        "/register",
        data={
            "username": username,
            "password": "123456",
            "email": f"{username}@test.com"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": username,
            "password": "123456"
        }
    )

    return response.json()["data"]["access_token"]


# 测试查询当前用户接口
def test_me(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get(
        "/me",
        headers=headers
    )

    assert response.status_code == 200
