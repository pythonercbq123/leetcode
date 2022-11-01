from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque()

    def cbt_insert(self):
        self.queue.append(self.root)
        while self.queue and self.queue[0].left is not None and self.queue[0].right is not None:
            #  存在子节点为None 说明下一个添加的父亲节点为该节点。
            node = self.queue[0]
            self.queue.popleft()
            self.queue.append(node.left)
            self.queue.append(node.right)

    def insert(self, v):
        parent = self.queue[0]
        node = TreeNode(v)
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.queue.popleft()
            # 添加新的节点到队列的时机为父节点已经满,添加对应两个子节点
            self.queue.append(parent.left)
            self.queue.append(parent.right)
        return parent.val

    def get_root(self):
        return self.root
