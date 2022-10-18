from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        count = 0
        for heap in coins:
            if heap % 2 == 1:
                count += heap // 2 + 1
            else:
                count += heap // 2
        return count
