from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(min(height[left], height[right]) * (right - left), max_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
