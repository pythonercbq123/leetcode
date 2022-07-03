from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    s = Solution()
    r = s.singleNumber([2, 2, 1, 1, 3])
    print(r)