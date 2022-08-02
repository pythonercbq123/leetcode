from typing import List


class Solution:
    def find_order(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        valid = True
        visited = [0 for _ in range(numCourses)]
        edges = defaultdict(list)
        result = []
        for cur, pre in prerequisites:
            edges[pre].append(cur)

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
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        if not valid:
            return list()
        return result[::-1]
