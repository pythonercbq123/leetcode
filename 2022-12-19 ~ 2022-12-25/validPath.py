from collections import defaultdict
from typing import List
from collections import deque


class Solution:
    """
    经典图搜索问题,
    分别采用深度优先， 广度优先 以及 并查集解决
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        :param n:
        :param edges:
        :param source:
        :param destination:
        :return:
        """

        def dfs(s, d, v, g):
            if s == d:
                return True
            visited.add(s)
            for w in g[s]:
                if w not in v and dfs(w, d, v, g):
                    return True
            return False

        graph = defaultdict(list)
        visited = set()
        for edge in edges:
            x, y = edge[0], edge[1]
            graph[x].append(y)
            graph[y].append(x)
        visited.add(source)
        return dfs(source, destination, visited, graph)

    def validPathBfs(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        :param n:
        :param edges:
        :param source:
        :param destination:
        :return:
        """
        graph = defaultdict(list)
        visited = set()
        queue = deque()
        for edge in edges:
            x, y = edge[0], edge[1]
            graph[x].append(y)
            graph[y].append(x)
        queue.append(source)
        while queue:
            v = queue.popleft()
            if v == destination:
                return True
            visited.add(v)
            for adj in graph[v]:
                if adj == destination:
                    return True
                if adj not in visited:
                    queue.append(adj)

        return False

    def validPathUnionFind(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        ufs = UnionFindSet(n)
        for x, y in edges:
            ufs.union(x, y)
        res = ufs.is_connected(source, destination)
        return res


class UnionFindSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        if self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        else:
            self.parent[rootx] = rooty
            self.size[rooty] = rootx

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    s = Solution()
    ret = s.validPathUnionFind(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    print(ret)
