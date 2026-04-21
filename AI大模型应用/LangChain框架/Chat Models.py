# # 一、演示单独使用HumanMessage
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import HumanMessage
#
# # 初始化模型
# chat =ChatTongyi(model="qwen3-max")
#
# # 准备消息list
# messages = [
#     HumanMessage(content="给我来个冷笑话"),
# ]
#
# #流式输出
# for chunk in chat.stream(input=messages):
#     print(chunk.content, end='', flush=True)

# # 二、演示SystemMessage + HumanMessage
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import SystemMessage, HumanMessage
#
# # 初始化模型
# chat = ChatTongyi(model="qwen3-max")
#
# # 准备消息list
# messages = [
#     SystemMessage(content="你是一名刚到中国的外国人"),
#     HumanMessage(content="你需要去找食物")
# ]
#
# # 流式输出
# for chunk in chat.stream(messages):
#     print(chunk.content, end='', flush=True)

# # 三、演示SystemMessage + HumanMessage +AIMessage
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
#
# # 初始化模型
# chat = ChatTongyi(model='qwen3-max')
#
# # 准备消息list
# # 这种是静态的，一步到位直接就得到了Message类的类对象
# messages = [
#     SystemMessage(content="你是一名刚到中国的外国人"),
#     HumanMessage(content="你需要去找餐厅吃饭"),
#     AIMessage(content="我找到一家火锅店"),
#     HumanMessage(content="这家火锅店的味道怎么样？"),
# ]
#
# # 流式输出
# for chunk in chat.stream(input=messages):
#     print(chunk.content, end='', flush=True)

# # 简写形式
# from langchain_community.chat_models.tongyi import ChatTongyi
#
# # 初始化模型
# chat = ChatTongyi(model='qwen3-max')
#
# # 准备消息list
# # 简写形式，是动态的，需要在运行时，由LangChain内部机制转换为Message类对象
# messages = [
#     ("system", "你是一名刚到中国的外国人"),
#     ("human", "你需要去找餐厅吃饭"),
#     ("ai", "我找到一家火锅店"),
#     ("human", "这家火锅店的味道怎么样？"),
# ]
#
# # 流式输出
# for chunk in chat.stream(input=messages):
#     print(chunk.content, end='', flush=True)