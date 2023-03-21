from typing import List


class Solution:
    def sub_array_num(self, nums: List, k: int) -> int:
        # 和为k的连续子数组个数
        hash_map = dict()
        hash_map[0] = 1
        _sum = 0
        count = 0
        for num in nums:
            _sum += num
            hash_map[_sum] = hash_map.get(_sum, 0) + 1
            count += hash_map.get(_sum - k, 0)
        return count


if __name__ == '__main__':
    s = Solution()
    ret = s.sub_array_num([1, 2, 2, 1, 5], 5)
    print(ret)
