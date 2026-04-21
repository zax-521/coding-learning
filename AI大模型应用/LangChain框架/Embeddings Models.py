# # 一、通过阿里云百炼调用
# from langchain_community.embeddings import DashScopeEmbeddings
#
# # 初始化嵌入模型对象，其默认使用模型是：text-embedding-v1
# embd = DashScopeEmbeddings()
#
# # 测试
# print(embd.embed_query("我喜欢你")) # 单次
# print(embd.embed_documents(["我喜欢你", "我喜欢您", "晚安"])) # 批量

# 二、本地Ollama模型访问
from langchain_ollama import OllamaEmbeddings

embed = OllamaEmbeddings(model="qllama/bge-small-zh-v1.5:q4_k_m")
print(embed.embed_query("我喜欢你")) # 单次
print(embed.embed_documents(["我喜欢你", "我喜欢您", "晚安"])) # 批量