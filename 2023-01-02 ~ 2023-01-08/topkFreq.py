from typing import List
from collections import defaultdict
import queue


class Solution:
    def topKFreq(self, nums: List, k: int):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        pq = queue.PriorityQueue()
        for num, freq in d.items():
            if pq.qsize() < k:
                pq.put((freq, (num, freq)))
            elif freq > pq.queue[0][0]:
                pq.get()
                pq.put((freq, (num, freq)))
        result = []
        while pq.qsize():
            result.append(pq.get()[1][0])
        return result


if __name__ == '__main__':
    s = Solution()
    ret = s.topKFreq([1, 2, 2, 1, 3, 1, 4, 4, 4, 4], 2)
    print(ret)
