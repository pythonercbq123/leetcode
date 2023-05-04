class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


# make a test func for removeNthFromEnd
def test_removeNthFromEnd():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    res = removeNthFromEnd(head, n)
    print(res)


if __name__ == '__main__':
    test_removeNthFromEnd()
