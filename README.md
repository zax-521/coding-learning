# 🗺️ 完整学习路径（详细版）

## 图例说明

| 标记 | 含义 |
|------|------|
| ⭐⭐⭐ | 必须学，核心技能 |
| ⭐⭐ | 重要，必须掌握 |
| ⭐ | 了解就行，知道概念 |
| 📅 | 以后学，当前阶段不需要 |
| 🔧 | 遇到再学，按需学习 |

---

## 第一阶段：Python 基础（2-3周）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 变量与数据类型 | ⭐⭐⭐ | int、float、str、bool、list、tuple、dict、set | 能区分可变/不可变类型 |
| 运算符 | ⭐⭐⭐ | 算术、比较、逻辑、赋值、身份（is/is not） | 熟练使用 |
| 字符串操作 | ⭐⭐⭐ | 切片、格式化（f-string）、join、split、strip | 能处理常见字符串 |
| 列表操作 | ⭐⭐⭐ | 增删改查、切片、排序、列表推导式 | 熟练 |
| 字典操作 | ⭐⭐⭐ | 增删改查、keys/values/items、字典推导式 | 熟练 |
| 元组与集合 | ⭐⭐ | 元组不可变、集合去重与运算 | 会用 |
| 控制流 | ⭐⭐⭐ | if/elif/else、for、while、break、continue | 熟练 |
| 函数 | ⭐⭐⭐ | 定义、参数（位置/关键字/默认值）、返回值、lambda | 熟练 |
| 作用域 | ⭐⭐ | global、nonlocal、LEGB规则 | 理解 |
| 异常处理 | ⭐⭐⭐ | try/except/else/finally、raise、自定义异常 | 熟练 |
| 文件操作 | ⭐⭐⭐ | open、with、读/写文本/JSON | 熟练 |
| 模块与包 | ⭐⭐⭐ | import、from...import、__name__、包结构 | 熟练 |
| 常用内置函数 | ⭐⭐⭐ | len、range、enumerate、zip、map、filter、sorted | 熟练 |
| collections模块 | ⭐ | defaultdict、Counter、deque | 知道存在，用时查 |
| datetime模块 | ⭐⭐ | date、time、datetime、timedelta、格式化 | 会用 |
| random模块 | ⭐ | 随机数生成 | 知道就行 |
| 正则表达式（re） | 🔧 | 匹配、搜索、替换 | 遇到再学 |
| 类型提示 | ⭐⭐⭐ | 变量类型、函数参数/返回值类型、Optional、Union、List、Dict | 熟练（FastAPI依赖） |
| 装饰器 | ⭐⭐⭐ | 函数装饰器、带参数装饰器、类装饰器 | 理解原理，能写简单装饰器 |
| 迭代器与生成器 | ⭐⭐ | iter、next、yield、生成器表达式 | 理解，会用yield |
| 上下文管理器 | ⭐⭐ | with语句、__enter__/__exit__ | 理解，会用 |
| 异步基础 | ⭐⭐⭐ | async def、await、asyncio.run、asyncio.sleep | 理解概念，会写async函数 |
| asyncio进阶 | ⭐⭐ | create_task、gather、wait、Semaphore | 会并发执行多个任务 |
| 面向对象基础 | ⭐⭐ | class、self、__init__、属性、方法 | 理解，能用 |
| 面向对象进阶 | 🔧 | 继承、多态、@property、__slots__、元类 | 以后学 |
| 多线程/多进程 | 📅 | threading、multiprocessing、concurrent.futures | FastAPI用异步，暂时不需要 |
| 虚拟环境 | ⭐⭐⭐ | venv、pip、requirements.txt | 熟练 |

---

