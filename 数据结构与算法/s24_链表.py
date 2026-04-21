"""
    链表：
        链表是由一系列节点组成的元素集合。每个节点包含两部分，
            数据域item和指向下一个节点的指针next。通过节点之间的相互连接，最终串联成一个链表。

    创建链表：
        方法一：头插法
        方法二：尾插法

    双链表：双链表的每个节点有两个指针：一个指向后一个节点，另一个指向前一个节点。
"""
# 单链表
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# 头插法
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

# 尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

# 链表的插入(先连接后节点，再连接前节点)
# p.next = curNode.next
# curNode.next = p

# 链表的删除(前节点直接跳过删除节点，连接删除节点的下一个节点)
# p = curNode.next
# curNode.next = curNode.next.next
# del p

# 链表的遍历
def print_linklist(lk):
    while lk:
        print(lk.item, end=",")
        lk = lk.next

lk_1 = create_linklist_head([1,2,3,4,5])
lk_2 = create_linklist_tail([1,2,3,4,5])
print_linklist(lk_1)
print()
print_linklist(lk_2)

# 双链表
class NodeDouble(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prior = None

# 双链表节点的插入
# p.next = curNode.next
# curNode.next.prior = p
# p.prior = curNode
# curNode.next = p

# 双链表节点的删除
# p = curNode.next
# curNode.next = p.next
# p.next.prior = curNode
# del p