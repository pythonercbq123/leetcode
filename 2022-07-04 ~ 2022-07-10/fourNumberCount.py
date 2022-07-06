from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        res = 0
        c = Counter(u + v for u in nums1 for v in nums2)
        for x in nums3:
            for y in nums4:
                if -x-y in c:
                    res += c.get(-x-y)
        return res
