from typing import List


class Solution:
    """
    小偷偷了相邻的两栋房屋 就会触发报警
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # 优化空间复杂度
            dp[i % 2] = max(dp[(i - 1) % 2],  dp[(i - 2) % 2] + nums[i])
        return dp[(n - 1) % 2]


if __name__ == '__main__':
    s = Solution()
    ret = s.rob(nums=[2, 3, 4, 5, 3])
    print(ret)
