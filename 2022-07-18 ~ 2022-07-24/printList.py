from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        rs = []
        n = len(stack)
        for i in range(n):
            rs.append(stack.pop())
        return rs