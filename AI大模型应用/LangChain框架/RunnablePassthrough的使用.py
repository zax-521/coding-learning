"""
    让向量检索加入链：使用RunnablePassthrough类
"""
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

model = ChatTongyi(model="qwen3-max")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}。"),
        ("user", "用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡稍有控制卡路里摄入并运动起来", "跑步是很好的运动哦"])

input_text = "怎么减肥？"

retriever = vector_store.as_retriever(search_kwargs={"k": 2})


def prompt_content(docs: list[Document]):
    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str += "]"
    return formatted_str

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

chain = ({
            "input": RunnablePassthrough(), # 透传用户输入
            "context" : retriever | prompt_content
        } # 这个链式中input=input_text首先会输入进retriever | prompt_content中，
         # 然后因为{}这个字典属于一个链式中的组件，所以input其实是拿不到input=input_text的，
         # 但是我们这里用了RunnablePassthrough()这个创建类的实例对象，这个实例对象的的构造方法可以透传用户输入，简单意思就是说可以直接拿取用户输入，
         # 所以这里的input=input_text传给了{}字典中的两个value中
        | prompt
        | RunnableLambda(print_prompt)
        | model
        | StrOutputParser())

res = chain.invoke(input=input_text)
print(res)

"""
    retriever:
        -输入：用户的提问   str
        -输出：向量库的检索结果 list[Document]
    
    prompt:
        -输入：用户的提问 + 向量库的检索结果   dict
        -输出：完整的提示词 PromptValue
"""