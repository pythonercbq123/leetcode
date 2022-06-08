from typing import List


class Solution:

    def find_peak_element(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        def get(i: int):
            if i == -1 or i == len(nums):
                return float('-inf')
            else:
                return nums[i]
        while left <= right:
            mid = left + (right - left) >> 1
            if get(mid) > get(mid - 1) and get(mid) > get(mid + 1):
                return nums[mid]
            elif get(mid) < get(mid - 1):
                right = mid - 1
            else:
                left = mid + 1
        return -1
