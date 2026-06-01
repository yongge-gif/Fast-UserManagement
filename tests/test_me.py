import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# 获取token
@pytest.fixture()
def token():
    response = client.post(
        "/login",
        json={
            "username": "pytest_user",
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
