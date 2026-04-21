"""
    栈和队列的应用： 迷宫问题
        给出一个二位列表，表示迷宫(0表示通道，1表示围墙)，
            给出算法，求一条走出迷宫的路径。
            maze= [
                [1,1,1,1,1,1,1,1,1,1],
                [1,0,0,1,0,0,0,1,0,1],
                [1,0,0,1,0,0,0,1,0,1],
                [1,0,0,0,0,1,1,0,0,1],
                [1,0,1,1,1,0,0,0,0,1],
                [1,0,0,0,1,0,0,0,0,1],
                [1,0,1,0,0,0,1,0,0,1],
                [1,0,1,1,1,0,1,1,0,1],
                [1,1,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1]
            ]
    思路方法：
        栈：
            方法名：深度优先搜索，回溯法
            思路：从一个节点开始，任意找下一个能走的点，当找不到能走的点时，
                退回上一个点寻找是否有其他方向的点。
            使用栈存储当前路径
            缺点：大概率不是最短路径

        队列：
            方法名：广度优先搜索
            思路：从一个节点开始，寻找所有接下来能继续走的点，继续不断寻找，直到找到出口。
            使用队列存储当前正在考虑的节点
"""
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y : (x-1, y),
    lambda x,y : (x+1, y),
    lambda x,y : (x, y-1),
    lambda x,y : (x, y+1)
]

# # 栈：深度优先搜索  回溯法
# def maze_path(x1,y1,x2,y2):
#     stack = []
#     stack.append((x1,y1)) # 起点
#     maze[x1][y1] = 2 #标记起点
#     while len(stack) > 0: # 栈大于0
#         curNode = stack[-1] # 当前所在位置
#         if curNode[0] == x2 and curNode[1] == y2:
#             for p in stack:
#                 print(p)
#             return True
#         # 四个方向：上：x-1,y; 下：x+1,y; 左：x,y-1; 右：x,y+1;
#         for dir in dirs: # 依次尝试：上、下、左、右
#             nextNode = dir(curNode[0], curNode[1]) # 计算下一个点的坐标
#             if maze[nextNode[0]][nextNode[1]] == 0: # 如果是路（0）
#                 stack.append(nextNode) # 走过去（入栈）
#                 maze[nextNode[0]][nextNode[1]] = 2 # 标记为已走过（2）
#                 break # 找到一个方向就走，不再试其他方向
#         else: # 这个else对应for循环，表示4个方向都走不了
#             stack.pop() # 退回到上一个位置
#     else:
#         print("没有路")
#         return False
#
# maze_path(1,1,8,8)

# 队列：广度优先搜索
from collections import deque

def print_r(path):
    curNode = path[-1]
    realPath = []
    while curNode[2] != -1:
        realPath.append((curNode[0], curNode[1]))
        curNode = path[curNode[2]]
    for node in realPath:
        print(node)

def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    # x,y坐标,前一个坐标的下标
    queue.append((x1,y1,-1))
    path = []
    maze[x1][y1] = 2
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print("没有路")
        return False

maze_path_queue(1,1,8,8)





