# # 方法一，调用阿里云百炼大模型api(常用)
# import os
# from openai import OpenAI
#
# client = OpenAI(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )
#
# completion = client.chat.completions.create(
#     # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
#     model="qwen-max",
#     messages= [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你是谁？"},
#     ],
#     stream=True
# )
# for chunk in completion:
#     print(chunk.choices[0].delta.content, end="", flush=True)

# # 方法二：通过Ollama部署本地大模型，调用本地大模型(备选)
# from openai import OpenAI
#
# client = OpenAI(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
#     api_key="ollama",
#     base_url="http://localhost:11434/v1",
# )
#
# completion = client.chat.completions.create(
#     # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
#     model="qwen2.5:0.5b",
#     messages= [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你是谁？"},
#     ],
#     stream=True
# )
# for chunk in completion:
#     print(chunk.choices[0].delta.content, end="", flush=True)