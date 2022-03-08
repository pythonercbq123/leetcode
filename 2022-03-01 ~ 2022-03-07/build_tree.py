# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            # 前序遍历的第一个节点是根节点
            pre_root = pre_left
            # 在中序遍历中定位根节点
            in_root = index[preorder[pre_root]]
            # 创建根节点
            root = TreeNode(preorder[pre_root])
            # 获取左子树的数量
            size_left_subtree = in_root - in_left
            # 递归创建左子树
            root.left = helper(pre_root + 1, pre_root + size_left_subtree, in_left, in_root - 1)
            # 递归创建右子树
            root.right = helper(pre_root + size_left_subtree + 1, pre_right, in_root + 1, in_right)
            return root

        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return helper(0, n - 1, 0, n - 1)
