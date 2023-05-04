from typing import List
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        BFS
        :param n:
        :param headID:
        :param manager:
        :param informTime:
        :return:
        """
        # 构建邻接表
        adj = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)

        # BFS
        queue = deque()
        # (员工编号，当前时间)时间为到达该员工的时间
        queue.append((headID, 0))
        res = 0
        while queue:
            cur, cur_time = queue.popleft()
            res = max(res, cur_time)
            for i in adj[cur]:
                queue.append((i, cur_time + informTime[cur]))
        return res
