from functools import reduce
from operator import xor
import bisect
bisect.bisect_left()


class Solution:
    def xorGame(self, nums):
        return len(nums) % 2 == 0 or reduce(xor, nums) == 0


if __name__ == '__main__':
    s = Solution()
    ret = s.xorGame([1, 2, 3])
    print(ret)
    ret = s.xorGame([1, 2, 1])
    print(ret)