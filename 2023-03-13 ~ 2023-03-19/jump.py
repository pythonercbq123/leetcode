from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i]是跳转到索引i需要的最小步数
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[n - 1]

    def jump2(self, nums: List[int]) -> int:
        # dp[i]是跳转到索引i需要的最小步数
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        step = [0] * n
        step[1] = nums[0]
        for i in range(1, len(nums)):
            if step[dp[i - 1]] >= i:
                dp[i] = dp[i - 1]

        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    ret = s.jump([2, 3, 1, 1, 4])
    print(ret)

    ret = s.jump([1, 2, 1, 1, 1])
    print(ret)