## 第二阶段：SQL 基础（1周）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 数据库概念 | ⭐⭐⭐ | 数据库、表、字段、记录、主键、外键 | 理解 |
| 查询基础 | ⭐⭐⭐ | SELECT、FROM、WHERE、AND/OR、IN、BETWEEN、LIKE、IS NULL | 熟练 |
| 排序与分页 | ⭐⭐⭐ | ORDER BY（ASC/DESC）、LIMIT、OFFSET | 熟练 |
| 聚合函数 | ⭐⭐⭐ | COUNT、SUM、AVG、MAX、MIN | 熟练 |
| 分组查询 | ⭐⭐⭐ | GROUP BY、HAVING | 熟练 |
| 表连接 | ⭐⭐⭐ | INNER JOIN、LEFT JOIN、RIGHT JOIN、多表连接 | 熟练 |
| 子查询 | ⭐⭐ | WHERE子查询、FROM子查询、EXISTS | 会写简单子查询 |
| 插入数据 | ⭐⭐⭐ | INSERT INTO、INSERT INTO SELECT | 熟练 |
| 更新数据 | ⭐⭐⭐ | UPDATE、WHERE条件更新 | 熟练 |
| 删除数据 | ⭐⭐⭐ | DELETE、TRUNCATE | 熟练 |
| 创建表 | ⭐⭐⭐ | CREATE TABLE、数据类型、约束 | 熟练 |
| 修改表结构 | ⭐⭐ | ALTER TABLE（ADD、DROP、MODIFY） | 会用 |
| 删除表 | ⭐⭐ | DROP TABLE | 会用 |
| 约束 | ⭐⭐⭐ | PRIMARY KEY、FOREIGN KEY、UNIQUE、NOT NULL、CHECK | 熟练 |
| 索引 | ⭐⭐ | CREATE INDEX、什么是索引、什么时候用 | 理解概念 |
| 事务 | ⭐⭐ | BEGIN、COMMIT、ROLLBACK | 理解概念 |
| 视图 | ⭐ | CREATE VIEW | 知道就行 |
| 存储过程 | 🔧 | 存储过程、触发器 | 业务逻辑写Python，不用学 |
| SQL 注入 | ⭐⭐⭐ | 什么是SQL注入、如何防范（参数化查询） | 理解 |

---

## 第三阶段：关系型数据库（1周）

选一个学透，推荐 MySQL。

### MySQL

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 安装与配置 | ⭐⭐⭐ | Windows/Mac/Linux安装、启动/停止服务 | 能安装并启动 |
| 连接工具 | ⭐⭐⭐ | 命令行mysql、MySQL Workbench | 能用 |
| 用户与权限 | ⭐⭐ | CREATE USER、GRANT、REVOKE | 了解 |
| 数据库操作 | ⭐⭐⭐ | CREATE DATABASE、DROP DATABASE、USE | 熟练 |
| 数据类型 | ⭐⭐⭐ | INT、VARCHAR、TEXT、DATE、DATETIME、TIMESTAMP、DECIMAL、BOOLEAN | 熟练 |
| 字符集与排序规则 | ⭐ | UTF8、utf8mb4、COLLATE | 知道就行 |
| 导入/导出数据 | ⭐⭐ | mysqldump、SOURCE | 会用 |
| 常用函数 | ⭐⭐ | NOW()、CURDATE()、CONCAT()、IFNULL() | 会用 |
| 慢查询日志 | ⭐ | 什么是慢查询 | 知道就行 |
| 主从复制 | 📅 | 读写分离概念 | 以后学 |

### SQLite（可选，用于本地开发）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| SQLite特点 | ⭐ | 文件型数据库、零配置 | 了解 |
| 连接与操作 | ⭐⭐ | sqlite3命令行、Python sqlite3模块 | 会用 |

### PostgreSQL（以后学，有需要再学）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| JSON/JSONB | 📅 | 存储和查询JSON数据 | 需要时学 |
| 数组类型 | 📅 | 数组字段、数组操作 | 需要时学 |
| 全文搜索 | 📅 | tsvector、tsquery | 需要时学 |
| 行级安全 | 📅 | RLS策略 | 需要时学 |

