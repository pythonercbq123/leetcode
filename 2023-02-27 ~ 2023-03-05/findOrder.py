from typing import List
from collections import deque


class Solution:
    def find_order(self, coursers: int, prerequisites: List[List[int]]) -> List:
        graph = {}
        for i in range(coursers):
            graph[i] = []
        in_degree = [0] * coursers
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1
        q = deque()
        for k in in_degree:
            if in_degree[k] == 0:
                q.append(k)
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for v in graph.get(course):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        # 可能并不存在拓扑排序
        return order


if __name__ == '__main__':
    s = Solution()
    ret = s.find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print(ret)
