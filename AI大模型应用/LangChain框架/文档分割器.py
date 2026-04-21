from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    file_path="../../python编程/基础/1_Python基础/基础笔记本.txt",
    encoding="utf-8",
)

all_docs = []
for docs in loader.lazy_load():
    all_docs.append(docs)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""],
    length_function=len
)

split_docs = splitter.split_documents(all_docs)
print(len(split_docs))
for doc in split_docs:
    print("="*20)
    print(doc)
    print("="*20)
