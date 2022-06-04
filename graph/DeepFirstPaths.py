from typing import List, Optional


class Graph:

    def __init__(self, v: int, e: int):
        self.V = v
        self.E = e
        self.adj = []
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


class DeepFirstPaths:
    """
    使用深度优先查找图中的路径
    """

    def __init__(self):
        self.marked: List[bool] = []
        self.edge_to: List[int] = []  # 从起点到一个顶点的已知路径的最后一个顶点
        self.s: int = 0  # 起点

    def deep_first_paths(self, g: Graph, s: int):
        self.marked = [False] * g.V
        self.edge_to = [-1] * g.V
        self.s = s
        self.dfs(g, s)

    def dfs(self, g: Graph, v: int):
        self.marked[v] = True
        for w in g.adj[v]:
            if not self.marked[w]:
                self.edge_to[v] = w
                self.dfs(g, w)

    def has_path_to(self, v: int):
        return self.marked[v]

    def path_to(self, v: int) -> Optional[List]:
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)
        return [i for i in reversed(path)]
