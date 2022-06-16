from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        定义dp[i]是以nums[i]结尾的最长子序列长度
        :param nums:
        :return:
        """
        n = len(nums)
        if n < 1:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(n):
            res = max(res, dp[i])
        return res