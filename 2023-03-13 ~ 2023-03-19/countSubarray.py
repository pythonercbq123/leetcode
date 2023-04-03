from typing import List


class Solution:
    def count_sub_arrays(self, nums: List[int], k: int) -> int:
        # 思路hash表 + 前缀和
        # nums中每个数字不一样
        # nums是排序数组
        _sum = 0
        counter = {0: 1}
        count = 0
        k_index = nums.index(k)
        # 子数组 每个元素 对应的含义大于k的元素 和小于k的元素的差值
        # 满足条件的子数组应该是 子数组要么是没有发生变化， 要么是变化之后比变化之前 大于k - 小于k的多了1
        for index, num in enumerate(nums):
            _sum += self.sign(num - k)
            if index < k_index:
                counter[_sum] = counter.setdefault(_sum, 0) + 1
            else:
                prev0 = counter.get(_sum, 0)
                prev1 = counter.get(_sum - 1, 0)
                count += prev0
                count += prev1
        return count

    def sign(self, num):
        return (num > 0) - (num < 0)


if __name__ == '__main__':
    s = Solution()
    ret = s.count_sub_arrays(nums=[3, 2, 1, 4, 5], k=4)
    print(ret)
