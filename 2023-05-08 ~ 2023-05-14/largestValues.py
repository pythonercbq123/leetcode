from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            max_val = float('-inf')
            for _ in range(size):
                node = queue.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val)
        return ans

    def largest_values(self, root: TreeNode) -> List[int]:
        # 找到二叉树每一层的最大值
        queue1 = deque()
        queue2 = deque()
        queue1.append(root)
        max_val = 0
        res = []
        while queue1:
            node = queue1.popleft()
            max_val = max(max_val, node.val)
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if not queue1:
                res.append(max_val)
                queue1 = queue2
                queue2 = deque()
                # 重置max_val
                max_val = 0
        return res

    def lowest_layer_left(self, root: TreeNode) -> List[int]:
        # 找到二叉树最下层的最左边的值
        queue1 = deque()
        queue2 = deque()
        queue1.append(root)
        left = root.val
        while queue1:
            node = queue1.popleft()
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if not queue1:
                queue1 = queue2
                queue2 = deque()
                if queue1:
                    left = queue1[0].val
        return left