---

## 第四阶段：FastAPI 框架（2-3周）

### 4.1 基础路由

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 创建应用 | ⭐⭐⭐ | FastAPI()、uvicorn运行 | 熟练 |
| GET请求 | ⭐⭐⭐ | @app.get()、路径参数、查询参数 | 熟练 |
| POST请求 | ⭐⭐⭐ | @app.post()、请求体 | 熟练 |
| PUT请求 | ⭐⭐⭐ | @app.put()、更新资源 | 熟练 |
| DELETE请求 | ⭐⭐⭐ | @app.delete() | 熟练 |
| PATCH请求 | ⭐⭐ | @app.patch()、部分更新 | 会用 |
| 路由顺序 | ⭐⭐ | 静态路由在前，动态路由在后 | 理解 |

### 4.2 参数与校验

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 路径参数 | ⭐⭐⭐ | /users/{user_id}、类型转换 | 熟练 |
| 查询参数 | ⭐⭐⭐ | /users?page=1&size=10、默认值、可选参数 | 熟练 |
| 请求体 | ⭐⭐⭐ | Pydantic模型、必填/可选字段 | 熟练 |
| 表单数据 | ⭐⭐ | Form()、application/x-www-form-urlencoded | 会用 |
| 文件上传 | ⭐⭐ | UploadFile、File()、多文件上传 | 会用 |
| 请求头 | ⭐⭐⭐ | Header() | 会用 |
| Cookie | ⭐⭐ | Cookie() | 会用 |

### 4.3 Pydantic（重要）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| BaseModel | ⭐⭐⭐ | 定义模型、字段类型 | 熟练 |
| 字段校验 | ⭐⭐⭐ | Field()、min_length、max_length、gt、lt、regex | 熟练 |
| 可选字段 | ⭐⭐⭐ | Optional、默认值、None | 熟练 |
| 嵌套模型 | ⭐⭐⭐ | 模型作为字段类型 | 熟练 |
| 模型继承 | ⭐⭐ | 复用字段 | 会用 |
| 数据验证装饰器 | ⭐⭐ | @validator、@field_validator | 会用 |
| 模型转换 | ⭐⭐ | dict()、json()、from_orm() | 会用 |
| 配置类 | ⭐⭐ | class Config、orm_mode、extra | 会用 |

### 4.4 响应

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 响应模型 | ⭐⭐⭐ | response_model、过滤输出 | 熟练 |
| 状态码 | ⭐⭐⭐ | status_code、HTTP状态码含义 | 熟练 |
| 响应头 | ⭐⭐ | Response、headers参数 | 会用 |
| 响应Cookie | ⭐⭐ | set_cookie | 会用 |
| JSONResponse | ⭐⭐ | 自定义JSON响应 | 会用 |
| HTMLResponse | ⭐ | 返回HTML | 了解 |
| 文件响应 | ⭐ | FileResponse | 了解 |
| 流式响应 | 🔧 | StreamingResponse | 需要时学 |

### 4.5 异常处理

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| HTTPException | ⭐⭐⭐ | 抛出HTTP错误响应 | 熟练 |
| 自定义异常处理器 | ⭐⭐ | @app.exception_handler | 会用 |
| 请求验证异常 | ⭐⭐ | RequestValidationError | 了解 |

### 4.6 依赖注入（核心）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 函数依赖 | ⭐⭐⭐ | Depends()、依赖函数 | 熟练 |
| 类依赖 | ⭐⭐ | 类作为依赖、__call__ | 会用 |
| 嵌套依赖 | ⭐⭐⭐ | 依赖可以依赖其他依赖 | 熟练 |
| 带yield的依赖 | ⭐⭐⭐ | 资源管理、数据库会话 | 熟练 |
| 缓存依赖 | ⭐⭐ | 同一请求中依赖默认缓存 | 理解 |
| 全局依赖 | ⭐⭐ | app = FastAPI(dependencies=...) | 了解 |

