from typing import List


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


class CC:
    def __init__(self):
        self.marked: List[bool] = []
        self.id: List[int] = []
        self.count = 0

    def cc(self, g: Graph):
        self.marked = [False] * g.V
        self.id = [-1] * g.V
        for s in range(g.V):
            if not self.marked[s]:
                self.dfs(g, s)
                self.count += 1

    def dfs(self, g: Graph, v: int) -> None:
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w)

    def connected(self, v: int, w: int) -> bool:
        return self.id[v] == self.id[w]
