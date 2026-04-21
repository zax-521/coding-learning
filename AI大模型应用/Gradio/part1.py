# 案例一：一个接收文本输入并返回的该文本倒序输出的应用
import gradio as gr

# 功能实现
# def reverse_test(test):
#     return test[::-1]
def hellotoPerson(name):
    return f'Hello, {name}!'
# 界面配置
demo = gr.Interface(
    fn= hellotoPerson, # 调用reverse_test函数
    inputs= "text", # 输入组件类型为文本
    outputs= "text") # 输出组件类型为文本

# 启动应用
demo.launch()