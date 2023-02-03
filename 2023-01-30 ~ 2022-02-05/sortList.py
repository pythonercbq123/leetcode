
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    排序一个链表
    """
    def sort_list(self, head: ListNode):
        if head is None or head.next is None:
            return head
        head1 = head
        head2 = self.split(head)
        head1 = self.sort_list(head1)
        head2 = self.sort_list(head2)
        return self.merge(head1, head2)

    def split(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        return second

    def merge(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1 is None:
            cur.next = head2
        else:
            cur.next = head1
        return dummy.next


if __name__ == '__main__':

    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(1)

    node1.next = node2
    node2.next = node3
    s = Solution()
    ret = s.sort_list(node1)
    while ret is not None:
        print(ret.val)
        ret = ret.next
