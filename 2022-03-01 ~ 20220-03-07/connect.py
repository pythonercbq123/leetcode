# # 层序遍历思路

# 填充每个节点的下一个右侧节点指针
# 给定一个
# 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct
# Node
# {
#     int
# val;
# Node * left;
# Node * right;
# Node * next;
# }
# 填充它的每个
# next
# 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将
# next
# 指针设置为
# NULL。
#
# 初始状态下，所有
# next
# 指针都被设置为
# NULL。

# 示例
# 1：

# 输入：root = [1, 2, 3, 4, 5, 6, 7]
# 输出：[1,  # ,2,3,#,4,5,6,7,#]
#     解释：给定二叉树如图
# A
# 所示，你的函数应该填充它的每个
# next
# 指针，以指向其下一个右侧节点，如图
# B
# 所示。序列化的输出按层序遍历排列，同一层节点由
# next
# 指针连接，'#'
# 标志着每一层的结束。
# 示例
# 2:
#
# 输入：root = []
# 输出：[]
#
# 提示：
#
# 树中节点的数量在[0, 212 - 1]
# 范围内
# - 1000 <= node.val <= 1000
#
# 进阶：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 通过次数211, 892

import collections

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:

            # 记录当前队列大小
            size = len(Q)

            # 遍历这一层的所有节点
            for i in range(size):

                # 从队首取出元素
                node = Q.popleft()

                # 连接
                if i < size - 1:
                    node.next = Q[0]

                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # 返回根节点
        return root


