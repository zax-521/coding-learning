"""
    LangChain的概念：一套用于构建大语言模型（LLM）应用的开源框架，核心目标是解决单一 LLM 能力局限，
        通过模块化组件将 LLM 与外部资源（数据、工具）、工作流结合，快速搭建复杂 AI 应用（如 RAG、智能体、对话机器人等）
        (即LangChain是一个开发LLM相关业务功能的集大成者，是一个Python的第三方库，提供了各种功能的API)
    注：LangChain自身并不是开发LLMs,它的核心理念是为各种LLMs实现通用的接口，
            把LLMs相关的组件"链接"在一起，简化LLMs应用的开发难度，方便开发者快速地开发复杂的LLMs应用

    LangChain的主要功能：
        1.Prompt：优化提示词(提示词工程)
        2.Models：调用各类模型
            1.LangChain目前支持三种类型的模型：
                1.LLMs(大语言模型)：是技术范畴的统称，指基于大参数量、海量文本训练的 Transformer 架构模型，
                    核心能力是理解和生成自然语言，主要服务于文本生成场景。
                2.Chat Models(聊天模型)：是应用范畴的细分，是专为对话场景优化的 LLMs，
                    核心能力是模拟人类对话的轮次交互，主要服务于聊天场景。
                    1.AIMessage：就是 AI 输出的消息，可以是针对问题的回答。（OpenAI 库中的 assistant 角色）
                    2.HumanMessage：人类消息就是用户信息，由人给出的信息发送给 LLMs 的提示信息，
                        比如 “实现一个快速排序方法”。（OpenAI 库中的 user 角色）
                    3.SystemMessage：可以用于指定模型具体所处的环境和背景，如角色扮演等。你可以在这里给出具体的指示，
                        比如 “作为一个代码专家”，或者 “返回 json 格式”。（OpenAI 库中的 system 角色）
                3.Embeddings Models(嵌入模型)：文本嵌入模型接收文本作为输入，得到文本的向量。
        3.History：管理会话历史记录(记忆)
        4.Indexes：管理和分析各类文档
        5.Chains：构建功能的执行链条
        6.Agent：构建智能体

    LangChain的安装：pip install langchain langchain-community langchain-ollama dashscope chromadb
        langchain：核心包
        langchain-community：社区支持包，提供了更多的第三方模型调用
        langchain-ollama：Ollama支持包，支持调用Ollama托管部署的本地模型
        dashscope：阿里云通义千问的Python SDK
        chromadb：轻量向量数据库

"""
# import langchain
# import langchain_community
# import langchain_ollama
# import dashscope
# import chromadb