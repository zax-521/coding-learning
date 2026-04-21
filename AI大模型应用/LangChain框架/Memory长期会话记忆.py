"""
    message_to_dict：单个消息对象(BaseMessage类实例) -> 字典
    messages_from_dict：[字典, 字典, ...] -> [消息, 消息, ...]
    AIMessage、HumanMessage、SystemMessage 都是BaseMessage的子类
"""

import os,json
from typing import Sequence
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id # 会话id
        self.storage_path = storage_path # 不同会话id的存储文件，所在的文件夹路径
        self.file_path = os.path.join(self.storage_path, self.session_id) # 完整路径
        os.makedirs(self.storage_path, exist_ok=True) # 确保文件夹是存在的； exist_ok = True：当文件夹存在则跳过，反之创建文件夹

    def add_messages(self, messages: Sequence[BaseMessage]) -> None: # Sequence：序列
        all_messages = list(self.messages) # 已有的消息列表
        all_messages.extend(messages) # 将新的消息列表跟已有的消息列表结合
        # 将数据同步写入到本地文件中
        # 类对象写入文件 -> 一堆二进制
        # 为了方便，可以将BaseMessage消息转为字典(借助json模块以json字符串写入文件)
        # message_to_dict：单个消息对象(BaseMessage类实例) 转换为 字典
        # new_messages = []
        # for message in all_messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)

        new_messages = [message_to_dict(message) for message in all_messages]

        # 将数据写入本地文件
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property # @property装饰器将 message方法 变成 成员属性使用
    def messages(self) -> list[BaseMessage]: # 当前文件内：list[字典]
        try:
            with open(self.file_path, 'r', encoding="utf-8") as f:
                messages_data = json.load(f) # 返回值：list[字典]
                # messages_from_dict：[字典, 字典, ...] -> [消息, 消息, ...]
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump([], f)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "需要你根据历史会话，猜歌："),
        MessagesPlaceholder("chat_history"),
        ("human","请回答问题：{input}")
    ]
)

model = ChatTongyi(model="qwen3-max")

str_parser = StrOutputParser()

base_chain = prompt | model | str_parser

def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")

conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key = "input",
    history_messages_key = "chat_history"
)

if __name__ == "__main__":
    session_config = {
        "configurable" : {
            "session_id" : "user_01"
        }
    }

    res1 =conversation_chain.invoke({"input": "小明有一只猫"}, session_config)
    print("第一次执行：",res1)
    res2 = conversation_chain.invoke({"input": "小红有三只狗"}, session_config)
    print("第二次执行：",res2)
    res3 = conversation_chain.invoke({"input": "总共有几只宠物？"}, session_config)
    print("第三次执行：",res3)