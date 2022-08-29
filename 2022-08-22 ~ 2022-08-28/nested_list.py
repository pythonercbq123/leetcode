
class NestedIterator:
    def __init__(self, nestsList):
        from collections import deque
        self.queue = deque()
        self.dfs(nestsList)

    def dfs(self, nests):
        for item in nests:
            if isinstance(item, int):
                self.queue.append(item)
            else:
                self.dfs(item)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue)
