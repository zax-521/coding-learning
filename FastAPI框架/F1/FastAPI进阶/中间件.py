"""
    FastAPI进阶(Middleware)：中间件是一个在每次请求进入FastAPI应用时都会被执行的函数。
        它在请求到达实际路径操作(路由处理函数)之前运行，并且在响应返回给客户端之前再运行一次。

    中间件的作用：为每个请求添加统一的处理逻辑(记录日志、身份认证、跨域、设置响应头、性能监控等)
        注：中间件控制所以请求

    中间件的执行顺序：按代码顺序自下而上

    中间件的使用方式：函数顶部使用装饰器@app.middleware("http")
        request：请求
        call_next：传递请求给路径处理函数
        response：响应
        中间件执行顺序：中间件2开始 → 中间件1开始 → 中间件1结束 → 中间件2结束
        @app.middleware("http")
        async def middleware(request, call_next)
            print("中间件1开始处理 -- start")
            response = await call_next(request) # 向下传递请求
            print("中间件1处理完成 -- end")
            return response

        @app.middleware("http")
        async def middleware2(request, call_next):
            print("中间件2开始处理 -- start")
            response = await call_next(request)
            print("中间件2处理完成 -- end")
            return response
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.middleware("http")
async def middleware1(request, call_next):
    print("中间件1开始处理 -- start")
    response = await call_next(request)
    print("中间件1处理完成 -- end")
    return response

@app.middleware("http")
async def middleware2(request, call_next):
    print("中间件2开始处理 -- start")
    response = await call_next(request)
    print("中间件2处理完成 -- end")
    return response