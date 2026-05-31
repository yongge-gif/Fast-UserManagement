from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# 注册测试接口
def test_register():

    response = client.post(
        "/register",
        data={
            "username": "pytest_user4",
            "password": "123456",
            "email": "pytest@test.com"
        }
    )

    assert response.status_code == 200
