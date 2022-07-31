from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        edges = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        valid = True
        result = []
        for pr in prerequisites:
            x, y = pr
            edges[y].append(x)

        def dfs(v):
            nonlocal valid
            visited[v] = 1
            for w in edges[v]:
                if visited[w] == 0:
                    dfs(w)
                    if not valid:
                        return
                elif visited[w] == 1:
                    valid = False
                    return
            visited[v] = 2
            result.append(v)

        for v in range(numCourses):
            if valid and not visited[v]:
                dfs(v)
        return valid