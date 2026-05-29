 # 基于Python 3.11镜像
FROM python:3.11

# 容器工作目录
WORKDIR /app

# 拷贝项目文件
COPY . .

# 安装依赖
RUN pip install -r requirements.txt

# 启动 FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]