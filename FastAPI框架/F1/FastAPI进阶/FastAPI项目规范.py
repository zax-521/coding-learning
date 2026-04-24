"""
    FastAPI 项目工程结构与模块化路由规范：
        一、推荐的工程结构
            1.标准三层架构（适合大多数项目）
                project/
                ├── app/
                │   ├── main.py                 # 应用入口
                │   ├── core/                   # 核心配置层
                │   │   ├── config.py          # 配置管理（Pydantic Settings）
                │   │   ├── security.py        # 安全相关（JWT、加密）
                │   │   ├── database.py        # 数据库连接
                │   │   └── exceptions.py      # 自定义异常
                │   │
                │   ├── api/                    # API层
                │   │   ├── v1/                # API版本控制
                │   │   │   ├── endpoints/     # 具体端点
                │   │   │   │   ├── users.py
                │   │   │   │   ├── items.py
                │   │   │   │   └── auth.py
                │   │   │   └── router.py      # v1路由聚合
                │   │   └── deps.py            # 全局依赖项
                │   │
                │   ├── models/                 # 数据库模型（SQLAlchemy）
                │   ├── schemas/               # Pydantic模型（请求/响应）
                │   ├── services/              # 业务逻辑层
                │   ├── crud/                  # CRUD操作层（可选）
                │   └── utils/                 # 工具函数
                │
                ├── tests/                     # 测试目录
                ├── .env                       # 环境变量
                └── requirements.txt
            
            2.各层职责说明
                | 目录  | 职责 | 依赖方向 |
                |------------|---------------------------|---------------------|
                | `api/`     | 路由层：处理HTTP请求与响应     | → services, schemas |
                | `services/`| 业务逻辑层：核心业务处理       | → crud, models      |
                | `crud/`    | 数据访问层：封装数据库操作      | → models            |
                | `schemas/` | Pydantic模型：数据验证与序列化 | 无                  |
                | `models/`  | ORM模型：数据库表映射         | 无                  |
                | `core/`    | 核心配置：全局配置与工具        | 无                  |
        ---
        二、模块化路由实现
            1. 基础路由模块示例
                **`app/api/v1/endpoints/users.py`**
                
                from fastapi import APIRouter, Depends, HTTPException, Query
                from typing import Optional
                from sqlalchemy.orm import Session
                
                from app.api import deps
                from app.schemas.user import UserCreate, UserResponse
                from app.services.user_service import user_service
                
                router = APIRouter()
                
                @router.get("/", response_model=List[UserResponse])
                async def get_users(
                    db: Session = Depends(deps.get_db),
                    skip: int = Query(0, ge=0),
                    limit: int = Query(100, ge=1, le=100),
                    current_user: User = Depends(deps.get_current_user)
                ):
                    # 获取用户列表，支持分页
                    return user_service.get_multi(db, skip=skip, limit=limit)
                
                @router.get("/{user_id}", response_model=UserResponse)
                async def get_user(
                    user_id: int,
                    db: Session = Depends(deps.get_db),
                    current_user: User = Depends(deps.get_current_user)
                ):
                    # 根据ID获取用户
                    user = user_service.get_by_id(db, user_id=user_id)
                    if not user:
                        raise HTTPException(status_code=404, detail="用户不存在")
                    return user
                
                @router.post("/", response_model=UserResponse, status_code=201)
                async def create_user(
                    user_in: UserCreate,
                    db: Session = Depends(deps.get_db)
                ):
                    # 创建新用户
                    existing_user = user_service.get_by_email(db, email=user_in.email)
                    if existing_user:
                        raise HTTPException(status_code=400, detail="邮箱已被注册")
                    return user_service.create(db, obj_in=user_in)

                2. 路由聚合器
                    **`app/api/v1/router.py`**
                    
                    from fastapi import APIRouter
                    from app.api.v1.endpoints import users, items, auth
                    
                    api_router = APIRouter()
                    
                    api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
                    api_router.include_router(users.router, prefix="/users", tags=["用户管理"])
                    api_router.include_router(items.router, prefix="/items", tags=["商品管理"])
                    
                3. 主应用注册
                    **`app/main.py`**

                    from fastapi import FastAPI
                    from app.api.v1.router import api_router
                    from app.core.config import settings
                    
                    app = FastAPI(
                        title=settings.PROJECT_NAME,
                        version=settings.VERSION,
                        docs_url="/api/docs"
                    )
                    
                    # 注册路由
                    app.include_router(api_router, prefix=settings.API_V1_STR)
                    
                    @app.get("/")
                    async def root():
                        return {"message": "API运行成功", "docs": "/api/docs"}
            ---
            三、核心规范要点
                1.路由设计原则
                    |     规范    |          说明         |               示例             |
                    |------------|----------------------|-------------------------------|
                    | RESTful风格 | 使用正确HTTP方法和状态码 | `GET /users`、`POST /users`   |
                    | 版本控制     | URL中包含版本号        | `/api/v1/users`               |
                    | 资源命名     | 使用复数名词           | `/users` ❌ `/user`          |
                    | 路径参数     | 与函数参数名一致        | `{user_id}` → `user_id: int` |

                2.关键最佳实践
                    1. 使用 `APIRouter`：每个资源模块独立路由
                    2. 设置 `prefix` 和 `tags`：保持API文档组织清晰
                    3. 使用 `response_model`：在装饰器中指定，而非依赖类型注解
                    4. 分离输入输出模型：请求和响应使用不同Pydantic模型
                    5. 保持路由"瘦"：复杂逻辑下沉到 `services` 层
                    6. 依赖注入：通过 `Depends` 管理依赖，提高可测试性

                3.配置管理
                    # app/core/config.py
                    from pydantic_settings import BaseSettings

                    class Settings(BaseSettings):
                        DATABASE_URL: str
                        SECRET_KEY: str
                        API_V1_STR: str = "/api/v1"

                        class Config:
                            env_file = ".env"

                    settings = Settings()
                    ---
            四、模块化进阶技巧
                1.动态路由注册（自动扫描）
                    def auto_register_routers(app: FastAPI, api_version: str = "v1"):
                        # 自动扫描并注册路由模块
                        endpoints_path = Path(__file__).parent / api_version / "endpoints"

                        for file_path in endpoints_path.glob("*.py"):
                            if file_path.name == "__init__.py":
                                continue

                            module = importlib.import_module(f"app.api.{api_version}.endpoints.{file_path.stem}")
                            if hasattr(module, "router"):
                                prefix = f"/{file_path.stem}"
                                tags = [file_path.stem.replace("_", " ").title()]
                                app.include_router(module.router, prefix=prefix, tags=tags)

                2.嵌套路由示例
                    # 处理资源关系：用户下的商品
                    @router.get("/{user_id}/items")
                    async def get_user_items(user_id: int):
                        return {"user_id": user_id, "items": []}

            五、总结速查表
                    | 方面     |            推荐做法            |      避免做法      |
                    |---------|------------------------------|-------------------|
                    | 项目结构 | 三层架构（api/services/models） | 所有代码堆在main.py  |
                    | 路由组织 | APIRouter + 版本前缀           | 直接在app上装饰路由   |
                    | 数据验证 | Pydantic模型                  | 手动验证或dict       |
                    | 业务逻辑 | 独立的service层                | 写在路由函数中        |
                    | 配置管理 | Pydantic Settings            | 硬编码或os.getenv散落 |
                    | 错误处理 | HTTPException + 全局处理器     | 裸raise Exception   |
                    | 类型注解 | 完整类型提示                   | 无注解或Any           |
"""