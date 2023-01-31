from typing import List
import random


class Solution:
    """
    通过快速排序求解数组中第k大的数字, 按照从小到大的排序, 第k大意味这排序完成 索引为 length - k
    """

    def kth_largest(self, nums: List, k: int) -> int:
        target = len(nums) - k
        start, end = 0, len(nums) - 1
        pivot = self.partition(nums, start, end)
        while pivot != target:
            if pivot > target:
                end = pivot - 1
            else:
                start = pivot + 1
            pivot = self.partition(nums, start, end)
        return nums[pivot]

    def partition(self, nums: List, start: int, end: int) -> int:
        rand = random.randint(0, end - start + 1) + start
        self.swap(nums, rand, end)
        small = start - 1
        for i in range(start, end):
            if nums[i] < nums[end]:
                small += 1
                self.swap(nums, small, i)
        small += 1
        self.swap(nums, small, end)
        return small

    def swap(self, nums: List, a: int, b: int):
        if a != b:
            nums[a], nums[b] = nums[b], nums[a]


if __name__ == '__main__':
    s = Solution()
    ret = s.kth_largest([1, 3, 7, 4, 2, 6], 2)
    print(ret)
