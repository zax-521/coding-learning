"""
    队列(Queue)是一个数据集合，仅允许在队列的一端进行插入，另一段进行删除。
        1进行插入的一段称为队尾(rear)，插入动作称为进队或入队
        2.进行删除的一端称为队头(front)，沙漠成绩动作称为出队
        3.队列的性质：先进先出FIFO(First-in,First-out)
        4.队列的实现方式：环形队列

    双向队列：两端都支持进队和出队操作
    双向队列的基本操作：
        1.队首进队
        2.队首出队
        3.队尾进队
        4.队尾出队

    队列的内置模块：
        使用方法：from collections import deque
        创建队列：q = deque()
        进队：q.append()
        出队：q.popleft()
        双向队列队首进队：q.appendleft()
        双向队列队尾出队：q.pop()

"""

class CircleQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [0 for _ in range(max_size)]
        self.front = 0
        self.rear = 0

    def is_empty(self): # 判断是否为空
        return self.front == self.rear

    def is_full(self): # 判断队满
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, val):
        if self.is_full():
            print("队列已满")
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = val
        return True

    def dequeue(self):
        if self.is_empty():
            print("队列中没有元素")
            return None
        self.front = (self.front + 1) % self.max_size
        val = self.queue[self.front]
        return val

    def show_queue(self):
        if self.is_empty():
            print("队列中没有元素")
            return
        i = (self.front + 1) % self.max_size
        while i != (self.rear + 1) % self.max_size:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.max_size

# if __name__ == '__main__':
#     q = CircleQueue(5)
#     q.enqueue("一辈子")
#     q.enqueue(2)
#     q.enqueue("有太多不可能")
#     q.enqueue(4)
#     q.show_queue()

# 队列的内置模块
from collections import deque

# q = deque() # 设置长度，如果队满就队首就自动出队
# q.append(1) # 队尾进队
# q.popleft() # 队首出队
#
# # 用于双向队列
# q.appendleft(2) # 队首进队
# q.pop() # 队尾出队

# 打印文件的后n行
def tail(n):
    with open("../test.txt", 'r') as f:
        q = deque(f, n)
        return q
for line in tail(7):
    print(line, end='')