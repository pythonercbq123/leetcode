class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for i in range(k + 1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    # make a test func for removeNthEnd
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    k = 2
    s = Solution()
    res = s.removeNthFromEnd(head, k)
    print(res)