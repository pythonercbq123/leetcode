class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 递归调用的方法需要O(n)的时间复杂度 ， O(n)的空间复杂度
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    #  以下方法只需要O(1)的时间复杂度
    def reverseList2(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
