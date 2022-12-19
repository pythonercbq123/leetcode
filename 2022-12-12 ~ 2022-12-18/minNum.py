from typing import List


class Solution:
    def min_num(self, nums: List, limit: int, goal: int):
        return (abs(sum(nums) - goal) + limit - 1) // limit


if __name__ == '__main__':
    s = Solution()
    ret = s.min_num([1, 2, -1, 1], 1, 9)
    print(ret)

