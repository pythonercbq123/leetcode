from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            if s * 2 + nums[i] == total:
                return i
            s += nums[i]
        return -1