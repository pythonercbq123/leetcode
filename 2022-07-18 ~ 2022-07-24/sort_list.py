from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sort_list(self, head: ListNode) -> ListNode:
        return self.helper(head, None)

    def helper(self, head: ListNode, tail: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow, fast = head, head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.helper(head, mid), self.helper(mid, tail))

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        temp1 = head1
        temp2 = head2
        temp = dummy_head
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        if temp2:
            temp.next = temp2
        return dummy_head.next


