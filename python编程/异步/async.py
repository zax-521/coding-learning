# # 同步阻塞
# # import time
# #
# # def boil_water():
# #     print("开始烧水...")
# #     time.sleep(3) # 模拟烧水要等三秒
# #     print("水烧开了")
# #
# # def wash_veggies():
# #     print("开始洗菜...")
# #     time.sleep(2) # 模拟洗菜要等两秒
# #     print("菜洗好了！")
# #
# # def cook():
# #     start = time.time()
# #     boil_water()
# #     wash_veggies()
# #     print(f"总耗时：{time.time() - start:.2f} 秒")
# #
# # cook()
#
# import asyncio
# import time
#
# # async def - 协程函数
# async def boil_water1():
#     print("开始烧水1...")
#     # 把time.sleep 换成 asyncio.sleep —— 这是告诉python：我可以去干别的事
#     await asyncio.sleep(3)
#     print("水烧开了1")
#
# async def wash_veggies1():
#     print("开始洗菜1")
#     await asyncio.sleep(2)
#     print("菜洗好了1！")
#
# # 主函数也得是async def
# async def cook1():
#     start = time.time()
#     # 关键一步：用 asyncio.gather 把两个任务[同时]启动
#     await asyncio.gather(
#         boil_water1(),
#         wash_veggies1()
#     )
#     print(f"总耗时1：{time.time() - start:.2f} 秒")
#
# async def cook2():
#     start = time.time()
#
#     # 创建一个后台任务 —— 我不等它，直接往下走
#     background = asyncio.create_task(boil_water1())
#
#     print("水已经开始烧了，我先去洗菜...")
#     await wash_veggies1() # 我只等洗菜，不等烧水
#
#     #菜洗完了，等我看一眼水烧好没，如果没好，在这里等以下
#     await background
#     print(f"总耗时2：{time.time() - start:.2f} 秒")
#
# # 启动入口：asyncio.run()
# # asyncio.run(cook1())
# asyncio.run(cook2())

import asyncio

# 1. 定义一个[异步上下文管理器]类
class AsyncDatabase:
    def __init__(self, name):
        self.name = name

    # 2. __aenter__ 是进入 async with 块时执行的
    async def __aenter__(self):
        print(f"[{self.name}] 正在连接数据库...")
        await asyncio.sleep(1) # 模拟网路连接耗时
        print(f"[{self.name}] 连接成功！")
        return self # 这个值会赋给 as 后面的变量

    # 3. __aexit__ 是退出 async with 块时执行的
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"[{self.name}] 正在关闭连接...")
        await asyncio.sleep(0.5) # 模拟关闭耗时
        print(f"[{self.name}] 连接已关闭。")

    # 4. 一个普通异步方法
    async def query(self, sql):
        print(f"[{self.name}] 执行查询：{sql}]")
        await asyncio.sleep(0.5)
        return f"结果集-{sql}"

# 5. 使用async with
async def main():
    print("=== 开始 ===")

    # 关键：async with 会自动调用 __aenter__ 和 __aexit__
    async with AsyncDatabase("主数据库") as db:
        result = await db.query("SELECT * FROM users")
        print(f"查询结果：{result}")

    print("=== 结束（连接已自动关闭） ===")

asyncio.run(main())

