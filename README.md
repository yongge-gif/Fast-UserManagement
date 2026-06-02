# FastAPI User Management System

基于 FastAPI + MySQL + Redis 构建的用户管理系统，集成 JWT 双 Token 认证、权限控制、Redis 缓存、接口限流、邮箱验证码、Celery 异步任务、Docker 容器化部署、自动化测试及 CI 持续集成等功能。

---

## 技术栈

### 后端框架

* FastAPI
* SQLAlchemy ORM
* Pydantic
* Alembic

### 数据库与缓存

* MySQL
* Redis

### 认证与安全

* JWT Access Token
* JWT Refresh Token
* bcrypt 密码加密
* RBAC 权限控制
* Redis 接口限流

### 异步任务

* Celery
* Redis Broker

### 工程化

* Docker
* Docker Compose
* Nginx
* Gunicorn
* Pytest
* GitHub Actions

---

## 核心功能

### 用户认证

* 用户注册
* 用户登录
* JWT 双 Token 认证
* Refresh Token 刷新机制
* 获取当前用户信息
* 修改密码

### 权限控制

* RBAC 角色权限管理
* 管理员接口权限控制
* 用户封禁功能

### 邮箱验证码

* 验证码生成
* Redis 缓存存储
* 过期时间控制
* 验证码校验

### Redis 缓存

* 用户信息缓存
* Cache Aside 旁路缓存模式
* 缓存更新策略

### 系统功能

* 用户头像上传
* 分页查询
* 软删除
* 排序查询
* 统一响应结构
* 全局异常处理

### 异步任务

* Celery 邮件异步发送
* 避免同步任务阻塞接口响应

---

## 项目架构

Client

↓

Nginx

↓

Gunicorn (4 Workers)

↓

FastAPI

↓

MySQL

FastAPI

↓

Redis

FastAPI

↓

Celery

↓

Email Service

---

## 项目结构

```text
fastapi_project
├── alembic
├── config
├── dependencies
├── models
├── routers
├── schemas
├── services
├── tests
├── uploads
├── utils
├── main.py
├── database.py
└── requirements.txt
```

## Docker Compose 服务

项目采用 Docker Compose 进行多服务编排：

* FastAPI
* MySQL
* Redis
* Celery
* Nginx

实现一键启动与统一管理。

```bash
docker compose up -d
```

---

## 自动化测试

使用 Pytest + HTTPX 编写接口自动化测试。

测试覆盖：

* 用户注册
* 用户登录
* 获取当前用户信息

执行测试：

```bash
pytest
```

---

## CI 持续集成

使用 GitHub Actions 实现持续集成。

流程：

```text
git push
    ↓
GitHub Actions
    ↓
Pytest
    ↓
测试通过
```

代码提交后自动执行测试，保证代码质量。

---

## API 文档

启动项目：

```bash
uvicorn main:app --reload
```

访问 Swagger：

```text
http://127.0.0.1:8000/docs
```

访问 ReDoc：

```text
http://127.0.0.1:8000/redoc
```

---

## 项目亮点

* FastAPI 分层架构设计
* JWT 双 Token 认证机制
* Redis 缓存优化
* Redis 接口限流
* Celery 异步任务
* Docker 容器化部署
* Docker Compose 服务编排
* Nginx 反向代理
* Gunicorn 多 Worker 部署
* Pytest 自动化测试
* GitHub Actions CI 持续集成

---

## 项目状态

持续迭代开发中。

后续计划：

* RabbitMQ
* 微服务架构升级
* 分布式缓存优化
* 分布式锁
* 操作日志系统
* 对象存储 OSS

---

## Author

杨连勇

Computer Science and Technology

Python Backend Developer

