# 第一题
# instructions = """
# 1.只能用context的内容回答
# 2.不许编
# 3.不知道就说"未找到答案"
# """
#
# context = """
# 苹果的营养成分有维生素 A、维生素 C、膳食纤维。
# """
#
# query = """
# 苹果里有维生素 B 吗？
# """
#
# prompt = """
# ### 指令
# {instructions}
# ### 上下文
# {context}
# ### 问题
# {query}
# """

# 第二题
# instructions = """
# 1.回答必须分点(1. , 2. , 3.)
# 2.语言简洁
# 3.只根据上下文内容回答
# """
# context = """
# RAG分为文本切分、向量存储、检索、生成四个步骤
# """
# query = """
# RAG有哪几步？
# """
#
# prompt = """
# ### 要求
# {instructions}
# ### 上下文
# {context}
# ### 问题
# {query}
# """

# # 第三题
# instructions = """
# # 1.聊天时，要分析当时场景，对方的情绪，然后基于对方相适应的拟人化回答，
# # 2.简单易懂，如果用户没有限制，尽量用白话文，如果有，就用户需求来
# # 3.只看上下文内容，对用户进行回答
# # """
# context = """
# Agent 就是让 AI 自己判断该做什么，比如查天气、计算、调用工具。
# """
#
# query = """
# 什么是Agent
# """
# prompt = """
# ### 要求
# {instructions}
# ### 上下文
# {context}
# ### 问题
# {query}
# """

# # 第四题
# instructions = """
# 1.分析问题类型：知识类问题或者计算类问题
# 2.【知识类问题】return【knowledge】
# 3.【计算类问题】return【math】
# """
#
# query = """
# 问题1.123+456等于多少？
# 问题2.什么是RAG?
# """
#
# prompt= """
# ### 要求
# {instructions}
# ###问题
# {query}
# """

# # 第五题
# instructions = """
# 1.回答不要超过20个字
# 2.只根据上下文内容回答
# """
#
# context = """
# 大模型就是通过大量数据训练出来、能理解和生成文本的人工智能
# """
#
# query = """
# 什么是大模型？
# """
#
# prompt = """
# ### 要求
# {instructions}
# ### 上下文
# {context}
# ### 问题
# {query}
# """