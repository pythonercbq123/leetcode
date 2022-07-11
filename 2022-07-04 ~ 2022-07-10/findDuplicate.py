from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return nums[slow]
