import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# 登录测试接口
def test_login():
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

    # 再登录
    response = client.post(
        "/login",
        json={
            "username": username,
            "password": "123456"
        }
    )

    # 登录必须成功 否则测试失败
    assert response.status_code == 200
