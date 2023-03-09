from typing import List


class Solution:
    def single_num(self, nums: List[int]) -> int:
        """
        一个数组 只有一个数次出现了一次, 其他数字都出现了3次
        求这个只出现了一次的数字
        :param nums:
        :return:
        """
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                bits[i] += (num >> (31 - i)) & 1

        result = 0
        for i in range(32):
            result = (result << 1) + bits[i] % 3
        return result


if __name__ == '__main__':
    s = Solution()
    ret = s.single_num([1, 0, 0, 1, 1, 0, 5])
    print(ret)
