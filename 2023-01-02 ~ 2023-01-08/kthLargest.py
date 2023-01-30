from typing import List
from queue import PriorityQueue


class Solution:
    def __init__(self, nums, k):
        self.size = k
        self.nums = nums
        self.pq = PriorityQueue()

    def kthLargest(self):
        """
        求解数据流中的第k大的数字
        :param nums:
        :param k:
        :return:
        """
        # 构建一个容量为K的小顶堆
        for num in self.nums:
            self.add(num)

    def add(self, num):
        if self.pq.qsize() < self.size:
            self.pq.put((num, num))
        elif self.pq.queue[0][1] < num:
            self.pq.get()
            self.pq.put((num, num))
        return self.pq.queue[0][1]


if __name__ == '__main__':
    s = Solution([4, 5, 8], 3)
    s.kthLargest()
    ret = s.add(2)
    print(ret)
    ret = s.add(5)
    print(ret)
    ret = s.add(10)
    print(ret)
    ret = s.add(11)
    print(ret)