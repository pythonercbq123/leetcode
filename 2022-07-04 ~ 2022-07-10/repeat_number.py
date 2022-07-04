from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        r = c.most_common()
        if r:
            return r[0][0]
        return -1

    def find_by_set(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for i in range(n):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                break
        return nums[i]
