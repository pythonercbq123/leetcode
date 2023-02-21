from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        _sum = 0
        for num in nums:
            _sum += num
        if _sum % 2 != 0:
            return False
        return self.subset_sum(nums, int(_sum / 2))

    def subset_sum(self, nums, target):
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 2)]
        for i in range(0, n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i][j - 1]
                if not dp[i][j] and j > nums[i - 1]:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]]
        return dp[n][target]


if __name__ == '__main__':
    s = Solution()
    ret = s.can_partition([1, 3, 4, 1, 9])
    print(ret)