### 4.7 中间件

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 中间件基础 | ⭐⭐⭐ | @app.middleware("http") | 熟练 |
| CORS中间件 | ⭐⭐⭐ | CORSMiddleware、配置 | 熟练 |
| 日志中间件 | ⭐⭐⭐ | 记录请求耗时、请求ID | 熟练 |
| 限流中间件 | 🔧 | 基于IP的限流 | 需要时学 |
| 请求体大小限制 | 🔧 | 限制上传大小 | 需要时学 |
| 响应压缩 | 🔧 | GzipMiddleware | 需要时学 |
| 请求ID中间件 | ⭐⭐ | 生成UUID、添加到响应头 | 会用 |
| 认证中间件 | ⭐⭐ | 验证token | 会用 |

### 4.8 路由组织

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| APIRouter | ⭐⭐⭐ | 拆分路由到多个文件 | 熟练 |
| 路由前缀 | ⭐⭐⭐ | prefix="/api/v1" | 熟练 |
| 路由标签 | ⭐⭐ | tags=["users"] | 会用 |
| 路由依赖 | ⭐⭐ | dependencies=[Depends(...)] | 会用 |
| 路由响应模型 | ⭐⭐ | responses={...} | 了解 |

### 4.9 配置管理

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 环境变量 | ⭐⭐⭐ | os.getenv()、python-dotenv | 熟练 |
| pydantic-settings | ⭐⭐⭐ | BaseSettings、嵌套配置 | 熟练 |
| 多环境配置 | ⭐⭐ | .env.dev、.env.prod | 会用 |
| 配置验证 | ⭐⭐ | 类型校验、必填校验 | 会用 |

### 4.10 后台任务

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| BackgroundTasks | ⭐⭐ | add_task()、后台执行函数 | 会用 |
| 任务参数 | ⭐⭐ | 传递参数给后台任务 | 会用 |

### 4.11 事件处理

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 启动事件 | ⭐⭐ | @app.on_event("startup") | 会用 |
| 关闭事件 | ⭐⭐ | @app.on_event("shutdown") | 会用 |
| lifespan上下文管理器 | ⭐⭐ | async with contextlib.asynccontextmanager | 会用 |

### 4.12 静态文件与模板

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 静态文件 | ⭐ | StaticFiles、mount | 了解 |
| Jinja2模板 | ⭐ | Jinja2Templates | 了解 |

### 4.13 高级特性

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| WebSocket | 📅 | @app.websocket | 以后学 |
| GraphQL | 📅 | strawberry、graphene | 以后学 |
| 版本控制 | 🔧 | /v1、/v2 | 需要时学 |
| OpenAPI自定义 | ⭐ | description、summary、tags | 了解 |

---

## 第五阶段：ORM（1-2周）

选择 **SQLAlchemy 2.0**（异步支持 + 类型提示）

### 5.1 核心概念

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| Engine | ⭐⭐⭐ | create_engine、create_async_engine | 熟练 |
| Session | ⭐⭐⭐ | sessionmaker、async_sessionmaker | 熟练 |
| Model基类 | ⭐⭐⭐ | DeclarativeBase | 熟练 |
| 映射列 | ⭐⭐⭐ | Mapped、mapped_column | 熟练 |
| 数据类型 | ⭐⭐⭐ | String、Integer、DateTime、Boolean | 熟练 |

### 5.2 模型定义

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 表名 | ⭐⭐⭐ | __tablename__ | 熟练 |
| 主键 | ⭐⭐⭐ | primary_key=True | 熟练 |
| 自增主键 | ⭐⭐⭐ | autoincrement=True、Identity | 熟练 |
| 默认值 | ⭐⭐⭐ | default、server_default | 熟练 |
| 可空字段 | ⭐⭐⭐ | nullable=True/False | 熟练 |
| 唯一约束 | ⭐⭐ | unique=True | 会用 |
| 索引 | ⭐⭐ | index=True | 会用 |
| 外键 | ⭐⭐⭐ | ForeignKey | 熟练 |
| 关系 | ⭐⭐⭐ | relationship()、back_populates | 熟练 |
| 联合唯一 | ⭐⭐ | UniqueConstraint | 会用 |
| 复合主键 | ⭐ | 多个字段作为主键 | 了解 |

