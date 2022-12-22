from typing import List
"""
给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。

你可以进行如下操作至多 maxOperations 次：

选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。

请你返回进行上述操作后的最小开销。

"""


class Solution:
    """
    二分查找解决这个问题十分精妙
    """
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right, ans = 1, max(nums), 0
        while left <= right:
            # 注意条件 <=, 当left=right的时候依然可以缩小范围
            y = (left + right)//2
            ops = sum((i-1)//y for i in nums)
            if ops <= maxOperations:
                # 右侧缩减范围
                right = y - 1
                ans = y
            else:
                # 左侧缩减范围
                left = y + 1
        return ans