from collections import deque
from typing import List
import queue
import heapq

pq = queue.PriorityQueue()
pq.put((5, 'a'))
pq.put((2, 3))
pq.put((2, 1))
pq.put((2, 2))
pq.put((3, 'c'))
t = pq.queue
print(t)
r = pq.get()
print(r)
r = pq.get()
print(r)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        boundary = []
        for i in buildings:
            boundary.append(i[0])
            boundary.append(i[1])
        boundary = sorted(boundary)
        q = queue.PriorityQueue()
        n = len(buildings)
        idx = 0
        ret = []
        for b in boundary:
            while idx < n and buildings[idx][0] <= b:
                q.put((-buildings[idx][2], buildings[idx][1]))
                idx += 1
            while not q.empty() and q.queue[0][1] <= b:
                q.get()
            max_h = -q.queue[0][0] if q.queue else 0
            if len(ret) == 0 or max_h != ret[-1][1]:
                ret.append([b, max_h])
        return ret


if __name__ == '__main__':
    s = Solution()
    ret = s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    print(ret)
