class InOrder:

    def __init__(self):
        self.node_list = []

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.node_list.append(root.val)
        self.dfs(root.right)

    """
    递归的代码比较简单 并且容易栈溢出 因此下面用栈的方式实现中序遍历
    """

    def dfs_with_stack(self, root):
        stack = []
        cur = root
        #  注意是or
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.node_list.append(cur.val)
            cur = cur.right
        return self.node_list
