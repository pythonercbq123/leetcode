

class PostOrder:

    def __init__(self):
        self.node_list = []

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.node_list.append(root.val)

    def dfs_with_stack(self, root):
        cur = root
        prev = None
        stack = []
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            # 如果节点存在右节点 并且 右子节点正好是前一个被遍历的节点， 那么它的右子树被遍历过
            if cur.right is not None and cur.right != prev:
                cur = cur.right
            else:
                cur = stack.pop()
                self.node_list.append(cur.val)
                prev = cur
                cur = None


