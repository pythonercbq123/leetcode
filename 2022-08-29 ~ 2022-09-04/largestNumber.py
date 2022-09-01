import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)

        def comp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        sorted_strs = sorted(strs, key=functools.cmp_to_key(comp), reverse=True)
        return ''.join(sorted_strs) if sorted_strs[0] != '0' else '0'


if __name__ == '__main__':
    s = Solution()
    r = s.largestNumber([0, 0])
    print(r)
