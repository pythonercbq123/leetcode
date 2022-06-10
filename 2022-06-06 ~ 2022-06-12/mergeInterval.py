from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for item in sorted_intervals:
            if not merged or item[0] > merged[-1][1]:
                merged.append(item)
            else:
                merged[-1][1] = max(merged[-1][1], item[1])
        return merged


