 # 基于Python 3.11镜像
FROM python:3.11

# 容器工作目录
WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# 拷贝项目文件
COPY . .

# 启动 FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]