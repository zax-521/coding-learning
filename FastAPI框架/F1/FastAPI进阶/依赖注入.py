"""
    依赖注入：
        依赖项：可以重复使用的组件(函数/类)，负责提供某种功能或者数据

        注入：FastAPI自动帮你调用依赖项，并将结果"注入"到路径操作函数中

        使用方式：
            创建依赖项：
                async def common_parameters(
                    skip: int = Query(0, ge=0)
                    limit: int = Query(10, le=60)
                ):
                    return {
                        "skip": skip,
                        "limit": limit
                    }

            导入 Depends：
                from fastapi import Depends

            声明依赖项：
                @app.get("/news/news_list")
                async def get_news_list(
                    commons = Depends(common_parameters)
                ):
                    return commons

        作用：使用依赖注入系统来共享通用逻辑，减少代码重复

        应用场景：
            处理请求参数：从请求中提取和验证参数(路径参数、查询参数、请求体)
            共享数据库连接：管理数据库会话的创建、使用、关闭
            共享业务逻辑：抽取封装多个路由公用的逻辑代码
            安全和认证：验证用户身份、检查权限和角色要求等

        注：依赖注入是自定义注入给谁

"""
from fastapi import FastAPI, Query, Depends


app = FastAPI()

# 三个路由都需要实现分页功能，我们可以直接注入依赖
# @app.get("/news/news_list")
# async def get_news_list(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, le=60)
# ):
#     # 分页逻辑...
#     return {"list": "新闻列表"}
#
# @app.get("/users/user_list")
# async def get_user_list(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, le=60)
# ):
#     # 分页逻辑...
#     return {"list": "用户列表"}
#
# @app.get("/news/category")
# async def get_news_category(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, le=60)
# ):
#     # 分页逻辑...
#     return {"category": "新闻分类"}

async def common_parameters(
    skip: int = Query(0, ge=0),
    limit:int = Query(10, le=60)
):
    return {
        "skip": skip,
        "limit": limit
    }

@app.get("/news/news_list")
async def get_news_list(
    commons = Depends(common_parameters)
):
    return commons

@app.get("/users/user_list")
async def get_user_list(
    commons = Depends(common_parameters)
):
    return commons

@app.get("/news/category")
async def get_news_category(
    commons = Depends(common_parameters)
):
    return commons