"""
    HTTP 方法使用场景：
        方法           用途              特点	                         示例
        GET	        获取数据	     参数在URL、可缓存、不改变数据	    查询图书列表、获取详情
        POST	    创建数据	     参数在Body、不可缓存、会改变数据	    添加新图书、注册用户
        PUT	        完整更新	     替换整个资源、幂等	                更新图书所有字段
        PATCH	    部分更新	     只改部分字段、幂等	                只修改图书价格
        DELETE	    删除数据	     删除资源、幂等	                删除图书

"""

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

"""
    路由：路由是URL地址和处理函数之间的映射关系
"""
@app.get("/") # 装饰器 app：FastAPI实例对象; get：请求方法; ("/")：请求路径; return：响应结果;
async def root():
    return {"message": "Hello FastAPI!"}

@app.get("/user/hello")
async def hello():
    return {"msg": "我正在学习FastAPI......"}


"""
FastAPI允许为参数声明额外的信息和校验
    一、路径参数 —— Path
        位置： URL路径的一部分 例： /book/{id}
        作用：指向唯一的、特定的资源
        方法：GET
        
        Python原生注解 和 Path注解：
        id: int = Path(...,gt=1, lt=101, description="书籍id，范围1-100")
            Python原生注解： id: int
            Path注解：Path(...,gt=1, lt=101, description="书籍id，范围1-100")
"""
@app.get("/book/{id}")
async def get_book(id: int = Path(..., ge=1, le=100, description="书籍id，范围1-100")):
    return {"id": id, "title": f"这是第{id}本书"}

@app.get("/user/{id},{name}")
async def get_user(id: int, name: str):
    return {"id": id, "name": name}

@app.get("/author/{name}")
async def get_name(name: str = Path(..., min_length=2, max_length=10)):
    return {"msg": f"这是{name}的信息"}

@app.get("/news/category/{category_id}")
async def get_news_id(
        category_id: int = Path(
            ...,
            ge=1,
            le=100,
            title="新闻分类ID",
            description="分类ID的范围为1~100"
        )
):
    return {"category_id": category_id,
        "msg": f"获取id为{category_id}的新闻分类成功"}

@app.get("/news/category/name/{category_name}")
async def get_news_name(
        category_name: str = Path(
            ...,
            min_length=2,
            max_length=10,
            title="新闻分类名称",
            description="分类名称长度为2~10"
        )
):
    return {"category_name" : category_name,
            "msg": f"获取名称为{category_name}的新闻分类成功"}

"""
声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数
    二、查询参数 —— Query
        位置：URL ?之后 k1=v1&k2=v2
        作用：对资源集合进行过滤、排序、分页等操作
        方法：GET
    
    Request URL: http://127.0.0.1:8001/news/news_list?skip=0&limit=10
"""

# 需求：查询新闻 → 分页，skip：跳过的记录数， limit：返回的记录数 10
@app.get("/news/news_list")
async def get_news_list(
        skip: int = Query(0, description="跳过的记录数", le=100),
        limit: int = Query(10, description="返回的记录数"),
):
    return {"skip": skip, "limit": limit}

@app.get("/books")
async def get_books(
        category: str = Query(
            "Python开发",
            min_length=5,
            max_length=255,
            title="图书分类",
            description="图书分类名称，长度为5~255，默认值为Python开发"
        ),
        price: int = Query(
            ge=50,
            le=100,
            title="图书价格",
            description="图书价格，范围为50~100"
        )
):
    return {
        "category": category,
        "price": price,
        "message": f"查询分类为【{category}】，价格范围在【{price}】范围内的图书成功]"
    }


"""
在HTTP协议中，一个完整的请求由三部分组成：
    1.请求行：包含方法、URL、协议版本
    2.请求头：元数据信息（Content-Type、Authorization等）
    3.请求体：实际要发送的数据内容

    三、请求体 —— BaseModel + Field
        位置：HTTP请求的消息体(body)中
        作用：创建、更新资源、携带大量数据，如：JSON
        方法：POST、PUT等
    
    请求体参数：
        1.定义类型：
            from pydantic import BaseModel
            class User(BaseModel):
                username: str
                password: str
        2.类型注解：
            @app.post("/register")
            async def register(user: User):
                return user
                
        消息体(body)：
            curl -X 'POST' \
            'http://127.0.0.1:8001/register' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
            "username": "admin",
            "password": "admin123"
        }'
"""

# 注册：用户名和密码 → str
class User(BaseModel):
    username: str = Field(default="张三", min_length=2, max_length=10, description="用户名：长度为2~10个字")
    password: str = Field(min_length=6, max_length=20, description="密码：长度为6~20")

@app.post("/register")
async def register(user: User):
    return user

class Book(BaseModel):
    title: str = Field(min_length=2, max_length=20, title="书名", description="书名长度范围为：2~20") # 书名
    author: str = Field(min_length=2, max_length=20, title="作者", description="作者长度范围为：2~20") # 作者
    publisher: str = Field(default="北京大学出版社", title="出版社") # 出版社
    price: int = Field(gt=0, title="售价", description="不能为空，价格要大于0元") # 售价

@app.post("/books/add")
async def add_book(book: Book):
    return book

"""
    四、响应类型
        JSONResponse        默认响应，返回JSON数据       return {"key": "value"}
        HTMLResponse        返回HTML内容               return HTMLResponse(html_content)
        PlainTextResponse   返回纯文本                  return PlainTextResponse("text")
        FileResponse        返回文件下载                return FileResponse(path)
        StreamingResponse   流式响应                   生成器函数返回数据
        RedirectResponse    重定向                     return RedirectResponse(url)
    
    响应类型设置方式
        装饰器中指定响应类：
            场景：固定返回类型(HTML，纯文本等)
            from fastapi.responses import HTMLResponse
            @app.get("/html", response_class=HTMLResponse)
            async def get_html():
                return "<h1>标题</h1>"
            
        返回响应对象：
            场景：文件下载、图片、流式响应
            from fastapi.responses import FileResponse
            @app.get("/file")
            async def get_file():
                file_path = "路径"
                return FileResponse(file_path)
        
    自定义响应数据格式：
        from pydantic import BaseModel
        
        class News(BaseModel):
        id: int
        title: str
        content: str
    
        @app.get("/news/{id}", response_model=News)
        async def get(id: int):
            return {
                "id": id,
                "title": f"第{id}页新闻",
                "content": "这是当天新闻"
            }
"""

# 接口 → 响应 HTML 代码
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>标题</h1>"

# 接口：返回一张图片内容
@app.get("/file")
async def get_file():
    file_path = "../files/img.png"
    return FileResponse(file_path)

# 自定义响应格式
class News(BaseModel):
    id: int
    title: str
    content: str

# 需求：新闻接口 → 响应数据格式：id、title、content
@app.get("/news/{id}", response_model=News)
async def get(id: int):
    return {
        "id": id,
        "title": f"第{id}页新闻",
        "content": "这是当天新闻"
    }

"""
    五、异常处理
        对于客户端引发的错误，使用fastapi.HTTPException来中断正常处理流程，并返回标准错误响应。
        from fastapi import FastAPI, HTTPException
        @app.get('/school/{id}')
        async def get_school(id: int):
            id_list = [1, 2, 3, 4, 5, 6]
            if id not in id_list:
                raise HTTPException(status_code=404, detail="当前id不存在")
            return {"id": id}
"""
# 需求：按 id 查询新闻 → 1 - 6
@app.get("/school/{id}")
async def get_school(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="当前id不存在")
    return {"id": id}