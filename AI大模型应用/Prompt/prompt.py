"""
    提示工程(Prompt Engineering)：是一项通过优化提示词(Prompt)和生成策略，从而获得更好的模型返回结果的工程。

    提示词的构成：
        1.指示(Instruction)/任务/要求：描述要让它做什么？
        2.上下文(Context)：给出与任务相关的背景信息。
        3.例子(Examples)：给出一些例子，让模型知道怎么回复。
        4.输入(Input)：任务的输入信息。
        5.输出(Output Format)：输出的格式，想要声明形式的输出？

    Zero-Shot学习(Zero-Shot Learning(零样本学习))：让模型在完全没见过某类任务数据的情况下，仅通过自然语言描述的指令，就能完成该任务。
        基于PromptTemplate直接完成
    One-Shot学习(One-Shot Learning(单样本学习))：提供 1 个示例，帮助模型理解任务格式与要求，再执行任务
    Few-Shot学习(Few-Shot Learning(少样本学习))：提供少量（通常 2～5 个）示例，让模型更准确地学习任务模式，提升输出稳定性与正确性
        基于FewShotPromptTemplate
    核心区别：给多少个example(示例)
"""

#     常见的提示词：
#         定义提示词：
#             instruction = """根据下面的上下文回答问题。保持答案简短且准确"""
#             context = """Teplizumab起源与一个位于新泽西的药品公司"""
#             query = """OKT3最初是从声明来员提取的？"""
#             prompt = f"""{instruction} ### 上下文{context} ###问题：{query}"""

"""
    样本学习(shot learning)：
        1.one-shot learning：只给一个example
        2.few-shot learning：多个examples
        3.zero-shot learning：不给任何的examples
        
    思维链(chain of thoughts)：把一个复杂的任务，拆解成多个骚味简单的任务，让大语言模型分步来四客机问题
        例子：提示词：-------------------------------，通过思维链CoT的方式来分析。
"""

# 例子：
# instruction = """
# 根据下面的上下文回答问题。保持答案简短且准确。如果不确定答案，请回答"不确定答案"
#
# 以Json格式输出:
# {"[具体问题]":"[答案]"}
# """
#
# examples = """
# {"你是谁?":"我是大模型"},
# """
#
# context = """
# Teplizumab起源于一个位于新泽西的药品公司，名为Ortho Pharmaceutical。\
# 在那里，科学家们生成了一种早期版本的抗体，被称为OKT3.最初这种分子是从小鼠中提取的，\
# 能够结合到T细胞的表面，并限制他们的细胞杀伤潜力。在1986年，它被批准用于帮助预防肾脏移植后的\
# 器官排斥，成为首个被允许用于人类的治疗性抗体。
# """
#
# query = """
# OTK3最初是从声明来源提取的？
# """
#
# prompt = f"""
# {instructions}
#
# # 最终 Prompt 模板（把 Example 加在指令和上下文之间）
# ### 示例
# {examples}
#
# ### 上下文
# {context}
#
# ### 问题
# {query}
#
# """
# # response = generate_responses(prompt) #调用大模型
# # print(response)
