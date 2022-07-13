from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left > right:
            return None
        elif left == right:
            return lists[left]
        else:
            mid = (right + left) >> 1
            return self.mergeTwo(self.merge(lists, left, mid), self.merge(lists, mid + 1, right))

    def mergeTwo(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        if a is None:
            return b
        elif b is None:
            return a
        else:
            head = ListNode(0)
            tail = head
            aPtr = a
            bPtr = b
            while aPtr and bPtr:
                if aPtr.val <= bPtr.val:
                    tail.next = aPtr
                    aPtr = aPtr.next
                else:
                    tail.next = bPtr
                    bPtr = bPtr.next
                tail = tail.next
            if aPtr is not None:
                tail.next = aPtr
            if bPtr is not None:
                tail.next = bPtr

            return head.next


if __name__ == '__main__':
    s = Solution()
    heada = ListNode(0)
    tail = heada
    for i in [1, 4, 5]:
        tail.next = ListNode(i)
        tail = tail.next

    headb = ListNode(0)
    tailb = headb
    for i in [1, 3, 4]:
        tailb.next = ListNode(i)
        tailb = tailb.next

    headc = ListNode(0)
    tailc = headc
    for i in [2, 6]:
        tailc.next = ListNode(i)
        tailc = tailc.next
    r = s.mergeKLists([heada.next, headb.next, headc.next])
    print(r)
