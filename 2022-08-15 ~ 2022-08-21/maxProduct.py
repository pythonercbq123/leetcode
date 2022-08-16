from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f_max = [nums[0] for _ in range(n)]
        f_min = [nums[0] for _ in range(n)]
        for i in range(1, n):
            f_max[i] = max(f_max[i - 1] * nums[i], nums[i], f_min[i-1] * nums[i])
            f_min[i] = min(f_max[i - 1] * nums[i], nums[i], f_min[i-1] * nums[i])
        ans = f_max[0]
        for i in range(1, n):
            ans = max(f_max[i], ans)
        return ans
