"""
    一、获取客户端对象
        主要是用两个参数：
            1.api_key：模型服务商提供的APIKEY密钥
            2.base_url：模型服务商的API接入地址
                2.1 主要基于此参数来切换不同的模型服务商

    二、client.chat.completion创建ChatCompletion对象
        主要参数有两个:
            1.model：选择所用模型，如代码的qwen3—max
            2.messages：提供给模型的消息
                2.1 类型：list, 可以包含多个字典消息
                2.2 每个字典消息包含2个key
                    1.role：角色
                        1.1 system：设定助手的整体行为、角色和规则，为对话提供上下文框架(如指定助手身份、回答风格、核心要求)，是全局的背景设置，影响后续所有交互
                        1.2 assistant：代表AI助手的回答，可以在代码中人为设定
                        1.3 user：代表用户，发送问题、指令或需求
                    2.content：内容

    三、处理结果(response变量就是ChatCompletion对象)
        可以通过print(response.choices[0].message.content)输出模型给出的回答信息

    四、OpenAI库的流式输出  (模型把回复 “拆成一个个小片段”，边生成边返回给你，而不是等全部生成完再一次性返回。)
        可以在设定给结果输出为stream模式(流式输出)，获得更好的使用体验。
        开启流式输出步骤：
            1.在client.chat.completion.create()调用模型的时候设定参数stream=True
            2.for循环response对象，并在循环内输出内容

    五、OpenAI库附带历史消息调用模型 (即在messages的list内，组织历史消息提供给模型)
        调用模型传入的参数messages，其要求是list对象，即表明其支持非常多的消息在内。
        我们可以基于此，将历史消息填入，让模型知晓对话的上下文，更好的回答
            注意：当前的历史消息是一次性的
"""
# 获取客户端对象
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client: OpenAI = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# client.chat.completion创建ChatCompletion对象
from openai.types.chat.chat_completion import ChatCompletion

response:ChatCompletion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        # {"role":"system","content":"你是一个Python编程专家"},
        # {"role":"assistant","content":"我是一个Python编程专家。请问有什么可以帮助您的吗？"},
        # {"role":"user","content":"for循环输出1到5的数字"},

        #以下是OpenAI库附带历史消息调用模型，就是在messages中将历史消息输入
        {"role":"system","content":"你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有两条宠物狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小明有三条宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几条宠物？"},
    ],
    stream=True # 开启流式输出功能
)

# 处理结果
# # 获取全部信息
# print(response)

# # 将信息转化为json格式
# import json
# # 步骤1：将响应对象转为字典
# response_dict = response.model_dump()
#
# # 步骤2：将字典转为JSON字符串（格式化输出）
# response_json = json.dumps(
#     response_dict,
#     ensure_ascii=False,  # 保留中文，不转义
#     indent=2            # 缩进2个空格，和示例JSON格式一致
# )
#
# # 步骤3：打印完整JSON字符串
# print("完整JSON响应：")
# print(response_json)
# 直接获取AI助手的回答
# print(response.choices[0].message.content)

# 开启流式输出时的处理结果
for chunk in response:
    if chunk.choices[0].delta.content:
        print(
            chunk.choices[0].delta.content,
            end='',    # 每一段之间以单引号中的字符分隔
            flush=True # 立刻刷新缓冲区
        )
