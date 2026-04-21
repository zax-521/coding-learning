"""
    一、ORM（Object-Relational Mapping，对象关系映射）
        定义：ORM是一种编程技术，用于在面向对象编程语言和关系型数据库之间建立映射。
            它允许开发者通过操作对象的方式与数据库进行交互，而无需直接编写复杂的SQL语句

        优势：
            1.减少重复的SQL代码
            2.代码更简洁易读
            3.自动处理数据库连接和事务
            4.自动防止SQL注入攻击

        创建ORM流程：
            1.创建数据库引擎
                # 1.导入异步引擎
                from sqlalchemy.ext.asyncio import create_async_engine
                # 2.数据库连接字符串
                ASYNC_DATABASE_SQL = "mysql+aiomysql://{user}:{password}@{host}:{port}/{database}?charset={charset}"
                # 3.创建异步引擎
                async_engine = create_async_engine(
                    ASYNC_DATABASE_SQL,
                    echo=True, # 可选，输出 SQL 日志
                    pool_size=10, # 连接池中常驻的连接数量
                    max_overflow=20 # 最多额外创建的连接数
                )

            2.ORM - 定义模型类：基类 + 表对应的模型类
                # 1.基类，继承DeclarativeBase（包含通用属性和字段的映射）
                from sqlalchemy import DateTime, func
                from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
                from datetime import datetime
                class Base(DeclarativeBase):
                    create_time: Mapped[datetime] = mapped_column(DateTime,
                        insert_default=func.now(), default=func.now, comment="创建时间")

                    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(),
                        onupdate=func.now(), default=func.now, comment="修改时间")
                # 2.定义数据库对应的模型类
                from sqlalchemy import String, Float
                class Book(Base):
                    __tablename__ = "book"

                    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
                    book_name: Mapped[str] = mapped_column(String(255), comment="书名")
                    author: Mapped[str] = mapped_column(String(255), comment="作者")
                    price: Mapped[float] = mapped_column(Float, comment="价格")
                    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")

            3.创建数据库表
                # 1.从连接池获取异步连接，开启事务，执行ORM操作
                async def create_tables():
                    # async with：异步上下文管理器，自动管理资源；
                    # async_engine.begin()：开启一个数据库事务；as conn：获取数据库连接对象
                    async with async_engine.begin() as conn:
                        #  conn.run_sync()：在同步环境中运行异步代码(SQLAlchemy的同步方法)；
                        # Base.metadata：所有继承Base的模型类的元数据集合；create_all：创建所有未创建的表
                        await conn.run_sync(Base.metadata.create_all)
                # 2.FastAPI应用启动时，创建数据库表
                from contextlib import asynccontextmanager
                @asynccontextmanager # 创建异步上下文管理器，用于FastAPI生命周期管理
                async def lifespan(app: FastAPI):   # 执行 lifespan 函数
                    await create_tables()           #   → await create_tables()
                    yield                           #   → 检查数据库有没有 book 表
                                                    #   → 没有就创建
                app = FastAPI(lifespan=lifespan)    #   → 有就跳过
    二、ORM的使用：
        1. 路由匹配中使用ORM：
            核心：创建 依赖项，使用 Depends 注入到处理函数中；
            流程：
                # 1.创建异步会话工厂
                from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
                AsyncSessionLocal = async_sessionmaker(
                    bind=async_engine, # 绑定数据库引擎
                    class_= AsyncSession, # 指定会话类
                    expire_on_commit=False # 提交后会话不过期，不会重新查询数据库
                )
                # 2.依赖项，用于获取数据库会话
                # 创建依赖项
                from fastapi import Depends
                async def get_database():
                    async with AsyncSessionLocal() as session:
                        try:
                            yield session # 返回数据库会话给路由处理函数
                            await session.commit() # 提交事务
                        except Exception:
                            await session.rollback() # 有异常回滚
                            raise
                        finally:
                            await session.close() # 关闭会话
                # 将依赖注入到路由处理函数
                @app.get("/book/books")
                async def get_book_list(db: AsyncSession = Depends(get_database)):
                    # 查询
                    result = await db.execute(select(Book))
                    book = result.scalars().all()
                    return book
        2。数据库操作：
            1.查询：
                核心语句：await db.execute(select(模型类))，返回一个ORM对象
                # 1.获取所有数据：
                    ORM对象.scalars().all()

                # 2.获取单挑数据：
                    ORM对象.scalars().first()
                    数据库会话.get(模型类, 主键值)

            2.查询条件：
                核心语句：await db.execute(select(模型类).where(条件1, 条件2, ...))
                条件：
                    比较判断：==、>、<、>=、<=等
                        result = await db.execute(select(Book).where(Book.id == book_id))

                    模糊查询：like()：%：任意字符；_:单个字符
                        result = await db.execute(select(Book).where(Book.author.like("曹_")))
                        result = await db.execute(select(Book).where(Book.author.like("曹%")))

                    与非查询：与：and_、&；非：or_、|；取反：not_、~
                        result = await db.execute(select(Book).where(and_(Book.author.like("曹%"), Book.price > 80)))
                        result = await db.execute(select(Book).where(or_(Book.author.like("曹%"), Book.price > 80)))
                        result = await db.execute(select(Book).where(not_(Book.author.like("曹%"))))

                    包含查询：in_()：包含
                        id_list = [1, 3, 5]
                        result = await db.execute(select(Book).where(Book.id.in_(id_list)))
            3.聚合查询：
                聚合计算：func.方法(模型类.属性) num = result.scalar() # 用来提取一个数值 → 标量值
                count：统计行数量 → result = await db.execute(select(func.count(Book.id)))
                avg：求平均值 → result = await db.execute(select(func.avg(Book.price)))
                max：求最大值 → result = await db.execute(select(func.max(Book.price)))
                min：求最小值 → result = await db.execute(select(func.min(Book.price)))
                sum：求和 → result = await db.execute(select(func.sum(Book.price)))

            4.分页查询：
                select().offset().limit()
                offset：跳过的记录数 offset 值 = (当前页码 - 1) * 每页数量 limit;
                limit：返回的记录数
                @app.get("/book/page")
                async def get_books_pagination(
                        page: int = 1, # 页码
                        page_size: int = 10, # 每页数量
                        db: AsyncSession = Depends(get_database)
                ):
                    skip = (page - 1) * page_size
                    # offset：跳过的记录数； limit：每页的记录数
                    stmt = select(Book).offset(skip).limit(page_size)
                    result = await db.execute(stmt)
                    books = result.scalars().all()
                    return books

            5.新增
                核心步骤：定义ORM对象 → 添加对象到事务：add(对象) → commit 提交到数据库
                    # 添加 用book.__dict__将book请求体对象转换成dict字典，
                        再用**book.__dict__将字典展开获取所有键值对，
                        再用Book(**book.__dict__)模型类转换成ORM对象
                    # 需求：用户输入图书信息（id、书名、作者、价格、出版社） → 新增
                    # 用户输入 → 参数 → 请求体
                    # 创建请求体类
                    class BookBase(BaseModel):
                        id: int
                        book_name: str
                        author: str
                        price: float
                        publisher: str

                    @app.post("/book/add_book")
                    async def add_book(book: BookBase, db: AsyncSession = Depends(get_database)):
                       # ORM对象 → add → commit
                       book_obj = Book(**book.__dict__)
                       db.add(book_obj) # 将ORM对象添加到事务
                       await db.commit() # 提交到数据库
                       return book

            6.修改(更新)：先查再改 (重新赋值)
                核心步骤：查询 get → 属性重新赋值 → commit 提交到数据库
                # 需求：修改图书信息：先查再改
                # 设计思路：路径参数书籍id：作用是查找；请求体参数：作用是新数据（书名、作者、价格、出版社）
                class BookUpdate(BaseModel):
                    book_name: str
                    author: str
                    price: float
                    publisher: str

                @app.put("book/update_book/{book_id}")
                async def update_book(book_id: int, data: BookUpdate,db: AsyncSession = Depends(get_database)):
                    # 1.查找图书
                    db_book = await db.get(Book, book_id)
                    # 如果未找到：抛出异常
                    if db_book is None:
                        raise HTTPException(
                            status_code=404,
                            detail="查无此书"
                        )
                    # 2.找到则修改：重新赋值
                    db_book.book_name = data.book_name
                    db_book.author = data.author
                    db_book.price = data.price
                    db_book.publisher = data.publisher
                    # 3.提交到数据库
                    await db.commit()
                    return db_book

            7.删除：先查后删
                核心步骤：查询 get → delete 删除 → commit 提交到数据库
                @app.delete("/book/detele_book/{book_id}")
                async def delete_book(book_id: int, db: AsyncSession = Depends(get_database)):
                    # 1.查询图书
                    db_book = await db.get(Book, book_id)
                    # 如果未找到：抛出异常
                    if db_book is None:
                        raise HTTPException(
                            status_code=404,
                            detail="查无此书"
                        )
                    # 2.删除图书
                    await db.delete(db_book)
                    # 3.提交到数据库
                    await db.commit()
                    return {"要删除的书籍信息": "{db_book}", "msg": "删除书籍成功"}
"""

