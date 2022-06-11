# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return
        dummy = pre = ListNode(next=head)
        for i in range(0, left - 1):
            pre = pre.next
        start = pre.next
        nxt = start.next
        for i in range(0, right - left):
            start.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = start.next
        return dummy.next
