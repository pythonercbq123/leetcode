from typing import List


class Solution:
    def max_two_sum_no_overlap(self, nums: List, first_len: int, second_len: int):
        # 滑动窗口 + 动态规划
        return max(self.helper(nums, first_len, second_len), self.helper(nums, second_len, first_len))

    def helper(self, nums: List, first_len: int, second_len: int) -> int:
        sum_l = 0
        for i in range(first_len):
            sum_l += nums[i]
        max_sum_l = sum_l
        sum_r = 0
        for i in range(first_len, first_len + second_len):
            sum_r += nums[i]
        j = first_len
        res = max_sum_l + sum_r
        for i in range(first_len + second_len, len(nums)):
            sum_l += nums[j] - nums[j - first_len]
            max_sum_l = max(max_sum_l, sum_l)
            sum_r += nums[i] - nums[i - second_len]
            res = max(max_sum_l + sum_r, res)
            j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.max_two_sum_no_overlap([1, 2, 3, 4, 5], 1, 2)
    print(ret)
