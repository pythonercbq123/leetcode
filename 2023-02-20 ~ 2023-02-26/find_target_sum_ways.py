from typing import List


class Solution:
    def find_target_sum_ways(self, nums: List[int], target: int) -> int:
        _sum = 0
        for num in nums:
            _sum += num
        if (_sum + target) % 2 == 1:
            return 0
        else:
            ret = self.subset_sum_one_dimension(nums, (_sum + target) // 2)
            return ret

    def subset_sum(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(target, 1, -1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        return dp[n][target]

    def subset_sum_one_dimension(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target, target - num - 1, -1):
                dp[j] += dp[j - num]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    ret = s.find_target_sum_ways([2, 2, 2], 2)
    print(ret)
