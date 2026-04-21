# # 一、LangChain访问阿里云通义千问大模型
# # langchain_community
# from langchain_community.llms.tongyi import Tongyi
#
# # 不用qwen3-max，因为qwen3-max是聊天模型，qwen-max是大语言模型
# model = Tongyi(model="qwen-max")
#
# # 调用invoke向模型提问
# # res = model.invoke(input="你是谁？") # invoke方法：一次性返回完整结果
# res = model.stream(input"你是谁？") # stream方法：逐段返回结果，流式输出
# print(res)
# for chunk in res:
#     print(chunk, end="", flush=True) # flush=True立刻刷新缓冲区

# # 二、访问Ollama本地模型
# from langchain_ollama import OllamaLLM
#
# model = OllamaLLM(model="qwen2.5:0.5b")
# # res = model.invoke(input="你是谁？你能干什么？")
# res = model.stream(input"你是谁？你有什么功能？")
# print(res)
# for chunk in res:
#     print(chunk, end="", flush=True) # flush=True立刻刷新缓冲区