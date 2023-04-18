from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_ancestor_diff(self, root: Optional[TreeNode]) -> int:
        #  必须是节点和其祖先的最大差值 而不是任意两个节点
        def dfs(node, min_val, max_val):
            if not node:
                return 0
            diff = max(abs(node.val - min_val), abs(node.val - max_val))
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)
            return max(diff, left_diff, right_diff)

        return dfs(root, root.val, root.val)


def test_max_ancestor_diff():
    # Test case 1
    root1 = TreeNode(8, left=TreeNode(3), right=TreeNode(10, right=TreeNode(14)))
    sol = Solution()
    assert sol.max_ancestor_diff(root1) == 6


if __name__ == '__main__':
    test_max_ancestor_diff()
