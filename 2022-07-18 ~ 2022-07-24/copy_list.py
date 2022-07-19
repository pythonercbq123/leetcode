from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    cache = {}

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        backtrack + hashmap to solve
        遍历  + 条件判断 + to do
        """
        if head is None:
            return None
        if head not in self.cache:
            headnew = Node(0)
            headnew.val = head.val
            self.cache[head] = headnew
            headnew.next = self.copyRandomList(head.next)
            headnew.random = self.copyRandomList(head.random)
        return self.cache[head]