### 5.3 CRUD操作

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 插入 | ⭐⭐⭐ | session.add()、session.add_all()、session.commit() | 熟练 |
| 刷新 | ⭐⭐⭐ | session.refresh() | 熟练 |
| 查询（2.0语法） | ⭐⭐⭐ | select()、session.execute() | 熟练 |
| 获取全部 | ⭐⭐⭐ | scalars().all() | 熟练 |
| 获取第一条 | ⭐⭐⭐ | scalars().first() | 熟练 |
| 获取单个 | ⭐⭐⭐ | session.get(Model, id) | 熟练 |
| 条件过滤 | ⭐⭐⭐ | where()、filter() | 熟练 |
| 多条件 | ⭐⭐⭐ | and_()、or_() | 熟练 |
| 排序 | ⭐⭐⭐ | order_by() | 熟练 |
| 分页 | ⭐⭐⭐ | offset()、limit() | 熟练 |
| 更新 | ⭐⭐⭐ | 修改属性 + commit() | 熟练 |
| 批量更新 | ⭐⭐ | update() | 会用 |
| 删除 | ⭐⭐⭐ | session.delete() + commit() | 熟练 |
| 批量删除 | ⭐⭐ | delete() | 会用 |

### 5.4 高级查询

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| LIKE查询 | ⭐⭐⭐ | like()、ilike() | 熟练 |
| IN查询 | ⭐⭐⭐ | in_() | 熟练 |
| BETWEEN | ⭐⭐ | between() | 会用 |
| NULL判断 | ⭐⭐⭐ | is_()、is_not() | 熟练 |
| 聚合函数 | ⭐⭐⭐ | func.count()、func.sum() | 熟练 |
| group_by | ⭐⭐⭐ | group_by() | 熟练 |
| having | ⭐⭐ | having() | 会用 |
| 连接查询 | ⭐⭐⭐ | join()、select_from() | 熟练 |
| 懒加载 | ⭐⭐⭐ | 默认行为，理解 | 理解 |
| 预加载 | ⭐⭐ | joinedload()、selectinload() | 会用 |
| 子查询 | ⭐⭐ | 作为查询条件 | 会用 |
| 原生SQL | ⭐⭐ | text() | 会用 |

### 5.5 异步ORM

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 异步引擎 | ⭐⭐⭐ | create_async_engine | 熟练 |
| 异步会话 | ⭐⭐⭐ | async_sessionmaker | 熟练 |
| 异步CRUD | ⭐⭐⭐ | await session.execute()、await session.commit() | 熟练 |
| 异步依赖注入 | ⭐⭐⭐ | async def get_db(): | 熟练 |

### 5.6 Alembic迁移

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 初始化 | ⭐⭐⭐ | alembic init | 熟练 |
| 配置连接 | ⭐⭐⭐ | alembic.ini、env.py | 熟练 |
| 生成迁移 | ⭐⭐⭐ | alembic revision --autogenerate | 熟练 |
| 执行迁移 | ⭐⭐⭐ | alembic upgrade head | 熟练 |
| 回滚 | ⭐⭐ | alembic downgrade | 会用 |
| 查看历史 | ⭐ | alembic history | 了解 |
| 异步支持 | ⭐⭐ | env.py配置async | 会用 |

