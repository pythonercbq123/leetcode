from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sort_people = sorted(people, key=lambda x: (-x[0], x[1]))
        s = []
        for p in sort_people:
            s[p[1]: p[1]] = [p]
        return s

