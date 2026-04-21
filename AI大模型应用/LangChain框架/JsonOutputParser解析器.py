"""
    invoke|stream 初始输入-->提示词模板-->模型-->数据处理-->提示词模板-->模型-->解析器-->结果
    其中数据处理-->提示词模板：将模型输出的AIMessage-->转换为字典-->注入第二个提示词模板中，形成新的提示词(PromptValue对象)
    JsonOutputParser：将AIMessage转换为字典
"""
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

# 创建解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model="qwen3-max")

# 第一个提示词模板
first_prompt =PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，帮忙起个名字，他希望女儿能够快快乐乐的生活"
    "输出为Json格式,key是name，value是你生成的名字"
)
second_prompt =PromptTemplate.from_template(
    "姓名：{name}，帮我解析一下"
)

chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# res = chain.invoke({"lastname": "朱", "gender": "女儿"})
#
# print(res,type(res))

for chunk in chain.stream({"lastname": "朱", "gender": "女儿"}):
    print(chunk, end='', flush=True) # flush=True立刻刷新缓冲区