### 5.7 进阶（以后学）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 连接池配置 | 📅 | pool_size、max_overflow | 以后学 |
| 事务嵌套 | 🔧 | savepoint | 需要时学 |
| 事件监听 | 🔧 | @event.listens_for | 需要时学 |
| 混合属性 | 🔧 | @hybrid_property | 需要时学 |
| 多数据库绑定 | 📅 | 多个engine | 以后学 |
| 分片 | 📅 | 水平分片 | 以后学 |

---

## 第六阶段：认证与安全（1周）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 哈希算法 | ⭐⭐ | MD5、SHA256（了解区别） | 理解 |
| bcrypt | ⭐⭐⭐ | passlib、哈希密码、验证密码 | 熟练 |
| JWT概念 | ⭐⭐⭐ | Header、Payload、Signature | 理解 |
| JWT生成 | ⭐⭐⭐ | jwt.encode() | 熟练 |
| JWT验证 | ⭐⭐⭐ | jwt.decode()、过期处理 | 熟练 |
| OAuth2PasswordBearer | ⭐⭐⭐ | tokenUrl、自动提取token | 熟练 |
| OAuth2PasswordRequestForm | ⭐⭐⭐ | 登录表单 | 熟练 |
| 当前用户依赖 | ⭐⭐⭐ | get_current_user | 熟练 |
| 密码重置 | ⭐ | 忘记密码流程 | 了解 |
| CORS配置 | ⭐⭐⭐ | allow_origins、allow_methods、allow_headers | 熟练 |
| CSRF防护 | 🔧 | 双提交Cookie、同源检查 | 需要时学 |
| HTTPS | ⭐ | SSL证书、TLS | 了解 |
| 环境变量存储密钥 | ⭐⭐⭐ | SECRET_KEY不写死在代码 | 熟练 |
| API Key认证 | ⭐⭐ | Header中的API Key | 会用 |
| 权限控制 | ⭐⭐ | 角色权限（admin、user） | 会用 |

---

## 第七阶段：测试（3-5天）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| pytest安装 | ⭐⭐⭐ | pip install pytest | 熟练 |
| 测试函数 | ⭐⭐⭐ | def test_xxx()、assert | 熟练 |
| fixture | ⭐⭐⭐ | @pytest.fixture、scope | 熟练 |
| TestClient | ⭐⭐⭐ | from fastapi.testclient import TestClient | 熟练 |
| GET测试 | ⭐⭐⭐ | client.get()、assert status_code | 熟练 |
| POST测试 | ⭐⭐⭐ | client.post()、json参数 | 熟练 |
| 请求头测试 | ⭐⭐ | headers参数 | 会用 |
| 依赖覆盖 | ⭐⭐⭐ | app.dependency_overrides | 熟练 |
| 临时数据库 | ⭐⭐⭐ | SQLite :memory: 或测试数据库 | 熟练 |
| 异步测试 | ⭐⭐ | pytest-asyncio | 会用 |
| 测试覆盖率 | ⭐⭐ | pytest-cov | 会用 |
| Mock | 🔧 | unittest.mock、模拟外部API | 需要时学 |
| 参数化测试 | ⭐⭐ | @pytest.mark.parametrize | 会用 |
| 跳过/预期失败 | ⭐ | @pytest.mark.skip、@pytest.mark.xfail | 了解 |

---

## 第八阶段：异步任务（以后学，按需）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| Celery概念 | 📅 | Worker、Broker、Backend | 需要时学 |
| Redis安装 | 📅 | 作为Broker | 需要时学 |
| Celery配置 | 📅 | Celery应用、配置Broker | 需要时学 |
| 定义任务 | 📅 | @celery.task | 需要时学 |
| 调用任务 | 📅 | .delay()、.apply_async() | 需要时学 |
| 任务结果 | 📅 | AsyncResult | 需要时学 |
| 定时任务 | 📅 | celery beat | 需要时学 |
| Flower监控 | 🔧 | Celery监控面板 | 需要时学 |
| FastAPI集成 | 📅 | 在路由中调用Celery任务 | 需要时学 |

---

