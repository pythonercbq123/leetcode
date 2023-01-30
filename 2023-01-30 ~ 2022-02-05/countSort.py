from typing import List


class CountSort:
    def count_sort(self, nums: List):
        max_num, min_num = float('-inf'), float('inf')
        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        counter = [0] * (max_num - min_num + 1)
        for num in nums:
            counter[num - min_num] += 1
        i = 0
        for num in range(min_num, max_num + 1, 1):
            while counter[num - min_num] > 0:
                nums[i] = num
                counter[num - min_num] -= 1
                i += 1
        return nums


if __name__ == '__main__':
    s = CountSort()
    ret = s.count_sort([1, 3, 3, 2, 2, 7, 9, 6, 5, 3, 7, 8])
    print(ret)