from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import DateTime, func, String, Float, select, and_, or_, not_
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel

from dotenv import load_dotenv
import os

load_dotenv()

# 1.创建数据库引擎
ASYNC_DATABASE_URL = os.getenv("DATABASE_URL")
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True, # 可选，输出 SQL 日志
    pool_size=10, # 设置连接池活跃的连接数
    max_overflow=20 # 允许额外的连接数
)

# 2.定义模块类：基类 + 表对应的模型类
# 基类：创建时间、更新时间
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now, comment="创建时间"
    )
    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        onupdate=func.now(),
        default=func.now,
        comment="修改时间"
    )

# 书籍表：id、书名、作者、价格、出版社
class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
    book_name: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price:Mapped[float] = mapped_column(Float, comment="价格")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")

# 3. 建表：定义函数建表 → FastAPI启动的时候调用建表的函数
# 定义函数建表
async def create_tables():
    # 获取异步引擎，创建事务：建表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # Base 模型类的元数据创建

# FastAPI启动的时候调用建表的函数
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


# 需求：查询功能的接口，查询图书 → 依赖注入：创建依赖项获取数据库会话 + Depends 注入路由处理函数
# 创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, # 绑定数据库引擎
    class_= AsyncSession, # 指定会话类
    expire_on_commit=False # 提交后会话不过期，不会重新查询数据库
)

