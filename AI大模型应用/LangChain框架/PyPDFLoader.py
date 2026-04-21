from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path=r"D:\Study\俄语\A1\ТРКИ-A1-刷习题\A1单词书.pdf",
    mode='single'
)

i = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20, i)