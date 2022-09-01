import heapq


class MedianFinder:

    def __init__(self):
        self.queMax = []
        self.queMin = []

    def addNum(self, num: int) -> None:
        q_min = self.queMin
        q_max = self.queMax
        if not q_min or num <= -q_min[0]:
            # -num
            heapq.heappush(q_min, -num)
            if len(q_min) > len(q_max) + 1:
                heapq.heappush(q_max, -heapq.heappop(q_min))
        else:
            heapq.heappush(q_max, num)
            if len(q_max) > len(q_min):
                heapq.heappush(q_min, -heapq.heappop(q_max))

    def findMedian(self) -> float:
        q_min = self.queMin
        q_max = self.queMax
        if len(q_min) > len(q_max):
            return -q_min[0]
        return (-q_min[0] + q_max[0]) / 2