## 第九阶段：Docker与容器化（1周）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| Docker概念 | ⭐⭐⭐ | 镜像、容器、仓库、Dockerfile | 理解 |
| Docker安装 | ⭐⭐⭐ | 安装Docker Desktop | 熟练 |
| Dockerfile编写 | ⭐⭐⭐ | FROM、WORKDIR、COPY、RUN、CMD、EXPOSE | 熟练 |
| 构建镜像 | ⭐⭐⭐ | docker build -t name . | 熟练 |
| 运行容器 | ⭐⭐⭐ | docker run、-p、-d、--name | 熟练 |
| 查看容器 | ⭐⭐⭐ | docker ps、docker logs | 熟练 |
| 停止/删除 | ⭐⭐⭐ | docker stop、docker rm | 熟练 |
| 镜像管理 | ⭐⭐ | docker images、docker rmi | 会用 |
| 卷挂载 | ⭐⭐ | -v、--mount、代码热更新 | 会用 |
| 网络 | ⭐⭐ | docker network、容器间通信 | 会用 |
| docker-compose | ⭐⭐⭐ | docker-compose.yml、services | 熟练 |
| 多服务编排 | ⭐⭐⭐ | FastAPI + MySQL + Redis | 熟练 |
| 环境变量 | ⭐⭐⭐ | environment、env_file | 熟练 |
| 数据持久化 | ⭐⭐ | volumes | 会用 |
| Docker Hub | ⭐ | push、pull | 了解 |
| 多阶段构建 | 🔧 | 减小镜像大小 | 需要时学 |
| .dockerignore | ⭐⭐ | 忽略文件 | 会用 |

---

## 第十阶段：部署与运维（1周）

### 10.1 Linux基础命令

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 文件操作 | ⭐⭐⭐ | ls、cd、pwd、mkdir、rm、cp、mv、touch | 熟练 |
| 文件查看 | ⭐⭐⭐ | cat、less、head、tail、tail -f | 熟练 |
| 权限管理 | ⭐⭐ | chmod、chown | 会用 |
| 进程管理 | ⭐⭐ | ps、top、kill | 会用 |
| 网络 | ⭐⭐ | netstat、ss、curl、wget | 会用 |
| 文本处理 | ⭐⭐ | grep、awk、sed | 会用 |
| SSH | ⭐⭐⭐ | ssh、scp | 熟练 |
| 压缩解压 | ⭐⭐ | tar、zip、unzip | 会用 |
| 环境变量 | ⭐⭐⭐ | export、.bashrc、PATH | 熟练 |
| 系统信息 | ⭐ | df、du、free、uname | 了解 |

### 10.2 部署FastAPI

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| Gunicorn | ⭐⭐⭐ | 安装、配置、启动 | 熟练 |
| UvicornWorker | ⭐⭐⭐ | -k uvicorn.workers.UvicornWorker | 熟练 |
| Worker数量 | ⭐⭐ | -w 4、根据CPU核心数 | 会用 |
| 绑定地址 | ⭐⭐⭐ | --bind 0.0.0.0:8000 | 熟练 |
| 进程管理 | ⭐⭐ | 后台运行、重启 | 会用 |
| systemd服务 | ⭐⭐ | 编写service文件、开机自启 | 会用 |
| 进程守护 | ⭐⭐ | supervisor | 了解 |

### 10.3 Nginx

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 安装 | ⭐⭐⭐ | apt/yum install nginx | 熟练 |
| 配置文件结构 | ⭐⭐⭐ | /etc/nginx/nginx.conf、sites-available、sites-enabled | 理解 |
| 反向代理配置 | ⭐⭐⭐ | proxy_pass、proxy_set_header | 熟练 |
| 静态文件服务 | ⭐⭐ | root、alias、try_files | 会用 |
| 负载均衡 | 🔧 | upstream、多个后端 | 需要时学 |
| SSL/HTTPS | ⭐⭐ | Let's Encrypt、certbot | 会用 |
| 日志 | ⭐⭐ | access_log、error_log | 会用 |
| 重定向 | ⭐ | rewrite、return | 了解 |
| 限流 | 🔧 | limit_req_zone | 需要时学 |

