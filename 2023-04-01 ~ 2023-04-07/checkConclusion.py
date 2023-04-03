from typing import List
from collections import defaultdict


class Solution:
    def check_conclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts = defaultdict(int)
        for i in range(len(s1)):
            counts[s1[i]] += 1
            counts[s2[i]] -= 1
        if self.counts_equal_zero(counts):
            return True
        for i in range(len(s1), len(s2)):
            counts[s2[i]] -= 1
            counts[s2[i - len(s1)]] += 1
            if self.counts_equal_zero(counts):
                return True
        return False

    def counts_equal_zero(self, counts):
        for i in counts.values():
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ret = s.check_conclusion('ac', 'dgcaf')
    print(ret)
