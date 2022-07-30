from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(cities):
            if i not in visited:
                self.dfs(i, cities, visited, isConnected)
                provinces += 1
        return provinces

    def dfs(self, index, cities, visited, isConnected):
        for j in range(cities):
            if isConnected[index][j] == 1 and j not in visited:
                visited.add(j)
                self.dfs(j, cities, visited, isConnected)