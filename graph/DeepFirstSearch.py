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


class DeepFirstSearch:
    def __init__(self):
        self.marked: List[bool] = []
        self.count: int = 0

    def deep_first_search(self, g: Graph, s: int) -> None:
        self.marked = [False] * g.V
        self.dfs(g, s)

    def dfs(self, g: Graph, v: int):
        self.marked[v] = True
        self.count += 1
        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w)


