class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here

        dummy = ListNode(-1)
        dummy.next = head
        prev_group_tail = dummy
        while head:
            group_head = head

            count = 0
            while head and count < k:
                head = head.next
                count += 1
            if count < k:
                prev_group_tail.next = group_head
                break
            cur = group_head
            prev = None
            for i in range(k):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            prev_group_tail.next = prev
            prev_group_tail = group_head
        return dummy.next



