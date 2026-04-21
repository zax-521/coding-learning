"""
    创建向量存储，基于向量存储完成：
                LangChain为向量存储提供的统一接口
        存入向量：add_documents
        删除向量：delete
        向量检索：similarity_search
"""

# 内置向量存储的使用示例
# from langchain_core.vectorstores import InMemoryVectorStore
# from langchain_community.embeddings import DashScopeEmbeddings
#
# # 调用向量转换使用的嵌入模型(向量模型)
# vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())
# # 添加文档到向量存储，并指定id
# vector_store.add_documents(documents=[doc1, doc2], ids=["id1", "id2"])
# # 删除文档(通过指定的id删除)
# vector_store.delete(ids=["id1"])
# # 相似度搜索
# similar_docs = vector_store.similarity_search("you query here", 4)

# 内置向量存储的使用
# from langchain_community.document_loaders import CSVLoader
# from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_core.vectorstores import InMemoryVectorStore
#
# vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())
#
# loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source" # 指定本条数据的来源是哪里
# )
#
# documents = loader.load()
# #id1
# vector_store.add_documents(
#     documents=documents,
#     ids=["id" + str(i) for i in range(1, len(documents) + 1)]
# )
#
# vector_store.delete(["id1","id10"])
# res = vector_store.similarity_search("全球AI算力竞赛升级", 3)
# print(res)



# 外置(Chroma)向量存储的使用示例
# from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_chroma import Chroma
#
# vector_store = Chroma(
#     collection_name="example_collection", # 集合的名称，相当于数据库的表的表名
#     embedding_function=DashScopeEmbeddings(), # 调用的向量模型
#     persist_directory="./chroma_langchain_db", #存储位置
# )

# Chroma向量存储的使用 (轻量级) 需pip install langchain-chroma,chromadb
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="name",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)

loader = CSVLoader(
    file_path="./data/info.csv",
    source_column="source",
    encoding="utf-8",
)

documents = loader.load()
vector_store.add_documents(
    documents=documents,
    ids=["id"+str(i) for i in range(1, len(documents) + 1)],
)
vector_store.delete(["id1"])
result = vector_store.similarity_search(
    "AI智能",
    3,
    filter={"source": "人民网"} # 来源过滤，只检索人民网的来源新闻
)
print(result)