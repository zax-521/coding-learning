from langchain_core.prompts import MessagesPlaceholder
from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from langchain_core.documents import Document
from file_history_store import get_history

class RagService(object):
    def __init__(self):
        self.vector_store = VectorStoreService(DashScopeEmbeddings(model=config.embedding_model_name))
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
                ("system","以下是该用户的历史会话消息:"),
                MessagesPlaceholder("history"),
                ("human","请回答用户提问:{input}"),
            ]
        )
        self.chat_model = ChatTongyi(model=config.chat_model_name)
        self.chain= self.__get_chain()

    def __get_chain(self):
        def print_prompt(prompt):
            print(prompt.to_string())
            print("=" * 20)
            return prompt

        def format_prompt(docs: list[Document]):
            if not docs:
                return "无相关参考资料"
            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段：{doc.page_content}\n文档元数据：{doc.metadata}\n\n"
            return formatted_str

        def format_for_retriever(value:dict) -> str:
            return value["input"]

        def format_for_prompt_template(value):
            new_value = {}
            new_value["input"] = value["input"]["input"]
            new_value["history"] = value["input"]["history"]
            new_value["context"] = value["context"]
            return new_value

        """获取最终的执行链"""
        retriever = self.vector_store.get_retriever()
        chain = (
            {"input" : RunnablePassthrough(), "context" : RunnableLambda(format_for_retriever) | retriever | format_prompt}
            | RunnableLambda(format_for_prompt_template) | self.prompt_template | print_prompt | self.chat_model | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )

        return conversation_chain

if __name__ == "__main__":

    res = RagService().chain.invoke({"input":"我体重为180斤，给我推荐尺码。"},config.session_config)
    print(res)