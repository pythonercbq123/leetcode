#  二叉树剪枝


class PruneTree:

    def prune(self, root):
        if root is None:
            return root
        root.left = self.prune(root.left)
        root.right = self.prune(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root