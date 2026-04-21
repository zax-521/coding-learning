"""
    如果想在链中加入自定义函数：
        1.将函数封装入RunnableLambda类对象，其是Runnable接口实例，可以直接入链
            my_func = RunnableLambda(lambda ai_msg: {"name" : ai_msg.content})
            ai_msg：上一个模型提供的返回值
        2.直接将函数入链，函数会自动转换为RunnableLambda对象
            | lambda ai_msg: {"name" : ai_msg.content} |
"""

from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.base import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

str_parser = StrOutputParser()

model = ChatTongyi(model="qwen3-max")

# 第一个提示词模板
first_prompt =PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，帮忙起个名字，他希望文字能含有诗意"
    "输出为Json格式,key是name，value是你生成的名字"
)
second_prompt =PromptTemplate.from_template(
    "姓名：{name}，帮我解析一下"
)
# 方法一：将函数封装进RunnableLambda的类对象
# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})
# chain = first_prompt | model | my_func | second_prompt | model | str_parser

# 方法二：直接将函数写入chain链中，chain链会自动将函数自动转化为RunnableLambda对象
chain = first_prompt | model | (lambda ai_msg : {"name" : ai_msg.content}) | second_prompt | model | str_parser

for chunk in chain.stream({"lastname":"何", "gender":"女孩"}):
    print(chunk, end="", flush=True)