### 10.4 环境与监控

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 环境变量管理 | ⭐⭐⭐ | .env文件、export、systemd Environment | 熟练 |
| 日志管理 | ⭐⭐ | 日志轮转、logrotate | 会用 |
| 健康检查 | ⭐⭐ | /health端点 | 会用 |
| 监控告警 | 🔧 | Prometheus、Grafana | 需要时学 |
| 错误追踪 | 🔧 | Sentry | 需要时学 |
| 备份恢复 | 🔧 | 数据库备份策略 | 需要时学 |

---

## 第十一阶段：版本控制（Git）

| 知识点 | 优先级 | 具体内容 | 掌握标准 |
|--------|--------|----------|----------|
| 仓库 | ⭐⭐⭐ | git init、git clone | 熟练 |
| 基本操作 | ⭐⭐⭐ | git add、git commit、git status、git log | 熟练 |
| 分支 | ⭐⭐⭐ | git branch、git checkout、git merge | 熟练 |
| 远程仓库 | ⭐⭐⭐ | git remote、git push、git pull | 熟练 |
| .gitignore | ⭐⭐⭐ | 忽略敏感文件、临时文件 | 熟练 |
| 冲突解决 | ⭐⭐ | 手动解决冲突 | 会用 |
| stash | ⭐ | git stash、git stash pop | 了解 |
| rebase | 🔧 | git rebase | 需要时学 |

---

## 第十二阶段：完整项目实战（2-3周）

综合运用以上所有知识，完成一个完整的项目。

### 推荐项目：博客系统

| 功能模块 | 涉及知识点 |
|----------|-----------|
| 用户注册登录 | JWT、密码哈希、依赖注入 |
| 用户个人主页 | 路径参数、查询参数、ORM查询 |
| 文章发布/编辑/删除 | CRUD、请求体校验、权限判断 |
| 文章列表（分页） | 分页、排序、ORM offset/limit |
| 文章评论 | 外键关联、关系查询 |
| 点赞功能 | 多对多关系、事务 |
| 搜索功能 | LIKE查询、全文搜索（可选） |
| 后台管理 | 中间件、权限控制 |
| 单元测试 | pytest、TestClient、依赖覆盖 |
| Docker部署 | Dockerfile、docker-compose |
| 生产部署 | Gunicorn + Nginx + PostgreSQL |

---

## 📋 总结表

| 阶段 | 内容 | 时间 | 优先级 |
|------|------|------|--------|
| 1 | Python基础 | 2-3周 | ⭐⭐⭐ |
| 2 | SQL基础 | 1周 | ⭐⭐⭐ |
| 3 | MySQL | 1周 | ⭐⭐⭐ |
| 4 | FastAPI | 2-3周 | ⭐⭐⭐ |
| 5 | SQLAlchemy | 1-2周 | ⭐⭐⭐ |
| 6 | 认证与安全 | 1周 | ⭐⭐⭐ |
| 7 | 测试 | 3-5天 | ⭐⭐⭐ |
| 8 | Docker | 1周 | ⭐⭐⭐ |
| 9 | 部署 | 1周 | ⭐⭐⭐ |
| 10 | Git | 2-3天 | ⭐⭐⭐ |
| 11 | 完整项目 | 2-3周 | ⭐⭐⭐ |
| - | Celery | - | 📅 以后学 |
| - | PostgreSQL高级 | - | 📅 以后学 |
| - | WebSocket | - | 📅 以后学 |
| - | GraphQL | - | 📅 以后学 |
| - | 监控告警 | - | 🔧 遇到再学 |
| - | Kubernetes | - | 🔧 遇到再学 |