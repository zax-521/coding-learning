"""
    chain链：
        [将组件串联，上一个组件的输出作为下一个组件的输入]是LangChain链(尤其是 | 管道链)的核心工作原理
            ，这也是链式调用的核心价值：实现数据的自动化流转与组建的协同工作
        示例：chain = prompt_template | model
        注：即Runnable子类对象才能入链(以及Callable、Mapping接口子类对象也可以)
"""

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.base import RunnableSerializable

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是李白的狂热爱好者，你可以背诵李白的所有诗"),
        MessagesPlaceholder("history"),
        ("human","来一首诗")
    ]
)

history_data = [
    ("human", "来一首诗"),
    ("ai", "静夜思：床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human", "来一首诗"),
    ("ai", "望庐山瀑布：日照香炉生紫烟，遥看瀑布挂前川。飞流直下三千尺，疑似银河落九天"),
    ("human", "来一首诗"),
    ("ai", "赠汪伦：李白乘舟将欲行，忽闻岸上踏歌声。桃花潭水深千尺，不及汪伦送我情。")
]

# prompt_text = chat_prompt_template.invoke(input={"history":history_data}).to_spring
# print(prompt_text)

model = ChatTongyi(model="qwen3-max")

# chain链
chain: RunnableSerializable = chat_prompt_template | model
print(type(chain))

#Runnable接口，invoke执行
res = chain.invoke(input={"history" : history_data})
print(res.content)

#Runnable接口，stream执行
for chunk in chain.stream(input={"history" : history_data }):
    print(chunk.content, end="", flush=True) # flush=True立刻刷新缓冲区