"""
    一、缓存：高速的临时数据存储机制
        1. 数据缓存：
            缓存是一种存储机制，用于临时存储数据或计算结果，
                当再次需要这些数据时，可以快速从缓存中检索，而不是重新进行耗时或者昂贵的获取和计算过程。

            在网站开发中，缓存（Cache）是一个非常重要的概念，其核心作用是提高性能、降低延迟和减轻服务器负载。

        2. 具体流程：
            不加缓存的流程：
                用户/前端 → FastAPI服务器（业务逻辑控制中心） → 数据库
            加缓存的流程：
                用户/前端 → FastAPI服务器（业务逻辑控制中心） → 缓存 → 数据库
            注：必须遵循“先查缓存 → 没命中再查数据库 → 查完写回缓存 → 返回数据给前端”的顺序

        3. 为什么需要缓存：
            当用户量很大时，数据库（硬盘）会因扛不住高并发而变慢或崩溃，
                此时需要在中间加一层 Redis（内存）作为缓存来为数据库‘挡子弹’。

        4. 主要优势：
            1.提升性能和用户体验
            2.减轻服务器/数据库负载
            3.降低网络延迟
            4.节省资源和成本

    二、Redis：
        1. 定义：
            一种高性能的 Key—Value 存储系统，它将数据存储在内存种，
                因此读写速度极快，非常适合作为应用层的缓存服务。

            在FastAPI这样的后端框架中，通常在应用层使用像 Redis 这样的内存数据存储作为缓存。

        2. 使用流程：
            安装 Redis 服务端 → 配置 Redis 客户端 → 封装缓存操作 → 设计缓存策略
            1.安装 Redis 服务端：默认端口号：6379

            2.配置 Redis 客户端：
                1.安装 Redis 客户端：pip install redis
                2.配置 Redis 客户端：
                    import redis.asyncio as redis
                    redis.Redis(...)
                    host: Redis 服务器地址
                    port: 端口号 6379
                    db: 数据库编号（0 ~ 15）
                    decode_response: 是否将返回的数据从字节流解码为字符串

            3.封装缓存操作：缓存操作就是围绕 Redis 做“存、取、删、判断、过期”等操作，让数据访问更快、数据库压力更小。
                Redis存储数据：key - value
                           方法                   参数                              描述
                1.设置缓存：setex    key:str, expire:int(秒), value:str          设置缓存并指定过期时间（秒）
                2.获取缓存：get                  key: str                       获取缓存值。若缓存不存在，返回None
                3.删除缓存：delete               key: str                       删除指定的缓存键
                4.检查缓存：exists               key: str                       检查缓存键是否存在，返回布尔值

            4.设计缓存策略：
                最常见的策略 - 旁路策略（Cache—Aside）：是一种常见的缓存策略，其核心概念是应用程序主动管理缓存，
                    在读取数据时先检查缓存，如果缓存种没有数据，则从数据库或其他数据源加载数据，并将数据存入缓存，
                    当数据更新或删除时，应用程序也负责更新或删除缓存种的数据。
                    1.读：先查缓存，有数据则返回，没有数据则查讯数据库
                    2.写：更新数据库后，更新或删除缓存数据
                例子：
                    设计新闻列表：
                        缓存 Key（唯一）：带上news:list分类 ID页码:每页数量；要确保key唯一，所以我们需要设计缓存key
                        缓存 Value：新闻列表

        3. 实例：
        cache_conf.py:
            import redis.asyncio as redis

            REDIS_HOST = "localhost"
            REDIS_PORE = 6379
            REDIS_DB = 0

            # 创建 Redis 的连接对象
            redis_client = redis.Redis(
                host=REDIS_HOST, # Redis 服务器的主机地址
                port=REDIS_PORT, # Redis 端口号
                db=REDIS_DB, # Redis 数据库编号，0~15
                decode_responses=True # 是否将字节数据解码为字符串
            )

            # 设置 和 读取（字符串 和列表或字典）"[{}]"
            # 读取：字符串
            async def get_cache(key: str):
                try:
                    return await redis_client.get(key) # 根据key获取缓存
                except Exception as e:
                    print(f"获取缓存失败：{e}")
                    return None

            # 读取：列表或字典
            async def get_json_cache(key: str):
                try:
                    data = await redis_client.get(key)
                    if data:
                        return json.loads(data) # 序列化
                    return None
                except Exception as e:
                    print(f"获取 JSON 缓存失败：{e}")
                    return None

            # 设置缓存
            async def set_cache(key: str, value: Any, expire: int = 3600):
                try:
                    if isinstance(value, (dict, list)): # isinstance(a, b)判断a是不是b类型
                        # 转字符串再存
                        value = json.dumps(value, ensure_ascii=False)) # ensure_ascii是否转译，这里用False不转译，保留中文

                    await redis_client.setex(key, expire, value)
                    return True
                except Exception as e:
                    print(f"设置缓存失败：{e}")
                    return False
"""







