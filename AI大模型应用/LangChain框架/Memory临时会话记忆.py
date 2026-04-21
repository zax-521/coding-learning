"""
    RunnableWithMessageHistory是LangChain内Runnable接口的实现，主要用于：
        创建一个带有历史记忆功能的Runnable实例(链)
    它在创建的时候需要提供一个BaseChatMessageHistory的具体实现：
        InMemoryChatMessageHistory可以实现在内存中存储历史

"""

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "需要你根据历史会话，回答问题："),
        MessagesPlaceholder("chat_history"),
        ("human","请回答问题：{input}"),
    ]
)

str_parser = StrOutputParser()

model = ChatTongyi(model="qwen3-max")

def print_prompt(full_prompt):
    print("="*20, full_prompt, "="*20)
    return full_prompt

base_chain = prompt_template | print_prompt | model | str_parser

story = {} # key为session_id,value为InMemoryChatMessageHistory类对象
# 实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in story:
        story[session_id] = InMemoryChatMessageHistory()
    return story[session_id]

# 创建一个新链，对原有链的增强功能：自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain, # 被增强的原有的chain
    get_history, # 通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input", # 表示用户输入在模板中的占位符
    history_messages_key="chat_history" # 表示历史记录在模板中的占位符
)


if __name__ == "__main__":
    # 固定格式，添加LangChain的配置，为当前程序配置所属的session——id
    session_config = {
        "configurable" : {
            "session_id" : "user_01"
        }
    }
    res = conversation_chain.invoke({"input": "小明有一只猫"}, session_config)
    print("第一次执行：",res)
    res1 = conversation_chain.invoke({"input": "小红有三只狗"}, session_config)
    print("第二次执行：",res1)
    res2 = conversation_chain.invoke({"input": "总共有几只宠物？"}, session_config)
    print("第三次执行：",res2)