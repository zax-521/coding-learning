from langchain_community.document_loaders import JSONLoader

# JSON类对象
# loader = JSONLoader(
#     file_path="./data/stu.json",
#     jq_schema=".name",
# )
#
# res = loader.load()
# print(res)

# JSON数组
# loader1 = JSONLoader(
#     file_path="./data/stus.json",
#     jq_schema=".[].name",
#     text_content=False, # json文件中是否时字符串
# )
#
# res1 = loader1.load()
# print(res1)

# JsonLines文件
# loader2 = JSONLoader(
#     file_path="./data/stu_json_lines.json",
#     jq_schema=".name",
#     text_content=False,
#     json_lines=True,
# )
#
# res2 = loader2.load()
# print(res2)