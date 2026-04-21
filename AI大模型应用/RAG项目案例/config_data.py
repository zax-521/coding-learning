md5_path = "./md5.text"

# Chroma
collection_name = "rag"
embedding_model_name = "text-embedding-v4"
persist_directory ="./chroma_db"

# Spliter
chunk_size = 1000
chunk_overlap = 100
separators = ["\n", "\n\n", "?", "!", ".", "？", "！", "。", " ", ""]
mix_split_char_number = 1000

#
similarity_threshold = 1 # 检索返回匹配的文档数量


#
chat_model_name = "qwen3-max"
session_config={
        "configurable" : {
            "session_id" : "user_001"
        }
    }