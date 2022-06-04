from typing import List, Optional, Set
from collections import deque


class Graph:

    def __init__(self, v: int, e: int):
        self.V = v
        self.E = e
        self.adj: List[Set[int]] = []
        for i in range(self.V):
            self.adj.append(set())

    def graph(self, stream):
        for i in range(0, self.E):
            v = stream.readint()
            w = stream.readint()
            self.add_edge(v, w)

    def add_edge(self, v: int, w: int):
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1


class BreadthFirstSearchPaths:

    def __init__(self):
        self.marked: List[bool] = []  # 到达该顶点的最短路径是否已知
        self.edge_to: List[int] = []  # 到达该顶点已知路径的最后一个顶点
        self.s: int = 0  # 起点

    def breadth_first_paths(self, g: Graph, s: int) -> None:
        self.marked = [False] * g.V
        self.edge_to = [-1] * g.V
        self.s = s
        self.bfs(g, s)

    def bfs(self, g: Graph, s: int):
        q = deque()
        q.append(s)
        self.marked[s] = True
        while q:
            v = q.popleft()
            for w in g.adj[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v
                    q.append(w)

    def has_path_to(self, v: int):
        return self.marked[v]

    def path_to(self, v: int):
        if not self.has_path_to(v):
            return None
        x = v
        path = []
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)
        return [i for i in reversed(path)]
