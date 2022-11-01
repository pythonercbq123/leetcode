

class PreOrder:

    def __init__(self):
        self.node_list = []

    def dfs(self, root):
        if root is None:
            return
        self.node_list.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def dfs_with_stack(self, root):
        stack = []
        cur = root
        while cur is not None or stack:
            while cur is not None:
                self.node_list.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        