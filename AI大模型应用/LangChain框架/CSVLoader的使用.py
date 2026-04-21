from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path= "./data/stu.csv",
    csv_args= {
        "delimiter": ",", # 指定分隔符
        "quotechar": "'", # 指定带有分割符文本的引号包围时单引号还是双引号 默认为双引号
        "fieldnames" : ["姓名", "年龄", "性别", "爱好",]
    },
    encoding="utf-8" # 指定编码
)
# documents = loader.load()
# print(documents)
#
# for document in documents:
#     print(document, type(document))
#

# 懒加载 迭代器[document]
for document in loader.lazy_load():
    print(document, type(document))
