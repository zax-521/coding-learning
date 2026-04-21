"""
    一、PromptTemplate：通过提示词模板，支持动态注入信息
        使用PromptTemplate模型构建提示词，在大型工程中更容易标准化模板
            Template模板类，支持LangChain框架的链式调用

    二、FewShotPromptTemplate：支持基于提示词模板注入任意数量的示例信息
        FewShotPromptTemplate(
            example=None # 示例数据，list，内套字典
            example_prompt=None # 示例数据的提示词模板
            prefix=None # 组装提示词，示例数据前内容
            suffix=None # 组装提示词，示例数据后内容
            input_variables=None # 列表，注入的变量列表
        )
    三、ChatpromptTemplate：支持注入任意数量的历史会话信息

"""
# 一、PromptTemplate
# # 标准写法
# from langchain_core.prompts import PromptTemplate
# from langchain_community.llms.tongyi import Tongyi
# prompt_template = PromptTemplate.from_template(
#     "我的邻居姓{lastname}，刚生了{gender}，帮忙起名字，请简略回答。"
# )
#
# # 变量注入，生成提示词文本 调用format方法注入信息
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
#
# model = Tongyi(model="qwen-max")  # 创建模型对象
# res = model.invoke(input=prompt_text) # 调用模型获取结果
# print(res)

# # 基于chain链的写法
# from langchain_core.prompts import PromptTemplate
# from langchain_community.llms.tongyi import Tongyi
# prompt_template = PromptTemplate.from_template(
#     "我的邻居姓{lastname}，刚生了个{gender}，帮忙起个名字，请简略回答。"
# )
#
# model = Tongyi(model="qwen-max") # 创建模型对象
# # 生成链
# chain = prompt_template | model # | 管道符，上一个组件的输出作为下一个组件的输入(即左边的输出作为右边的输入)
# # 基于链，调用模型获取结果
# res = chain.invoke(input={"lastname" : "张", "gender" : "儿子"})
# print(res)

# 二、FewShotPromptTemplate
# from langchain_community.llms.tongyi import Tongyi
# from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
# # 示例模板
# example_template = PromptTemplate.from_template("单词:{word}, 反义词:{antonym}")
# # 示例的动态数据注入 要求是list内部套字典
# example_data = [
#     {"word":"大","antonym":"小"},
#     {"word":"上","antonym":"下"}
# ]
#
# few_shot_prompt = FewShotPromptTemplate(
#     example_prompt=example_template, # 示例数据的模板
#     examples=example_data, # 示例的数据(来自于动态数据的)，list内套字典
#     prefix="给出给定词的反义词，如下示例：", # 示例之前的提示词
#     suffix="基于示例告诉我：{input_word}的反义词是？", # 示例之后的提示词
#     input_variables=['input_word'] # 声明在前缀或后缀中所需要注入的变量名
# )
#
# prompt_text =few_shot_prompt.invoke(input={"input_word": "天"}).to_string()
#
# print(prompt_text)
#
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

# 三、ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是李白的狂热爱好者，你可以背诵李白的所有诗"),
        MessagesPlaceholder("history"),
        ("human","来一首诗"),
    ]
)

history_data = [
    ("human","来一首诗"),
    ("ai","静夜思：床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human","来一首诗"),
    ("ai", "望庐山瀑布：日照香炉生紫烟，遥看瀑布挂前川。飞流直下三千尺，疑似银河落九天"),
    ("human","来一首诗"),
    ("ai", "赠汪伦：李白乘舟将欲行，忽闻岸上踏歌声。桃花潭水深千尺，不及汪伦送我情。")
]

prompt_text = chat_prompt_template.invoke(input={"history" : history_data}).to_string()
print(prompt_text)
model = ChatTongyi(model="qwen3-max")
res = model.invoke(input=prompt_text)
print(res.content)