from typing import List, Dict
from collections import deque


class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        """
        判断一个图是否可以被二分,
        :param graph:
        :return:
        """
        n = len(graph)
        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1:
                if not self.set_color(graph, colors, i, 0):
                    return False
        return True

    def set_color(self, graph, colors, i, color):
        q = deque()
        q.append(i)
        colors[i] = color
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] >= 0:
                    if colors[neighbor] == colors[node]:
                        return False
                else:
                    q.append(neighbor)
                    colors[neighbor] = 1 - colors[node]
        return True


if __name__ == '__main__':
    s = Solution()
    ret = s.is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
    print(ret)
    ret = s.is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    print(ret)