"""
    栈(Stack)是一个数据集合，可以理解为只能在一段进行插入或删除操作的列表。
    栈的特点：后进先出LIFO(last-in, first-out)
    栈的概念：栈顶、栈底
    栈的基本操作：
        1.进栈(压栈)：push
        2.出栈：pop
        3.取栈顶；getTop
"""

class Stack:
    def __init__(self):
        self.stack = []

    # 进栈
    def push(self, element):
        self.stack.append(element)
    #出栈
    def pop(self):
        if len(self.stack) >= 0:
            return self.stack.pop()
        else:
            return None
    # 看栈顶
    def get_top(self):
        if len(self.stack) >= 0:
            return self.stack[-1]
        else:
            return None
    # 判断是否为空列表
    def is_empty(self):
        return len(self.stack) == 0
    # 元素个数
    def size(self):
        return len(self.stack)

# 栈的应用：括号匹配问题
def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False