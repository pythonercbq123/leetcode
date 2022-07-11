from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for num in nums:
            if num - 1 not in nums_set:
                current_streak = 1
                cur_num = num
                while cur_num + 1 in nums_set:
                    current_streak += 1
                    cur_num += 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak