from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# 登录测试接口
def test_login():

    response = client.post(
        "/login",
        json={
            "username": "pytest_user",
            "password": "123456"
        }
    )

    # 登录必须成功 否则测试失败
    assert response.status_code == 200
