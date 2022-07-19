from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def max_gain(node):
            if node is None:
                return 0

            max_left = max(max_gain(node.left), 0)
            max_right = max(max_gain(node.right), 0)
            total = node.val + max_left + max_right
            self.max_sum = max(self.max_sum, total)
            return max(max_left + node.val, max_right + node.val)
        max_gain(root)
        return self.max_sum
