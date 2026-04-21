"""
    Document loaders(文档加载器)：文档加载器提供了一套标准接口，用于将不同来源(如 CSV、PDF或JSON等)的数据
        读取为LangCHain的文档格式。这确保了无论数据来源如何，都能对其进行一致性处理。
        文档加载器(内置或自行实现)需实现BaseLoader接口。
    Class Document：是LangChain内文档的统一载体，所有文档加载器最终返回此类的实例。
    Document类的核心记录了：
        page_content；文档内容
        metadata：文档原数据(字典)
    不同文档加载器的统一接口方法：
        load()：一次性加载全部文档
        lazy_load()：延迟流式传输文档，对大型数据集很有用，避免内存溢出

    CSVLoader：将CSV数据加载为Document类对象

    JSONLoader：将JSON数据加载为Document类型对象，使用时需安装pip install jq
        jq：jq是一个跨平台的json解析工具，LangChain底层对JSON的解析就是基于jq工具实现的
        将JSON数据的信息抽取出来，封装为Document对象，抽取的时候依赖jq_schema语法

    TextLoader：将读取文本文件(如.txt)，将全部内容放入到一个Document对象中(即一个Document对象的list)
        当文档内容过大时，一个Document对象不够用时，可以使用文档分割器(RecursiveCharacterTextSplitter)

    RecursiveCharacterTextSplitter：递归字符文本分割器
        主要用于按自然段落分割大文档
        可以指定小文档的最大字符数、重叠字符数
        可以手动指定段落划分的依据(符号)以及字符数量统计函数

    PyPDFLoader：将PDF数据加载为Document类型对象，使用时需安装pip install pypdf(依赖PyPDF库)

    注：Langchain内置文档加载器官方文档：https://docs.langchain.com/oss/python/integrations/document_loaders
"""
# Document类实例
# from langchain_core.documents import Document
#
# document = Document(
#     page_content="Hello,world", metadata={"source":"https://example.com"}
# )

# CSVLoader的使用示例
# from langchain_community.document_loaders.csv_loader import CSVLoader
#
# loader = CSVLoader(
#     # 初始化参数
#     file_path="./xxx.csv", # 文件完整路径
#     csv_args={
#         "delimiter": ",", # 指定分隔符
#         "quotechar": '"', # 指定字符串的引号包裹
#         # 字段列表(无表头时使用，有表头勿用会读取首行做为数据)
#         "fieldnames" : ["name", "age", "gender"],
#     }
#     encoding="utf-8",
#     source_column="source", # 指明本条数据的来源
# )
# # 一次性加载全部文档
# document = loader.load() # [document, document, ...]
# print(document)
# # 延迟流式传输文档，对于大数据集，分段返回文档
# for document in loader.lazy_load():
#     print(document)

# JSONLoader的使用示例
# json对象 .表示整个JSON对象的根 []表示数组
# 例子：.name = "周杰伦", .hobby[2] = "rap", .other.addr = "深圳"
# {
#     "name" : "周杰伦",
#     "age" : 11,
#     "hobby" : ["唱", "跳", "rap"],
#     "other" : {
#           "addr" : "深圳",
#           "tel" : "1233123123"
#     }
# }
# json数组 .[].得到所有字典, .[].name 表示抽取所有字典的name
# [
#     {"name" : "周杰伦", "age" : 11, "gender" : "男"},
#     {"name" : "蔡依林", "age" : 12, "gender" : "女"},
#     {"name" : "王力宏", "age" : 11, "gender" : "男"}
# ]
#
# JsonLines文件
#     {"name" : "周杰伦", "age" : 11, "gender" : "男"}
#     {"name" : "蔡依林", "age" : 12, "gender" : "女"}
#     {"name" : "王力宏", "age" : 11, "gender" : "男"}


# from langchain_community.document_loaders import JSONLoader
#
# loader = JSONLoader(
#     file_path="data/stus.json", # 文件路径
#     jq_schema=".", # jq schema语法
#     text_content=False, # 抽取的是否时字符串，默认True
#     json_lines=True # 是否时JsonLines文件(即每一行都是JSON对象) 默认为False
# )

# TextLoader的使用示例
# from langchain_community.document_loaders import TextLoader
#
# loader = TextLoader(
#     "xxx.txt",
#     encoding="utf-8",
# )
# docs = loader.load()
# print(docs)
# print(len(docs))

# RecursiveCharacterTextSplitter的使用示例
# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
#
# loader = TextLoader(
#     "xxx.txt",
#     encoding="utf-8",
# )
#
# docs = loader.load()
#
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500, # 分段的最大字符数
#     chunk_overlap=50, # 分段之间允许重叠的字符数
#     # 文本分段依据
#     separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", "",],
#     # 字符统计依据(函数)
#     length_function=len,
# )
# # 调用分割器中分割文档的方法split_documents()
# split_docs = splitter.split_documents(docs)

# PyPDFLoader的使用示例
# from langchain_community.document_loaders import PyPDFLoader
#
# loader = PyPDFLoader(
#     file_path="", # 文件路径必填
#     mode='page', # 读取模式，可选page(按页划分不同的Document)和single(单个Document) 默认为page模式
#     password='password', # 文件密码
# )




