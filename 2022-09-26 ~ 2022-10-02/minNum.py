from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        求解旋转数组的最小值
        二分查找法
        :param numbers:
        :return:
        """
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            mid = (right + left) // 2
            if numbers[mid] < numbers[right]:
                # 需要包含mid
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                right = right - 1
        return numbers[left]