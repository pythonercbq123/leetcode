

class Solution:

    def sum_numbers(self, root):
        return self.dfs(root, 0)
    
    def dfs(self, root, path):
        if root is None:
            return 0
        path = path * 10 + root.val
        if root.left is None and root.right is None:
            return path
        return self.dfs(root.left, path) + self.dfs(root.right, path)