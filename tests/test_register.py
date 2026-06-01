import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 每次测试生成随机用户名
username = f"pytest_{uuid.uuid4().hex[:8]}"


# 注册测试接口
def test_register():

    response = client.post(
        "/register",
        data={
            "username": username,
            "password": "123456",
            "email": f"{username}@test.com"
        }
    )

    assert response.status_code == 200