# 创建依赖项
async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session # 返回数据库会话给路由处理函数
            await session.commit() # 提交事务
        except Exception:
            await session.rollback() # 有异常回滚
            raise
        finally:
            await session.close() # 关闭会话

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 将依赖注入到路由处理函数
@app.get("/books/")
async def get_all_books(db: AsyncSession = Depends(get_database)):
    # 查询
    result = await db.execute(select(Book)) # 查询 → 返回一个 ORM 对象
    book = result.scalars().all() # 获取所有
    # book = result.scalars().first() # 获取第一条数据
    # book = await db.get(Book, 5) # 获取单条数据 → 根据主键
    return book

# 需求：路径参数 书籍id
@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int, db: AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none() # 提取一个或者null，返回多个是报错
    return book

# 需求：条件：价格大于 80
@app.get("/book/price-gt-80")
async def get_books_price_gt_80(db: AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.price > 80))
    book = result.scalars().all()
    return book

@app.get("/books/search/author")
async def search_books_by_name(db: AsyncSession = Depends(get_database)):
    # like() 模糊查询： % _
    # result = await db.execute(select(Book).where(Book.author.like("曹_")))
    # result = await db.execute(select(Book).where(Book.author.like("曹%")))

    # 与：and、&；非：or_、|；取反：not_、~
    # result = await db.execute(select(Book).where(and_(Book.author.like("曹%"), Book.price > 80)))
    # result = await db.execute(select(Book).where(or_(Book.author.like("曹%"), Book.price > 80)))
    result = await db.execute(select(Book).where(not_(Book.author.like("曹%"))))
    book = result.scalars().all()
    return book

