from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = MonotonicQueue()
        n = len(nums)
        for i in range(n):
            if i < k - 1:
                # 先填满窗口的前k-1个
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i - k + 1])
        return res


class MonotonicQueue:
    def __init__(self):
        from collections import deque
        self.q = deque()

    def push(self, n):
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)

    def max(self):
        return self.q[0]

    def pop(self, n):
        if n == self.q[0]:
            self.q.popleft()
