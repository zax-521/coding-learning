"""
    跨域资源共享CORS：
        跨域资源共享（CORS）：是一种浏览器安全机制，用于允许允许在一个源（Origin）的Web应用，
            通过浏览器向另一个源的服务器发起跨域 HTTP 请求，并在服务器授权的前提下获取资源。
            注：浏览器的安全机制，只允许同源请求，不同源的访问会被浏览器拦截
        同源的三个条件：
            1.协议；2.域名；3.端口
            实例：         前端                   后端                 是否跨域
                http://localhost:5713   http://localhost:8000         跨域，端口不一致
                https://example.com      https://api.example.com        跨域，域名不一致
                https://example.com      https://example.com            不跨域
            注：在web浏览器的眼中 localhost 和 127.0.0.1 是不同域的
    解决跨域问题
        全局配置 CORS 中间件：
            CORS：让后端主动告诉浏览器：这个前那段"允许访问"，fastapi内置CORS
            在main.py中添加中间件
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许的来源（可以是域名列表）
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://example.com",
]

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"], # 允许所有源（仅开发环境，正常写项目要写origins列表）
    allow_credentials=True, # 允许携带Cookie
    allow_methods=["*"], # 允许所有请求方式
    allow_headers=["*"] # 允许所有请求头
)

