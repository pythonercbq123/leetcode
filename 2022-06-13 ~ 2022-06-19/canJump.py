from typing import List
import math


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        n = len(nums)
        right_most = 0
        for i in range(n):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
                if right_most >= n - 1:
                    return True

        return False