# 需求：书籍id列表，数据库里面的 id 如果在 书籍id列表里面 就返回
@app.get("/book/search/id_list")
async def search_books_by_id_list(db: AsyncSession = Depends(get_database)):
    id_list = [1, 3, 5]
    # in_() 包含
    result = await db.execute(select(Book).where(Book.id.in_(id_list)))
    book = result.scalars().all()
    return book

# 集合查询 select(func.方法名(模型类.属性))
@app.get("/books/stats/aggregation")
async def get_book_aggregation(db: AsyncSession = Depends(get_database)):
    # result = await db.execute(select(func.count(Book.id)))
    # result = await db.execute(select(func.avg(Book.price)))
    # result = await db.execute(select(func.max(Book.price)))
    # result = await db.execute(select(func.min(Book.price)))
    result = await db.execute(select(func.sum(Book.price)))
    num = result.scalar() # 用来提取一个数值 → 标量值
    return num

# 分页查询
@app.get("/book/page")
async def get_books_pagination(
        page: int = 1, # 页码
        page_size: int = 10, # 每页数量
        db: AsyncSession = Depends(get_database)
):
    skip = (page - 1) * page_size
    # offset：跳过的记录数； limit：每页的记录数
    stmt = select(Book).offset(skip).limit(page_size)
    result = await db.execute(stmt)
    books = result.scalars().all()
    return books

# 添加 将book对象转换成dict字典，再将字典展开获取所有键值对，再用模型类转换成ORM对象
# 需求：用户输入图书信息（id、书名、作者、价格、出版社） → 新增
# 用户输入 → 参数 → 请求体
class BookBase(BaseModel):
    id: int
    book_name: str
    author: str
    price: float
    publisher: str

@app.post("/book/add_book")
async def add_book(book: BookBase, db: AsyncSession = Depends(get_database)):
   # ORM对象 → add → commit
   book_obj = Book(**book.__dict__)
   db.add(book_obj)
   await db.commit()
   return book

# 需求：修改图书信息：先查再改
# 设计思路：路径参数书籍id：作用是查找；请求体参数：作用是新数据（书名、作者、价格、出版社）
class BookUpdate(BaseModel):
    book_name: str
    author: str
    price: float
    publisher: str

@app.put("/book/update_book/{book_id}")
async def update_book(book_id: int, data: BookUpdate,db: AsyncSession = Depends(get_database)):
    # 1.查找图书
    db_book = await db.get(Book, book_id)

    # 如果未找到：抛出异常
    if db_book is None:
        raise HTTPException(
            status_code=404,
            detail="查无此书"
        )

    # 2.找到则修改：重新赋值
    db_book.book_name = data.book_name
    db_book.author = data.author
    db_book.price = data.price
    db_book.publisher = data.publisher

    # 3.提交到数据库
    await db.commit()
    return db_book

@app.delete("/book/detele_book/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_database)):
    # 1.查询图书
    db_book = await db.get(Book, book_id)
    # 如果未找到：抛出异常
    if db_book is None:
        raise HTTPException(
            status_code=404,
            detail="查无此书"
        )
    # 2.删除图书
    await db.delete(db_book)
    # 3.提交到数据库
    await db.commit()
    return {"要删除的书籍信息": "{db_book}", "msg": "删除书籍成功"}
